#Limpieza base de datos
import pandas as pd
pd.set_option('display.max_columns', None)
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
import numpy as np

geolocator = Nominatim(timeout=10,user_agent="MyGeoCoder")
df = pd.read_excel(r"C:\Users\20344807257\Desktop\PERMISOS DE OBRA_2022.xlsx", engine="openpyxl")

# 1 - conveneint function to delay between geocoding calls
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
# 2- - create location column
df['adress'] = df['DIRECCION'] + ", "  + df["BARRIOS"] + ", Buenos Aires, Argentina"
df.dropna(inplace=True,subset="adress")

for i in df.index:
    print(f"{(i/len(df))*100}%")
    print(i)
    try:
        df["Latitud"].loc[i], df["Longitud"].loc[i] = (geolocator.geocode(df["adress"].loc[i]).latitude, geolocator.geocode(df["adress"].loc[i]).longitude)
    except:
        df["Latitud"].loc[i], df["Longitud"].loc[i] = np.nan, np.nan
#print(df["Latitud", "longitud"])

df.to_excel("georeferenciada.xlsx")
