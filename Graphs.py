'''
NAME
        Graphs.py

VERSION
        1.2

AUTHOR
        Rodrigo Daniel Hernández Barrera  <rodrigoh@lcg.unam.mx>
        Mateo Maya Martínez <mateom@lcg.unam.mx>

DESCRIPTION
        Este módulo trabaja con el archivo most_expressed_genes que puede ser generado con el
        módulo D_Analysis. Contiene 3 funciones, la primera genera una gráfica de pastel que muestra
        la cantidad de genes que se sobreexpresaron en más muestras. La segunda función grafica
        los niveles de expresión para 10 de los genes sobreexpresados que se encontraron en todas las
        muestras. La tercera función hace una gráfica de barras con los 20 niveles de expresión para
        cada uno de 10 genes que estan sobreexpresados en todas las muestras.

CATEGORY
        Module

USAGE
        Para usar este modulo se debe:
        importar el paquete:
            import Graphs
        y llamar cada una de las funciones:
            Graphs.expression_each_gene()

INPUT
        Este programa recibe como input un archivo de expresión génica normalizado.

OUTPUT
        Solo genera las imágenes

GITHUB
        https://github.com/rod13-afk/ProyectoFinal_PythonII/blob/master/Graphs.py
'''


# Importación de librerías
import pandas as pd
from iteration_utilities import duplicates, unique_everseen
import matplotlib.pyplot as plt
import random
import numpy as np


def mayores_repeticiones():
    """
    Funcion para graficar un pie chart que muestre los genes
    que se encuentran en más de quince archivos.

    """

    # Abrir el archivo generado por la funcion most_expressed_genes del módulo D_Analysis y leerlo por líneas.
    most_expressed = open("../output/most_expressed_genes.txt")
    most_expressed_lines = most_expressed.readlines()

    # Inicializar una lista para guardar los nombres de los genes más expresados.
    name_gene_most_expressed = []

    # Separar el archivo por columnas y guardar el nombre de los genes.
    for line in most_expressed_lines:
        name_gene_most_expressed.append(line.split('\t')[0])

    # Ordenar la lista.
    name_gene_most_expressed.sort()

    # Inicializar la lista que guardará las ocurrencias.
    matches = []

    # Contar las ocurrencias para cada gen y guardarlas en la lista
    for i in name_gene_most_expressed:
        a = (i, name_gene_most_expressed.count(i))
        matches.append(a)

    # Eliminar las repeticiones de las ocurrencias y guardar el resultado en una lista.
    repetidos = duplicates(matches)
    repetidos_unicos = unique_everseen(repetidos)
    repetidos_unicos = list(repetidos_unicos)

    # Inicializar las listas que gardarán el nombre, el valor y las parejas gen- nivel de expresión
    data_list = []
    name = []
    value = []

    # Para cada gen guardar su nombre y su valor.
    for i in repetidos_unicos:
        name.append(i[0])
        value.append(i[1])

    # Hacer el data frame con las parejas gen-nivel de expresión.
    data_list = [(name), (value)]
    df = pd.DataFrame(data_list).T
    df.columns = ['Gene', ('Value')]

    # Inicializar la lista que guardarán el nombre, el valor de expresión de cada gen.
    value_1 = []
    name_1 = []
    # Determinar los genes que están en 15 o más de las muestras y guardarlos.
    for i in range(0, len(value)):
        if value[i] >= 15:
            name_1.append(name[i])
            value_1.append(value[i])

    # Hacer un data frame con el nombre del gen y el número de repeticiones.
    data_list_2 = [(name_1), (value_1)]
    df_2 = pd.DataFrame(data_list_2).T
    df_2.columns = ['Gene', 'Repeticiones']

    # Acceder a los renglones del data frame cuyo número de repeticiones sea mayor a 15 y guardar
    # el número de repeticiones.
    count_rep = []
    for i in range(15, 18):
        boolean = df_2["Repeticiones"] == i
        index = boolean[boolean].index
        count_rep.append(len(df_2.iloc[index, :]))

    # Graficar el pie chart y darle formato.
    desfase = (0, 0, 0.1)
    plt.pie(count_rep, labels=['15 repeticiones', '16 repeticiones', '17 repeticiones'], explode=desfase, colors=['#2ee8bb', '#276ab3', '#750851'],
                    autopct="%0.1f %%")

    plt.title('Genes repetidos mas de 15 veces')
    plt.show()


def expresion_mayores_repeticiones():

    """
    Función para graficar el nivel de expresión de 10 genes aleatorios presentes en todos los archivos.
    """

    # Abrir el archivo generado por la funcion most_expressed_genes del módulo D_Analysis y leerlo por líneas.
    most_expressed = open("../output/most_expressed_genes.txt")
    most_expressed_lines = most_expressed.readlines()

    # Inicializar las listas para guardar los nombres y el nivel de expresión de los genes más expresados.
    name_gene_most_expressed = []
    expression_gene_most_expressed = []

    # Separar el archivo por columnas y guardar el nombre de los genes.
    for line in most_expressed_lines:
        name_gene_most_expressed.append(line.split('\t')[0])
        expression_gene_most_expressed.append(line.split('\t')[1])

    # Ordenar la lista.
    name_gene_most_expressed_sorted = sorted(name_gene_most_expressed)

    # Inicializar la lista que guardará las ocurrencias.
    matches = []

    # Contar las ocurrencias para cada gen y guardarlas en la lista
    for i in name_gene_most_expressed_sorted:
        a = (i, name_gene_most_expressed_sorted.count(i))
        matches.append(a)

    # Eliminar las repeticiones de las ocurrencias y guardar el resultado en una lista.
    repetidos = duplicates(matches)
    repetidos_unicos = unique_everseen(repetidos)
    repetidos_unicos = list(repetidos_unicos)

    # Inicializar las listas que gardarán el nombre, el valor y las parejas gen- nivel de expresión
    data_list = []
    name = []
    value = []

    # Para cada gen guardar su nombre y su valor.
    for i in repetidos_unicos:
        name.append(i[0])
        value.append(i[1])

    # Hacer el data frame con las parejas gen-nivel de expresión.
    data_list = [(name), (value)]
    df = pd.DataFrame(data_list).T
    df.columns = ['Gene', ('Value')]

    # Inicializar la lista que guardarán el nombre de cada gen.
    name_1 = []

    # Determinar los genes que están en 20 muestras y guardarlos.
    for i in range(0, len(value)):
        if value[i] == 17:
            name_1.append(name[i])

    # Tomar una muestra aleatoria de diez genes
    random_genes = random.sample(name_1, 10)

    # Guardar los valores de expresión de los genes aleatorios.
    expression_list = []
    for gen in random_genes:
        for i in range(0, len(name_gene_most_expressed)):
            if gen == name_gene_most_expressed[i]:
                expression_list.append(float(expression_gene_most_expressed[i].strip('\n')))

    # Separar las listas cada diez elementos.
    n = 10
    endlist = [[] for _ in range(n)]
    for index, item in enumerate(expression_list):
        endlist[index % n].append(item)

    # Graficar.
    x = np.arange(1, 18, 1)
    plt.xlim(1, 18)
    default_x_ticks = range(len(x))
    plt.xticks(np.arange(0, 18, step=1))

    for lista in endlist:
        y = lista
        plt.plot(x, y, marker='.')

    plt.legend(random_genes)
    plt.xlabel('Numero de muestra')
    plt.ylabel('Nivel de expresion')
    plt.title('Nivel de expresion de 10 de los genes mas conservados')
    plt.show()


def expression_each_gene():

    """
        Función para graficar en una gráfica de barras el nivel de expresión
        de cada uno de los 10 genes aleatorios presentes en todos los archivos.

    """
    # Abrir el archivo generado por la funcion most_expressed_genes del módulo D_Analysis y leerlo por líneas.
    most_expressed = open("../output/most_expressed_genes.txt")
    most_expressed_lines = most_expressed.readlines()

    # Inicializar las listas para guardar los nombres y el nivel de expresión de los genes más expresados.
    name_gene_most_expressed = []
    expression_gene_most_expressed = []

    # Separar el archivo por columnas y guardar el nombre de los genes.
    for line in most_expressed_lines:
        name_gene_most_expressed.append(line.split('\t')[0])
        expression_gene_most_expressed.append(line.split('\t')[1])

    # Ordenar la lista.
    name_gene_most_expressed_sorted = sorted(name_gene_most_expressed)
    matches = []

    # Contar las ocurrencias para cada gen y guardarlas en la lista
    for i in name_gene_most_expressed_sorted:
        a = (i, name_gene_most_expressed_sorted.count(i))
        matches.append(a)

    # Eliminar las repeticiones de las ocurrencias y guardar el resultado en una lista.
    repetidos = duplicates(matches)
    repetidos_unicos = unique_everseen(repetidos)
    repetidos_unicos = list(repetidos_unicos)

    # Inicializar las listas que gardarán el nombre, el valor y las parejas gen- nivel de expresión
    data_list = []
    name = []
    value = []

    # Para cada gen guardar su nombre y su valor.
    for i in repetidos_unicos:
        name.append(i[0])
        value.append(i[1])

    # Hacer el data frame con las parejas gen-nivel de expresión.
    data_list = [(name), (value)]
    df = pd.DataFrame(data_list).T
    df.columns = ['Gene', ('Value')]

    # Inicializar la lista que guardarán el nombre de cada gen.
    name_1 = []

    # Determinar los genes que están en 20 muestras y guardarlos.
    for i in range(0, len(value)):
        if value[i] == 17:
            name_1.append(name[i])

    # Tomar una muestra aleatoria de diez genes
    random_genes = random.sample(name_1, 10)

    # Guardar los valores de expresión de los genes aleatorios.
    expression_list = []
    for gen in random_genes:
        for i in range(0, len(name_gene_most_expressed)):
            if gen == name_gene_most_expressed[i]:
                expression_list.append(float(expression_gene_most_expressed[i].strip('\n')))

    # Separar las listas cada diez elementos.
    n = 10
    endlist = [[] for _ in range(n)]
    for index, item in enumerate(expression_list):
        endlist[index % n].append(item)

    # Graficar.
    x = np.arange(1, 18, 1)

    i = 0
    for lista in endlist:
        y = lista

        plt.xlim(1, 18)
        default_x_ticks = range(len(x))
        plt.xticks(np.arange(0, 18, step=1))

        plt.bar(x, y, color='#ff5b00')
        plt.xlabel('Numero de muestra')
        plt.ylabel('Nivel de expresion')
        plt.title('Nivel de expresion del gen ' + str(random_genes[i]))
        plt.show()
        i += 1


mayores_repeticiones()
expresion_mayores_repeticiones()
expression_each_gene()
