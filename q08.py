##
# Agregue el año como una columna a la tabla tbl0.tsv
##

import pandas as pd
table = pd.read_csv("tbl0.tsv", sep='\t')
table["ano"] = table["_c3"].str.split("-").map(lambda x: x[0])
print(table)
