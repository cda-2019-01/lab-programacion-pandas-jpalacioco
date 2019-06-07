##
# Construya una tabla que contenga _c1 y una lista
# separada por ':' de los valores de la columna _c2
# para el archivo tbl0.tsv
##


import pandas as pd
table = pd.read_csv("tbl0.tsv", sep='\t')

new_df = pd.DataFrame()
new_df["_c1"] = table["_c1"].unique()
new_df["lista"] = table.groupby('_c0')["_c2"]
print(new_df)
