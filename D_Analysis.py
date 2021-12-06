'''
NAME
        D_Analysis.py

VERSION
        2.0

AUTHOR
        Rodrigo Daniel Hernandez Barrera  <rodrigoh@lcg.unam.mx>
        Mateo Maya Martinez <mateom@lcg.unam.mx>

DESCRIPTION
        Este modulo trabaja con archivos con datos de expresion genica, normalizados a TPM,
        en un formato de dos columnas, una de las columnas contiene los nombres de los genes
        y la segunda los nivlees de expresion normalizados para el gen. Contiene una funcion
        que genera el archivo most_expressed_genes, el cual contiene el nombre de los genes
        mas expresados y su nivel de expresion, para cada uno de los archivos input. La segunda
        funcion utiliza el archivo most_expressed_genes para crear un nuevo archivo que contiene
        el core transcriptome.

CATEGORY
        Module

USAGE
        Para usar este modulo se debe:
        importar el paquete:
            import D_Analysis
        y llamar cada una de las funciones:
            D_Analysis.most_expressed_genes()

INPUT
        Este programa recibe como input archivos de expresion genica normalizados.

OUTPUT
        Archivo most_expressed_genes.txt
        Archivo core.txt

GITHUB
        https://github.com/rod13-afk/ProyectoFinal_PythonII/blob/master/D_Analysis.py
'''

# Importación de librerías
from os import listdir
import numpy
from iteration_utilities import duplicates, unique_everseen
import pandas as pd
from numpy import mean

def most_expressed_genes():
    """
        Funcion para determinar los genes que están sobreexpresados
        con respecto al control. Para cada archivo se evalúa si cada
        gen tiene un nivel de expresión mayor que el del control. También
        se calcula el promedio de expresión de los genes sobreexpresados.

        """

    # Definir el directorio que contiene los archivos.
    list_files = listdir("../data/tpms")

    # Abrir el archivo control y leerlo por líneas
    control = open("../data/Control_1.txt")
    control_lines = control.readlines()

    #Crear un archivo en el que se escribirá el output.
    output_file = open("../output/most_expressed_genes.txt", 'w')

    #Inicializar listas que guardarán los genes y el nivel de expresión.
    name_gene_c = []
    N_expression_c = []

    # Separar el archivo control por columnas.
    for line in control_lines:
        name_gene_c.append(line.split('\t')[0])
        N_expression_c.append((line.split('\t')[1]))

    # Hacer una lista cuyos elementos sean parejas gen-expresión y formatearla como data frame.
    data_list = [(name_gene_c), (N_expression_c)]
    df = pd.DataFrame(data_list).T
    df.columns = ['Gene', 'Expression']
    # Eliminar los saltos de línea.
    df['Expression'] = df['Expression'].str.rstrip('\n')

    # Inicializar las listas que guardarán el nombre del gen, el nivel de expresión, y el nivel de expresión de los
    # que se encuentran sobreexpresados.
    i = 1
    name_gene = []
    N_expression = []
    data_mean = []

    # Leer cada archivo por líneas, separarlo por columnas y generar un data frame con las parejas gen-expresión.
    for file in list_files:

        file = open("../data/tpms/" + str(file))
        file_all_lines = file.readlines()

        for line in file_all_lines:
            name_gene.append(line.split('\t')[0])
            N_expression.append(line.split('\t')[1].strip('\n'))

        data_list = [(name_gene), (N_expression)]
        df = pd.DataFrame(data_list).T
        df.columns = ['Gene', ('Expression' + str(i))]
        df['Expression'] = df[('Expression' + str(i))].str.rstrip('\n')

        # Determinar si los genes están sobreexpresados.
        for i in range(0, len(file_all_lines)):
            if N_expression[i] > N_expression_c[i]:
                data_mean.append(float(N_expression[i]))

    # Cálculo del promedio de los niveles de expresión de los genes sobreexpresados.
    numpy_array = numpy.array(data_mean)
    promedio = mean(numpy_array)
    promedio.tolist()

    # Si nivel de expresión de un gen es mayor al promedio, se escribe en un archivo.
    for i in range(0, len(N_expression)):
        if float(N_expression[i]) > float(promedio):
            output_file.write(name_gene[i] + '\t' + str(N_expression[i]) + '\n')

    i += 1



def core():

    """
    Funcion para calcular el core de los genes sobreexpresados
    a partrir del archivo most_expressed_genes.txt.

    """

    # Abrir el archivo generado por la función most_expressed_genes y leerlo por líneas.
    file = open("../output/most_expressed_genes.txt")
    file_all_lines = file.readlines()

    # Crear el archivo output
    output_file = open("../output/core.txt", 'w')

    # Inicializar las listas que contendrán los genes y niveles de expresión.
    name_gene_core = []
    N_expression_core = []

    # Separar el archivo por columnas.
    for line in file_all_lines:
        name_gene_core.append(line.split('\t')[0])
        N_expression_core.append(line.split('\t')[0])

    # Ordenar la lista.
    name_gene_core.sort()

    # Encontrar los genes repetidos y guardar sus ocurrencias.
    repetidos = list(duplicates(name_gene_core))
    repetidos_unicos = list(unique_everseen(repetidos))
    repetidos_totales = repetidos + repetidos_unicos
    repetidos_totales.sort()

    # Escribir los genes repetidos (con solo una ocurrencia) en un archivo.
    for i in repetidos_unicos:
        if i != '\n':
            output_file.write(i + '\n')

#most_expressed_genes()
#core()

