import pandas as pd
import numpy as np

import geopandas as gpd
import geopy

import matplotlib.pyplot as plt
import seaborn as sb
import calplot

peajes = pd.read_csv('./docs/Peajes en Paraguay 2018-2021 - Resumen.csv')
peajes['dia'] = peajes['dia'].astype(int)
peajes['ene'] = peajes['ene'].astype(int)
peajes['feb'] = peajes['feb'].astype(int)
peajes['mar'] = peajes['mar'].astype(int)
peajes['abr'] = peajes['abr'].astype(int)
peajes['may'] = peajes['may'].astype(int)
peajes['jun'] = peajes['jun'].astype(int)
peajes['jul'] = peajes['jul'].astype(int)
peajes['ago'] = peajes['ago'].astype(int)
peajes['sep'] = peajes['sep'].astype(int)
peajes['oct'] = peajes['oct'].astype(int)
peajes['nov'] = peajes['nov'].astype(int)
peajes['dic'] = peajes['dic'].astype(int)

dias_entre = pd.date_range(start='1/1/2018', end='31/12/2021',freq='D')


print(peajes.head())
print(peajes.shape)
print(peajes.columns)

anios = peajes['anio'].unique()
puestos = peajes['peaje'].unique()

print(anios)
print(puestos)

# events = pd.Series(np.random.randn(len(dias_entre)), index=dias_entre)
# print(events)

# ecovia = peajes.loc[peajes['peaje'] == "ecovia"]
# ecovia = ecovia.loc[ecovia['anio'] == 2021]


for puesto, _ in enumerate(puestos):

	valores = pd.Series(dtype = 'float64')
	dias_entre = pd.date_range(start='1/1/2018', end='31/12/2021',freq='D')
	puesto_peaje = peajes.loc[peajes['peaje'] == puestos[puesto]]
	for dia, _ in enumerate(dias_entre):
		dato = puesto_peaje.loc[puesto_peaje['anio'] == dias_entre[dia].year]
		dato = dato.loc[dato['dia'] == dias_entre[dia].day]
		
		# print(puestos[puesto])
		# print(dias_entre[dia])
		fecha = dias_entre[dia]
		valor = dato[dato.columns[dias_entre[dia].month+4]].values[0]
		
		valores=pd.concat([valores, pd.Series(valor)], ignore_index=True)

	
	valores.index = dias_entre
	# print(valores)
	calplot.calplot(valores, suptitle='Puesto de peaje '+puestos[puesto], cmap='GnBu',linewidth=0.3,tight_layout=False,figsize=(13,6),daylabels= ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom'],suptitle_kws={'x': 0.5, 'y': 1.0}, monthlabels= ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'])
	plt.savefig('./graph/'+puestos[puesto]+'.png', dpi=300)