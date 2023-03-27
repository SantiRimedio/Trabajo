import pandas as pd

df_2022 = pd.read_excel(r"C:\Users\20344807257\Desktop\base_georeferenciada.xlsx", engine="openpyxl")
df_2012_2021 = pd.read_excel(r"C:\Users\20344807257\Desktop\base_limpia_2012_2021.xlsx", engine="openpyxl")

df_2012_2022_limpia = pd.concat([df_2022,df_2012_2021])
df_2012_2022_limpia['TIPO_OBRA'] = df_2012_2022_limpia['TIPO_OBRA'].astype(str)
df_2012_2022_limpia.to_excel("base_2012_2022_limpia.xlsx")