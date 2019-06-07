##
# Construya una tabla que contenga _c0 y una lista
# separada por ',' de los valores de la columna _c4
# de la tabla tbl1.tsv
##

import pandas as pd
table = pd.read_csv("tbl1.tsv", sep='\t')


new_df = pd.DataFrame()
new_df["_c0"] = table["_c0"].unique()
new_df["lista"] = table.groupby('_c0')['_c4'].unique().str.join(",")
print(new_df)
