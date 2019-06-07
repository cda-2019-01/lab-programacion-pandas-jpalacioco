##
# Imprima los valores unicos e la columna _c4 de
# de la tabla tbl1 en mayusculas
##


import pandas as pd
import numpy as np
table = pd.read_csv("tbl1.tsv", sep='\t')
letras = table["_c4"].str.upper().unique()
letras = list(letras)
letras.sort()
print(letras)
