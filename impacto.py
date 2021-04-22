# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:25:32 2021

@author: twi
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator,
                               FormatStrFormatter,
                               AutoMinorLocator)
import pandas as pd

#%%
dataset = pd.read_excel(r'C:\Users\twi\Desktop\LPM-2021\Relatorio5\experimento_impacto.xlsx') 
#dataset = dataset[0:20]
#dataset = dataset.iloc[:,:8]

#pd.read_excel('filename.xlsx', sheet_name = None)

#%%
fig = plt.figure(figsize=(18/2.54,10/2.54))
plt.rcParams.update({'font.size': 12})
ax = fig.add_subplot()

ax.plot(dataset.iloc[:,0],dataset.iloc[:,1],'b--', linewidth=0.25)
ax.scatter(dataset.iloc[:,0],dataset.iloc[:,1],color='black', marker='o',s=30, label='CP Falhou') 


vec_x = [dataset.iloc[11,0],dataset.iloc[11,0]]
vec_y = [-5,dataset.iloc[11,1]]
vec_y = [-5,95]
ax.plot(vec_x,vec_y,'r--', linewidth=1.7)

vec_x = [dataset.iloc[2,0],dataset.iloc[2,0]]
vec_y = [-5,dataset.iloc[2,1]]
vec_y = [-5,95]
ax.plot(vec_x,vec_y,'b--', linewidth=1.7)

plt.xlim([-180., 105.0])
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.xaxis.set_major_formatter(FormatStrFormatter('% 1.f'))
plt.ylim([20.0, 92.0])

#ax.yaxis.set_major_locator(dataset.iloc[:,0])
#ax.yaxis.set_major_formatter(FormatStrFormatter('% 1.2f'))

plt.xlabel('Temperatura, T [°C] ') 
plt.ylabel('Energia de Impacto [J]') 
#plt.ticklabel_format(axis='y', style='sci',scilimits=(-1,1))

plt.grid()
plt.tight_layout()


ax.text(-174.,50., r'Reg. Frágil', c='red',bbox=dict(facecolor='white'))
ax.text(-60.,40., r'Região Dúctil-Frágil', c='green',bbox=dict(facecolor='white'))
ax.text(56.,50., r'Reg. Dúctil', c='blue',bbox=dict(facecolor='white'))


# vec_y = [dataset.iloc[11,1],dataset.iloc[11,1]]
# vec_x = [-175,105]
# ax.plot(vec_x,vec_y,'g--', linewidth=1.7)

# vec_y = [dataset.iloc[2,1],dataset.iloc[2,1]]
# vec_x = [-175,105]
# ax.plot(vec_x,vec_y,'g--', linewidth=1.7)

vec_x = [-37.5,-37.5]
vec_y = [20,95]
ax.plot(vec_x,vec_y,'g-', linewidth=1.7)

#ax.text(-115.,78., r'TTDF = -75,75', c='green',bbox=dict(facecolor='white'))
ax.text(-50.,54., r'TTDF = -37,5', c='green',bbox=dict(facecolor='white'))


#fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.33),fancybox=True)

title = "Ensaio_Impacto_3"
fig.savefig(r"C:\Users\twi\Desktop\LPM-2021\Relatorio5\plot_"+title+".jpeg",dpi=300) #En

#plt.close();
#%%

#plt.plot(dataset.iloc[:,2], dataset.iloc[:,4],'*-')  

ax.plot(x,y,color='black', marker='o',markersize=4) 
ax.plot(x1,y1,'k--o') 
#plt.scatter(x,y,c='red') 
x_E = x[3]
y_E = y[3]
ax.scatter(x_E,y_E,color='red',marker='o',s=40)
t = 0.0003
E_text = "$P_{4}$("+str(round(x_E,3))+";"+str(round(y_E,3))+")"
ax.text(x_E+t, y_E-10, E_text, fontsize=12)

x_LE = x[5]
y_LE = y[5]
ax.scatter(x_LE,y_LE,color='red',marker='o',s=40)
t_LE = 33
LE_text = "$P_{6}$("+str(round(x_LE,3))+";"+str(round(y_LE,3))+")"
ax.text(x_LE+0.0001, y_LE-t_LE, LE_text, fontsize=12)

vec_x_temp = [x_E,x_E]
vec_y_temp = [0,y_E]

plt.plot(vec_x_temp,vec_y_temp,color='red',linestyle='dashed')

vec_x_temp = [0,x_E]
vec_y_temp = [x_E,0]
plt.plot(vec_x_temp,vec_y_temp,color='red',linestyle='dashed')


#>>> plot(x, y, color='green', marker='o', linestyle='dashed',


plt.xlim([-0.001, 0.01])
plt.xlabel('Deformação de Engenharia [mm/mm]') #En
#plt.ylim([-2, 4])
plt.ylabel('Tensão uniaxial [N/mm²]') #MPa
#plt.ylabel('Tensão uniaxial [KPa]') 


major = ['major','-','0.0001','black']
plt.grid(major)
plt.tight_layout()


title = "Tensão_x_Deformação_ampliado"
fig.savefig(r"C:\Users\twi\Desktop\LPM-2021\Relatorio1\plot_"+title+".jpeg",dpi=300) #En

plt.close();
