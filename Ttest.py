'''
NAME
        Ttest.py

VERSION
        2.0

AUTHOR
        Victor Jesus Enriquez Castro  <victorec@lcg.unam.mx>
        Adrian Prieto Castellanos <adrianpc@lcg.unam.mx>

DESCRIPTION
        Este programa contiene una funcion que realiza un análisis
        estadístico llamado T-test para evaluar si la diferencia
        de expresión de las diferentes muestras es significativa
        deacuerdo al grupo control.

CATEGORY
        Función 

INPUT
       La direccion de los archivos de las muestras como del control.
       '../data/e740e34f/e740e34f.tpm', '../data/e023c283/e023c283.tpm', '../data/d7bff2a7/d7bff2a7.tpm',
       '../data/c71784ba/c71784ba.tpm', '../data/c592e62e/c592e62e.tpm', '../data/bb804a2f/bb804a2f.tpm',
       '../data/b3f7a18b/b3f7a18b.tpm', '../data/a1e80ada/a1e80ada.tpm', '../data/97745843/97745843.tpm',
       '../data/743ef32d/743ef32d.tpm', '../data/0e397288/0e397288.tpm', '../data/1e7b2b3b/1e7b2b3b.tpm',
       '../data/40a5ed6b/40a5ed6b.tpm', '../data/03d7d46d/03d7d46d.tpm', '../data/4fd836c4/4fd836c4.tpm',
       '../data/5d3c2256/5d3c2256.tpm', '../data/7cf82e1d/7cf82e1d.tpm', '../data/8b26a752/8b26a752.tpm',
       '../data/8ddc8e8b/8ddc8e8b.tpm', '../data/39d6716f/39d6716f.tpm'
       ../data/Control.txt

GITHUB
        https://github.com/rod13-afk/ProyectoFinal_PythonII/edit/master/Ttest.py
'''

#Se importan las librerias
import numpy as np
import pandas as pd
from scipy.stats import ttest_rel
from tabulate import tabulate

#Definimos la funcion que realiza el T-test a los subsets de datos
def stats():

    #Creamos una lista con los nombres de los archivos
    file_list = ['../data/e740e34f/e740e34f.tpm', '../data/e023c283/e023c283.tpm', '../data/d7bff2a7/d7bff2a7.tpm',
                     '../data/c71784ba/c71784ba.tpm', '../data/c592e62e/c592e62e.tpm', '../data/bb804a2f/bb804a2f.tpm',
                     '../data/b3f7a18b/b3f7a18b.tpm', '../data/a1e80ada/a1e80ada.tpm', '../data/97745843/97745843.tpm',
                     '../data/743ef32d/743ef32d.tpm', '../data/0e397288/0e397288.tpm', '../data/1e7b2b3b/1e7b2b3b.tpm',
                     '../data/40a5ed6b/40a5ed6b.tpm', '../data/03d7d46d/03d7d46d.tpm', '../data/4fd836c4/4fd836c4.tpm',
                     '../data/5d3c2256/5d3c2256.tpm', '../data/7cf82e1d/7cf82e1d.tpm', '../data/8b26a752/8b26a752.tpm',
                     '../data/8ddc8e8b/8ddc8e8b.tpm', '../data/39d6716f/39d6716f.tpm', ]

    #Creamos una serie de listas que nos permiten almacenar datos y dar formato a la tabla
    header = ['ID', 'T-value', 'P-value']
    datos = []
    ids = []

    #Se lee el archivo control
    file_c = open('../data/Control.txt')
    lines_c = file_c.readlines()

    #Se obtienen los valores de expresion de los genes para cada archivo,
    # y posteriormente se guardan en un array de modo que sea posible
    # la realizacion del T-test. El resultado del Ttest se guarda en una lista
    for i in range(0,len(file_list)):
        file_p = open(file_list[i])
        lines_p = file_p.readlines()

        ids.append(file_list[i].split('/')[2])

        v_exp_paciente = []
        v_exp_control = []

        for i in range(0,len(lines_p)):
            v_exp_paciente.append(float(lines_p[i].split('\t')[1].replace('\n','')))

        for i in range(0,len(lines_c)):
            v_exp_control.append(float(lines_c[i].split('\t')[1].replace('\n','')))

        paciente = pd.array(v_exp_paciente)
        control = pd.array(v_exp_control)

        datos.append(ttest_rel(paciente, control))

    #Damos formato a los datos para poder presentarlos como una tabla
    statistics = pd.Series(datos,
                           index=ids,
                           name='Estadisticas')
