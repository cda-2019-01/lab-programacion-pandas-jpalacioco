##
# Imprima el promedio de la _c2 por cada letra de la _c1
# de la tabla tbl0
##

import pandas as pd
table = pd.read_csv("tbl0.tsv", sep='\t')
frecuencia = table['_c1'].value_counts()
print(table.groupby('_c1')['_c2'].sum()/frecuencia)
