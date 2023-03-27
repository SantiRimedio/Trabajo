import pandas as pd
import matplotlib.pyplot as plt




df_2012_2022_limpia = pd.read_excel(r"C:\Users\20344807257\Desktop\base_2012_2022_limpia.xlsx")
df_2012_2022_limpia['TIPO_OBRA'] = df_2012_2022_limpia['TIPO_OBRA'].astype(str)

df_2021 = df_2012_2022_limpia[df_2012_2022_limpia["ANIO"] == 2021]
df_2022 = df_2012_2022_limpia[df_2012_2022_limpia["ANIO"] == 2022]

print(df_2021["TIPO_OBRA"].value_counts())
print(df_2021["BARRIOS"].value_counts())
print(df_2022["TIPO_OBRA"].value_counts())
print(df_2022["BARRIOS"].value_counts())
print(df_2012_2022_limpia["ANIO"])

#print(df_2012_2022_limpia[df_2012_2022_limpia["ANIO"] == 2022])
plt.bar(["2021","2022"],[1230,1769], color="#29BDEF")
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
#plt.savefig("barrasazul.png", transparent=True)
