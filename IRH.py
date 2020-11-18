import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

excel = 'Datos_Diarios.xlsx'


df = pd.read_excel(excel,sheet_name='QL_1',index_col=0)


estaciones = df.columns

#curva duracion de caudales

Ql = df[estaciones [1]] # seleciona cualquier estacion
Ql = Ql.dropna()
n = np.size(Ql)

# m / n +1
m = np.arange(1.0, n + 1.0)
f = (m * 100) / (n + 1)
output = pd.DataFrame(columns=['%Excedencia', 'Q(m3/s)'])
q_or = Ql.sort_values(axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
plt.stackplot(f, q_or,color='silver',colors=[(0.75,0.75,0.75,1)])
plt.plot(f, q_or, linewidth=2.0, linestyle='-', color='dimgray')
plt.grid(True)
plt.show()

q_prom = Ql.mean()
a = np.where(Ql <= q_prom, Ql, 0)
vp_a = sum(a)
b = np.where(Ql > q_prom, q_prom, 0)
vp_b = sum(b)
Vp = vp_a + vp_b
Vt = sum(Ql)
IRH = Vp / Vt

print(q_or)
print('Indice de regulación hídrica es')
print(IRH)