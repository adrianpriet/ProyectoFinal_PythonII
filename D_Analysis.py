from os import listdir
from iteration_utilities import duplicates, unique_everseen
import pandas as pd


def most_expressed_genes():

    list_files = listdir("../data/tpms")

    control = open("../data/a1e80ada.tpm")
    control_lines = control.readlines()

    output_file = open("../output/most_expressed_genes.txt", 'w')

    name_gene_c = []
    N_expression_c = []
    for line in control_lines:
        name_gene_c.append(line.split('\t')[0])
        N_expression_c.append((line.split('\t')[1]))

    for file in list_files:
        name_gene = []
        N_expression = []

        file = open("../data/tpms/" + str(file))
        file_all_lines = file.readlines()

        for line in file_all_lines:
            name_gene.append(line.split('\t')[0])
            N_expression.append(line.split('\t')[1])

        for i in range(0, len(file_all_lines)):
            if N_expression[i] > N_expression_c[i]:
                output_file.write(name_gene[i] + '\t' + str(N_expression[i]))

        # output_file.write('\n')


def core():

    file = open("../output/most_expressed_genes.txt")
    file_all_lines = file.readlines()

    output_file = open("../output/core.txt", 'w')

    name_gene_core = []
    N_expression_core = []
    for line in file_all_lines:
        name_gene_core.append(line.split('\t')[0])
        N_expression_core.append(line.split('\t')[0])

    name_gene_core.sort()

    repetidos = list(duplicates(name_gene_core))
    repetidos_unicos = list(unique_everseen(repetidos))

    repetidos_totales = repetidos + repetidos_unicos
    repetidos_totales.sort()

    for i in repetidos_unicos:
        if i != '\n':
            output_file.write(i + '\n')

    return repetidos_totales


most_expressed_genes()
repetidos_totales = core()
print(repetidos_totales[0:10])
