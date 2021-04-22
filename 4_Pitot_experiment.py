# -*- coding: utf-8 -*-
"""
TAREFA 8 - LCT - Experimento Tubo de Pitot - Escoamento de Ar em um Cano
Created on on Tue Apr  5 18:31:31 2021
@author: lucas Manassés Pinheiro de Souza - 16200572
"""

#%%
# imports
import matplotlib.pyplot as plt
import numpy as np
import math as ma
import pandas as pd

#%%
# Dados calculados no Excel, Tabelas
dataset = pd.read_excel('G:\LCT\dados_tarefa_8.xlsx', sheet_name='Planilha2')

#%% Fig 1: V (velocidade Não normalizada) x r* (raio normalzado)
fig, axes = plt.subplots(1, 1, figsize=(17/2.54,12/2.54))
plt.rcParams.update({'font.size': 12})
ax = axes

ax.plot(dataset['Velocidade, V [m/s], sem Redutor'],dataset['r* = r/R, sem Redutor'],'b-o',label='Sem Redutor')

ax.plot(dataset['Velocidade, V [m/s], com Redutor'],dataset['r* = r/R, com Redutor'],'r-o',label='Com Redutor')

ax.set_xlabel('Velocidade, V [m/s]')
ax.set_ylabel('r* [r/R]')
ax.grid()

fig.legend(loc='upper right', bbox_to_anchor=(0.45, 0.35),fancybox=True, shadow=False, ncol=1)
ax.set_title('Curva da Velocidade Com e Sem Redutor\n')
#fig.suptitle('Perfil de Velocidades do Ar em Escoamento Laminar e Turbulento')
fig.tight_layout()
plt.show()
fig.savefig(r"G:\LCT\plot_LCT_Tarefa_8_Fig-1.jpeg",dpi=300, bbox_inches='tight')

#%% Fig 2: V* (velocidade normalizada) x r* (raio normalzado)

fig, axes = plt.subplots(1, 1, figsize=(17/2.54,12/2.54))
plt.rcParams.update({'font.size': 12})
ax = axes

ax.plot(dataset['V* = V/Vo, sem Redutor'],dataset['r* = r/R, sem Redutor'],'b-o',label='Sem Redutor')

ax.plot(dataset['V* = V/Vo, com Redutor'],dataset['r* = r/R, com Redutor'],'r-o',label='Com Redutor')

ax.set_xlabel('V* [V/Vo]')
ax.set_ylabel('r* [r/R]')
ax.grid()

fig.legend(loc='upper right', bbox_to_anchor=(0.45, 0.34),fancybox=True, shadow=False, ncol=1)
ax.set_title('Curva da Velocidade Normalizada Com e Sem Redutor\n')
fig.tight_layout()
plt.show()
fig.savefig(r"G:\LCT\plot_LCT_Tarefa_8_Fig-2.jpeg",dpi=300, bbox_inches='tight')

#%% Cálculo de Reynolds + Velocidade média Vm
# Parâmetros do experimento 
ro_ar = 1.2        # [kg/m³]
u_ar = 1.8*1e-5   # [Ns/m²] [Ps] viscosidade absoluta ou dinâmica
R = 35.9          # [mm] raio do tubo do experimento
D = 2*R           # [mm] diâmetro do tubo 
D = D*1e-3        # [m] diâmetro do tubo

Vo_sem_red = max(dataset['Velocidade, V [m/s], sem Redutor']) # [m/s] velocidade máxima no perfil do escoamento
Vo_com_red = max(dataset['Velocidade, V [m/s], com Redutor'])


# Cálculo - Reynolds
# calcular vazao e dividir pela área
At = (ma.pi/4)*(D**2) # [m²] área da seção transversal do tubo

# Método de Gauss para o Cálculo de Vm

Vm_sem_red = sum(dataset['Velocidade, V [m/s], sem Redutor']*dataset['Wi, Gauss']) # [m/s] velocidade média pelo Método de Gauss
Vm_com_red = sum(dataset['Velocidade, V [m/s], com Redutor']*dataset['Wi, Gauss']) # [m/s] velocidade média pelo Método de Gauss


Re_sem_red = (ro_ar*Vm_sem_red*D)/u_ar
Re_sem_red = round(Re_sem_red,2)
Re_com_red = (ro_ar*Vm_com_red*D)/u_ar
Re_com_red = round(Re_com_red,2)

Qt_sem_red =  Vm_sem_red*At
Qt_sem_red =  round(Qt_sem_red,2)
Qt_com_red =  Vm_com_red*At
Qt_com_red =  round(Qt_com_red,2)



#%% Fig 3 V* (velocidade normalizada) x r* (raio normalzado) SEM REDUÇÃO + curva teórica tarefa 6 

fig, axes = plt.subplots(1, 1, figsize=(16/2.54,12/2.54))
plt.rcParams.update({'font.size': 12})
ax = axes

ax.plot(dataset['V* = V/Vo, sem Redutor'],dataset['r* = r/R, sem Redutor'],'b-o',label=f'Curva Experimental - Sem Redutor, Re = {Re_sem_red} >> 2300')


r = np.arange(-R,R,0.1)
r_estrela = r/R 
V_lam_estrela = 1 - (r_estrela**2)
ax.plot(V_lam_estrela,r_estrela,'c-',label=f'Curva Teórica - Regime Laminar com Re < 2300')

# curva 2 - esc. turbulento - Fig 5 da Terefa
r = np.arange(0,R,0.01)
r_estrela = r/R
# Fórmula da Fig 1
V_tur_estrela = ((1-r_estrela)**(1/7))
ax.plot(V_tur_estrela,r_estrela,'m-',label=f'Curva Teórica - Regime Turbulento com Re > 2300')
ax.plot(V_tur_estrela,-r_estrela,'m-')
# Para efeitos de Plotagem
x_V_tur_estrela = np.arange(0,0.35,0.1)
y_r_tur_estrela = np.empty(len(x_V_tur_estrela))
y_r_tur_estrela.fill(-R/R)
ax.plot(x_V_tur_estrela,y_r_tur_estrela,'m--')
y_r_tur_estrela.fill(R/R)
ax.plot(x_V_tur_estrela,y_r_tur_estrela,'m--')


ax.set_xlabel('V* [V/Vo]')
ax.set_ylabel('r* [r/R]')
ax.grid()

ax.text(0.25,0., r'$Q_{T} = V_{médio }$ x $A_{T} = %.2f $ m³/s'%Qt_sem_red, c='blue',bbox=dict(facecolor='white'))


fig.legend(loc='upper left', bbox_to_anchor=(0.07, 0.03),fancybox=True, shadow=False, ncol=1)
ax.set_title('Comparação Curva Teórica x Experimental - Sem Redutor\n')
fig.tight_layout()
plt.show()
fig.savefig(r"G:\LCT\plot_LCT_Tarefa_8_Fig-3.jpeg",dpi=300, bbox_inches='tight')



#%% Fig 4 V* (velocidade normalizada) x r* (raio normalzado) COM REDUÇÃO + curva teórica tarefa 6 

fig, axes = plt.subplots(1, 1, figsize=(16/2.54,12/2.54))
plt.rcParams.update({'font.size': 12})
ax = axes

ax.plot(dataset['V* = V/Vo, com Redutor'],dataset['r* = r/R, com Redutor'],'r-o',label=f'Curva Experimental - Com Redutor, Re = {Re_com_red} >> 2300')


r = np.arange(-R,R,0.1)
r_estrela = r/R 
V_lam_estrela = 1 - (r_estrela**2)
ax.plot(V_lam_estrela,r_estrela,'c-',label=f'Curva Teórica - Regime Laminar com Re < 2300')

# curva 2 - esc. turbulento - Fig 5 da Terefa
r = np.arange(0,R,0.01)
r_estrela = r/R
# Fórmula da Fig 1
V_tur_estrela = ((1-r_estrela)**(1/7))
ax.plot(V_tur_estrela,r_estrela,'m-',label=f'Curva Teórica - Regime Turbulento com Re > 2300')
ax.plot(V_tur_estrela,-r_estrela,'m-')
# Para efeitos de Plotagem
x_V_tur_estrela = np.arange(0,0.35,0.1)
y_r_tur_estrela = np.empty(len(x_V_tur_estrela))
y_r_tur_estrela.fill(-R/R)
ax.plot(x_V_tur_estrela,y_r_tur_estrela,'m--')
y_r_tur_estrela.fill(R/R)
ax.plot(x_V_tur_estrela,y_r_tur_estrela,'m--')


ax.set_xlabel('V* [V/Vo]')
ax.set_ylabel('r* [r/R]')
ax.grid()

ax.text(0.25,0., r'$Q_{T} = V_{médio }$ x $A_{T} = %.2f $ m³/s'%Qt_com_red, c='red',bbox=dict(facecolor='white'))
#ax.text(0.58,0.1, f'{Qt_com_red} m³/s', c='red')


fig.legend(loc='upper left', bbox_to_anchor=(0.07, 0.03),fancybox=True, shadow=False, ncol=1)
ax.set_title('Comparação Curva Teórica x Experimental - Com Redutor\n')
fig.tight_layout()
plt.show()
fig.savefig(r"G:\LCT\plot_LCT_Tarefa_8_Fig-4.jpeg",dpi=300, bbox_inches='tight')

#%%
