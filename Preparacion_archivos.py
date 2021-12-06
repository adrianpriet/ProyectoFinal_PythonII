'''
NAME
        Preparacion_archivos.py

VERSION
        2.0

AUTHOR
        Victor Jesus Enriquez Castro  <victorec@lcg.unam.mx>
        Adrian Prieto Castellanos <adrianpc@lcg.unam.mx>

DESCRIPTION
        Este programa cuenta con varias funciones que nos sirven para el 
	correcto manejo y preparacion de archivos.
	Función obtener_nombres: Con esta función obtenemos los nombres
	que se encuentran en los archivos a traves de su ID.
	Función obtener_longitudes: Con esta función obtenemos las longitudes
	de los genes que se encuentra en nuestros archivos.
	Funcion normalización: Con esta se normalizan el formato de todos los
	archivos a su vez se obtienen los tpm(transcritos por millon).
	

CATEGORY
        Funcion

INPUT
        Este programa recibe como input una serie de rutas a distintos archivos
	'../data/e740e34f/e740e34f.tpm', '../data/e023c283/e023c283.tpm', '../data/d7bff2a7/d7bff2a7.tpm',
        '../data/c71784ba/c71784ba.tpm', '../data/c592e62e/c592e62e.tpm', '../data/bb804a2f/bb804a2f.tpm',
        '../data/b3f7a18b/b3f7a18b.tpm', '../data/a1e80ada/a1e80ada.tpm', '../data/97745843/97745843.tpm',
        '../data/743ef32d/743ef32d.tpm', '../data/0e397288/0e397288.tpm', '../data/1e7b2b3b/1e7b2b3b.tpm',
        '../data/40a5ed6b/40a5ed6b.tpm', '../data/03d7d46d/03d7d46d.tpm', '../data/4fd836c4/4fd836c4.tpm',
        '../data/5d3c2256/5d3c2256.tpm', '../data/7cf82e1d/7cf82e1d.tpm', '../data/8b26a752/8b26a752.tpm',
        '../data/8ddc8e8b/8ddc8e8b.tpm', '../data/39d6716f/39d6716f.tpm'

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



#Dado que las longitudes son necesarias para normalizar, esta función
# genera un lista de genes con su respectiva longitud
def obtener_longitudes(ruta_gene_list,ruta_gene_lengths):
	file_o = open(ruta_gene_list) #recibe la ruta del archivo con la lista de genes (nombres)
	all_lines = file_o.readlines()

	file_n = open(ruta_gene_lengths,'w')#ruta del archivo que se generara

	# Dado que no todos los ids del archivo están correctamente anotados,
	# este for obtiene las longitudes de los genes de la base de datos Ensenmbl
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

	#Se obtiene la suma de todos los rpks y se divide por un millón
	for i in range(0,len(lines_rpks)):
		rpks += float(lines_rpks[i].split('\t')[1].replace('\n',''))
		
	scaling_factor = rpks/1000000

	#Se obtienen los valores tpm
	for i in range(0,len(lines_rpks)):
		rpk = float(lines_rpks[i].split('\t')[1].replace('\n','')) / scaling_factor
		file_final.write(lines_rpks[i].split('\t')[0]+'\t'+str(rpk)+'\n')

	return(ruta_ff)
