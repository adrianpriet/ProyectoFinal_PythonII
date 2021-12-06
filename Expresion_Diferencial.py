'''
NAME
        Expresion_Diferencial.py

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro  <victorec@lcg.unam.mx>
        Adrian Prieto Castellanos <adrianpc@lcg.unam.mx>

DESCRIPTION
        Este programa se encarga de llamar a las funciones necesarias 
        para realizar el analisis, a su vez nos permite seleccionar los argumentos  

CATEGORY
        Gene expression

INPUT
        Este programa recibe como input una serie de rutas a distintos archivos, asi como 
        el argumento necesario para seleccionar la funcion

GITHUB

'''

import os
import argparse
import pandas as pd
from  D_Analysis import *
from Graphs import *
from Preparacion_archivos import *
from Ttest import *


#Argumentos
# Se crea el parser
parser = argparse.ArgumentParser(description="Accede a los archivos dadas las rutas")

# Agregamos los argumentos
parser.add_argument("-F", "--Funcion",
                    help="Seleccion de funcion para correr",
                    required=False)
parser.add_argument("-c", "--crudas",
                    help="Ruta al archivo con cuentas crudas",
                    required=False)
parser.add_argument("-o", "--output",
                    help="Ruta al archivo output",
                    required=False)
parser.add_argument("-l", "--list",
                    help="Ruta al archivo con la lista de genes",
                    required=False)
parser.add_argument("-e", "--length",
                    help="Ruta al archivo con las longitudes de los genes",
                    required=False)

args = parser.parse_args()

funcion = args.Funcion

if funcion == '1':
    ruta_cuentas_crudas = args.crudas
    ruta_cuentas_nuevas = args.output
    obtener_nombres(ruta_cuentas_crudas,ruta_cuentas_nuevas)

if funcion == '2':
    ruta_gene_list = args.list
    ruta_gene_lengths = args.length
    obtener_longitudes(ruta_gene_list, ruta_gene_lengths)

if funcion == '3':
    ruta_cuentas_crudas = args.crudas
    ruta_gene_lengths = args.length
    ruta_ff = args.output
    normalizacion(ruta_cuentas_crudas, ruta_gene_lengths, ruta_ff)

if funcion == '4':
    print(stats())

if funcion == '5':
    most_expressed_genes()

if funcion == '6':
    core()

if funcion == '7':
    expression_each_gene()
