#  Proyecto Final. Python II.

## Analisis de expresion diferencial de carcinomas lobulillar y tubular de individuos afroamericanos. 

### Integrantes del equipo. 

- Rodrigo Daniel Hernandez Barrera [rodrigoh@lcg.unam.mx](mailto:rodrigoh@lcg.unam.mx) 
- Victor Jesus Enriquez Castro [victorec@lcg.unam.mx](mailto:victorec@lcg.unam.mx)
- Adrian Prieto Castellanos [adrianpc@lcg.unam.mx](mailto:adrianpc@lcg.unam.mx)
- Mateo Maya Martinez [mateom@lcg.unam.mx](mailto:mateom@lcg.unam.mx)



### Introducción.

El cáncer de mama es el tipo más común de cáncer a nivel mundial, se trata de una enfermedad altamente heterogénea lo que tiene un gran impacto en la respuesta al tratamiento y el resultado clínico.
Las terapias dirigidas disponibles actualmente se aprovechan de la sobreexpresión de los receptores ER (Estrogenic Receptor alfa), PR (Progesterone Receptor) y HER2 (Human Epidermal Growth Factor 2 receptor).
debido a esto al momento no hay terapias dirigidas disponibles para tumores que no expresan estos receptores. Por lo que el objetivo de este proyecto es identificar aquellas proteínas que se sobreexpresan en un subset de 20 muestras obtenidas de pacientes con cáncer de mama, con la finalidad de identificar posibles blancos terapéuticos.



### Objetivo. 

Realizar un analisis de expresion diferencial, comparando datos de expresion de carcinomas lobulillar y tubular contra un control sano, y obtener el *core transcriptome* de las muestras de cancer.



### Metodologia. 

1. Modulo TCGA_Downloader para descargar  los datos de expresion generados por RNA-Seq desde la base de datos [The Cancer Genome Atlas Program](https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga) (Obtenido de https://www.youtube.com/watch?v=YJxcsm4aJXI)

2. Modulo Preparacion_archivos para modificar el formato de los archivos y para normalizar los datos de expresion, pasando de cuentas crudas a datos TPM (Transcripts per million)
3. Modulo Ttest para realizar un analisis estadistico que nos muestra la significancia de los datos
4. Modulo D_Analysis para realizar el analisis de expresion diferencial y obtener el *core transcriptome*. 
5. Modulo Graphs para graficar los genes que se encontraron en la mayor cantidad de muestras. 



### Resultados. 

1. Se descargaron 20 archivos de expresion de la base de datos The Cancer Genome Atlas Program, con las cuentas crudas para al rededor de 20,000 genes representados con el ID de Ensembl, por lo tanto se uso el modulo Preparacion_archivos para modificar el formato, obtener el nombre real del gen y normalizar los datos de expresion. Se obtuvieron los archivos con el nombre del gen y los datos normalizados a TPM.  

​			                              		   	![](/output/archivo_crudo.jpeg)					

​														Fig 1. Archivo con cuentas crudas



![](/output/archivo_norm.jpeg)

Fig 2. Archivo con cuentas normalizadas 



2. Posteriormente se hizo un T-test para comprobar que los datos observados tienen p-values y T-values y poder rechazar la hipotesis de que la varianza entre los datos del control y del cancer no es significativa. Se realizo entre el control y cada uno de los 20 archivos y solo 17 de estos pasaron la prueba y se utilizaron en las siguientes pruebas. 

   

​		                               ![](/output/tabla_pvalue.jpeg)      

Fig 3. Datos del T-test para cada archivo



3. Con los 17 archivos que pasaron la prueba se realizo el modulo D_Analysis para identificar los genes que mas se expresaron en estos archivos. Los resultados se almacenaron en el archivo most_expressed_genes, en este archivo se tienen los nombres de los genes y su nivel de expresion, pero debido a que son los resultados de todos los archivos, era necesario eliminar las repeticiones y utilizar una sola copia del gen para crear el *core transcriptome*.  El *core transcriptome* se almacena en un archivo nuevo, donde solo podemos ver el nombre de los genes sobreexpresados compartidos entre los 17 archivos. En total nuestro *core transcriptome* esta formado por 217 genes 

​											![](/output/most2.jpeg)	

Fig 4. Primeros 15 elementos del archivo most_expressed_genes



​							                       				![](/output/core.jpeg)

Fig 5. Primeros 15 elementos del archivo core



4. A partir del archivo most_expressed_genes se grafico la cantidad de genes que estan mas repetidos entre los archivos, aquellos que se encuentran en 15, 16 y 17 muestras. 

​		![](/output/Genes_repetidos_mas_de_15_veces.png)

Fig 6. Cantidad de genes con mayor representacion entre las muestras.



5.  Tambien se graficaron los niveles de expresion de 10 de los genes que se encontraron en las 17 muestras

![](/output/expresion_genes_mas_conservados.png)

  Fig 7. Muestra los niveles de expresion de 10 genes que se encontraron en todas las muestras 



6. Por ultimo se muestran los niveles de expresion para cada uno de los genes anteriores. 

   ![](/output/expresion_gen_CAPG_17.png)

Fig 8. Se muestra la expresion de uno solo de los genes. 




### Conclusión.

Podemos concluir que el core (proteínas sobreexpresadas a través de todos los archivos) se va a reducir de manera gradual, conforme aumentamos el número de archivos analizados. Esto es contundente con estudios previos que demuestran que el cáncer es una enfermedad altamente heterogénea, por lo que a mayor número de muestras menor número de proteínas sobreexpresadas en todas ellas.

### Referencias.

+ Lawrence, R., Perez, E., Hernández, D., Miller, C., Haas, K., & Irie, H. et al. (2021). The Proteomic Landscape of Triple-Negative Breast Cancer. Retrieved 18 November 2021, from.
+ Mudvari, P., Ohshiro, K., Nair, V., Horvath, A., & Kumar, R. (2013). Genomic Insights into Triple-Negative and HER2-Positive Breast Cancers Using Isogenic Model Systems. Plos ONE, 8(9), e74993. https://doi.org/10.1371/journal.pone.0074993
+ Corrie, P. (2008). Cytotoxic chemotherapy: clinical aspects. Medicine, 36(1), 24-28. https://doi.org/10.1016/j.mpmed.2007.10.012
+ Chiu, A., Mitra, M., Boymoushakian, L., & Coller, H. (2018). Integrative analysis of the inter-tumoral heterogeneity of triple-negative breast cancer. Scientific Reports, 8(1). https://doi.org/10.1038/s41598-018-29992-5
+ Moreira, M., Brayner, F., Alves, L., Cassali, G., & Silva, L. (2019). Phenotypic, structural, and ultrastructural analysis of triple-negative breast cancer cell lines and breast cancer stem cell subpopulation. European Biophysics Journal, 48(7), 673-684. https://doi.org/10.1007/s00249-019-01393-0
+ RNA-Seq Analysis. (2021). Retrieved 6 December 2021, from https://www.strand-ngs.com/files/manual/reference/rnaseq.html
