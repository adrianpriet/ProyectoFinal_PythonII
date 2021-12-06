# Proyecto Final. Python II

## Analisis de expresion diferencial de carcinomas lobulillar y tubular de individuos afroamericanos 

### Integrantes del equipo 

- Rodrigo Daniel Hernandez Barrera [rodrigoh@lcg.unam.mx](mailto:rodrigoh@lcg.unam.mx) 
- Victor Jesus Enriquez Castro [victorec@lcg.unam.mx](mailto:victorec@lcg.unam.mx)
- Adrian Prieto Castellanos [adrianpc@lcg.unam.mx](mailto:adrianpc@lcg.unam.mx)
- Mateo Maya Martinez [mateom@lcg.unam.mx](mailto:mateom@lcg.unam.mx)



### Objetivo 

Realizar un analisis de expresion diferencial, comparando datos de expresion de carcinomas lobulillar y tubular contra un control sano, y obtener el *core transcriptome* de las muestras de cancer.



### Metodologia 

1. Modulo TCGA_Downloader para descargar  los datos de expresion generados por RNA-Seq desde la base de datos [The Cancer Genome Atlas Program](https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga) (Obtenido de https://www.youtube.com/watch?v=YJxcsm4aJXI)

2. Modulo Preparacion_archivos para modificar el formato de los archivos y para normalizar los datos de expresion, pasando de cuentas crudas a datos TPM (Transcripts per million)
3. Modulo Ttest para realizar un analisis estadistico que nos muestra la significancia de los datos
4. Modulo D_Analysis para realizar el analisis de expresion diferencial y obtener el *core transcriptome*. 
5. Modulo ---- para graficar los genes que se encontraron en la mayor cantidad de muestras. 



### Resultados 

Tras analizar los datos de expresión se encontró que un total de 225 proteínas se encuentran sobreexpresadas respecto al control, en los archivos de cáncer utilizados. Además al emplear el T-test se observó que de un total de 20 archivos (correspondientes a cáncer) descargados solo 17 presentaron diferencias significativas con P-values menores a .05 y T-values mayores a |2.00|.


### Conclusion

Podemos concluir que el core (proteínas sobreexpresadas a través de todos los archivos) se va a reducir de manera gradual, conforme aumentamos el número de archivos analizados. Esto es contundente con estudios previos que demuestran que el cáncer es una enfermedad altamente heterogénea, por lo que a mayor número de muestras menor número de proteínas sobreexpresadas en todas ellas.

### Referencias

+ Lawrence, R., Perez, E., Hernández, D., Miller, C., Haas, K., & Irie, H. et al. (2021). The Proteomic Landscape of Triple-Negative Breast Cancer. Retrieved 18 November 2021, from.
+ Mudvari, P., Ohshiro, K., Nair, V., Horvath, A., & Kumar, R. (2013). Genomic Insights into Triple-Negative and HER2-Positive Breast Cancers Using Isogenic Model Systems. Plos ONE, 8(9), e74993. https://doi.org/10.1371/journal.pone.0074993
+ Corrie, P. (2008). Cytotoxic chemotherapy: clinical aspects. Medicine, 36(1), 24-28. https://doi.org/10.1016/j.mpmed.2007.10.012
+ Chiu, A., Mitra, M., Boymoushakian, L., & Coller, H. (2018). Integrative analysis of the inter-tumoral heterogeneity of triple-negative breast cancer. Scientific Reports, 8(1). https://doi.org/10.1038/s41598-018-29992-5
+ Moreira, M., Brayner, F., Alves, L., Cassali, G., & Silva, L. (2019). Phenotypic, structural, and ultrastructural analysis of triple-negative breast cancer cell lines and breast cancer stem cell subpopulation. European Biophysics Journal, 48(7), 673-684. https://doi.org/10.1007/s00249-019-01393-0
+ RNA-Seq Analysis. (2021). Retrieved 6 December 2021, from https://www.strand-ngs.com/files/manual/reference/rnaseq.html
