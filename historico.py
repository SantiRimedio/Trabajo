import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\20344807257\Desktop\Obras Nuevas_4Trimestre_2022.xlsx", engine="openpyxl", sheet_name="Evolución Histórica")
df.columns = df.iloc[0]
df.dropna(inplace=True)
df = df[1:]
print(df)
x = df["Año"].astype(int)
y = df["Superficie registrada de obra nueva (m²)"].astype(int)
#plt.plot(df["Año"], df["Superficie registrada de obra nueva (m²)"])

plt.fill_between(x, y)
plt.show()