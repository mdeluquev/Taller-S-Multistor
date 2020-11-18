import  pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt

#Llamar los datos

pth = 'Colombia_Oferta_Demanda.shp'

df_geo = gp.GeoDataFrame.from_file(pth)
columnas=df_geo.columns

print(columnas)

# Se calcula el Índice de Escasez para el año modal
df_geo['IEMOD'] = (df_geo['Demanda']/df_geo['Oferta_Mod']*100)
df_geo['IESECO'] = (df_geo['Demanda']/df_geo['Oferta_97_']*100)


#Exportar a shp file
df_geo.to_file(r"IE_Colombia.shp")

