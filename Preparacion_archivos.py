'''
NAME
        Preparacion_archivos.py

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro  <victorec@lcg.unam.mx>
        Adrian Prieto Castellanos <adrianpc@lcg.unam.mx>

DESCRIPTION
        Este programa prepara los archivos de modo  que se pueda realizar un analisis de
        expresion diferencial a partir de archivos con cuentas crudas

CATEGORY
        Funcion

INPUT
        Este programa recibe como input una serie de rutas a distintos archivos

GITHUB
	https://github.com/rod13-afk/ProyectoFinal_PythonII/blob/master/Preparacion_archivos.py
'''

#Importamos las librerias
from pyensembl import EnsemblRelease
from os import path
from Bio import Entrez, SeqIO
from Bio import ExPASy 
from Bio import SwissProt

#Llamamos el genoma referencia de Ensembl
data = EnsemblRelease(77)

#Accedemos con nuestro correo
Entrez.email = "victorec@lcg.unam.mx" 

#Generamos lista de genes (nombre	cuenta)
def obtener_nombres(ruta_cuentas_crudas,ruta_cuentas_nuevas):
	file_o = open(ruta_cuentas_crudas)#ruta del archivo con cuentas original
	all_lines = file_o.readlines()

	file_n = open(ruta_cuentas_nuevas,'w') #ruta donde se genera el archivo

	#Dado que no todos los ids del archivo estan correctamente anotados,
	# este for obtiene los nombres de los genes de la base de datos Ensenmbl
	# siempre y cuando esten correctamente anotados
	for line in all_lines:
		try:
			id = line.split('\t')[0].split('.')[0]
			gene = data.gene_by_id(id)
			file_n.write(gene.gene_name+'\t'+line.split('\t')[1])
		except ValueError:
			break
			
	return(ruta_cuentas_nuevas)



#Dado que las longitudes son necesarias para normalizar, esta funcion
# genera un lista de genes con su respectiva longitud
def obtener_longitudes(ruta_gene_list,ruta_gene_lengths):
	file_o = open(ruta_gene_list) #recibe la ruta del archivo con la lista de genes (nombres)
	all_lines = file_o.readlines()

	file_n = open(ruta_gene_lengths,'w')#ruta del archivo que se generara

	# Dado que no todos los ids del archivo estan correctamente anotados,
	# esta for obtiene las longitudes de los genes de la base de datos Ensenmbl
	# siempre y cuando esten correctamente anotados
	for line in all_lines:
		try:
			name = line.replace('\n','')
			gene = data.genes_by_name(name)
			gene = gene[0]
			gene_len =  gene.end - gene.start
			file_n.write(name+'\t'+str(gene_len)+'\n')
		except ValueError:
			break
			
	return(ruta_gene_lengths)



#Se normalizan los datos para poder realizar comparaciones
def normalizacion(ruta_cuentas,ruta_gene_lengths,ruta_ff):

	#Se accede y se leen los archivos
	file_cn = open(ruta_cuentas)#ruta al archivo con cuentas crudas
	al_lines = file_cn.readlines()
	file_l = open(ruta_gene_lengths)#ruta al archivo con las longitudes de los genes
	all_lines = file_l.readlines()

	# se crea tanto un archivo transitorio que nos permitira almacenar de manera
	# ordena el valor de rpk para cada gen, como el archivo final normalizado
	file_rpk = open('../data/file_rpk.txt','w')
	file_final = open(ruta_ff,'w')

	#Se obtiene el valor de rpk para cada gen
	for i in range(0,len(al_lines)):
		rpk = float(al_lines[i].split('\t')[1]) / float(all_lines[i].split('\t')[1])
		file_rpk.write(al_lines[i].split('\t')[0]+'\t'+str(rpk)+'\n')

	#Se leen los datos almacenados en el archivo transitorio
	file_rpk = open('../data/file_rpk.txt','r')
	lines_rpks = file_rpk.readlines()
	
	rpks = 0

	#Se obtiene la suma de todos los rpks y se divide por un millon
	for i in range(0,len(lines_rpks)):
		rpks += float(lines_rpks[i].split('\t')[1].replace('\n',''))
		
	scaling_factor = rpks/1000000

	#Se obtienen los valores tpm
	for i in range(0,len(lines_rpks)):
		rpk = float(lines_rpks[i].split('\t')[1].replace('\n','')) / scaling_factor
		file_final.write(lines_rpks[i].split('\t')[0]+'\t'+str(rpk)+'\n')

	return(ruta_ff)
