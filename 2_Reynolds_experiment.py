# -*- coding: utf-8 -*-
"""
TAREFA 6 - LCT - Experimento de Reynolds - Escoamento de Ar a pressão atmosférica
Created on Fri Mar 26 02:27:07 2021
@author: lucas Manassés Pinheiro de Souza - 16200572
"""

#%%
# imports
import matplotlib.pyplot as plt
import numpy as np
import math as ma

#%%
# Parâmetros do experimento
p_ar = 1.2        # [kg/m³]
u_ar = 1.8*1e-5  # [Ns/m²] [Ps] viscosidade absoluta ou dinâmica
R = 35.9          # [mm] raio do tubo do experimento
D = 2*R           # [mm] diâmetro do tubo 
D = D*1e-3        # [m] diâmetro do tubo
Vo_lam = 0.5      # [m/s] velocidade máxima no perfil do escoamento laminar
Vo_tur = 15       # [m/s] velocidade máxima no perfil do escoamento turbulento

# Cálculo - Reynolds
# calcular vazao e dividir pela área
A = (ma.pi/4)*(D**2) # [m²] área da seção transversal do tubo
Vm_lam = 0.5*Vo_lam
Vm_tur = (49/60)*Vo_tur

Re_lam = (p_ar*Vm_lam*D)/u_ar
Re_lam = round(Re_lam,2)
Re_tur = (p_ar*Vm_tur*D)/u_ar
Re_tur = round(Re_tur,2)

#%%
n_rows = 1
n_cols = 2
fig, axes = plt.subplots(n_rows, n_cols, figsize=(19/2.54,12/2.54))
plt.rcParams.update({'font.size': 12})

# Primeiro Gráfico - Curvas Näo Normalizadas
ax = axes[0]
# curva 1 - esc. laminar - Fig 1 da Tarefa
r = np.arange(-R,R,0.1)
# Fórmula da Fig 1
Vr_lam = Vo_lam*(1-((r/R)**2))
ax.plot(Vr_lam,r,'b-')#,label=f'Esc. Laminar, Re={Re_lam}')
# curva 2 - esc. turbulento - Fig 4 da Terefa
r = np.arange(0,R,0.1)
# Fórmula da Fig 1
Vr_tur = Vo_tur*((1-(r/R))**(1/7))
ax.plot(Vr_tur,r,'r-')#,label=f'Esc. Turbulento, Re={Re_tur}')
ax.plot(Vr_tur,-r,'r-')
# Para efeitos de Plotagem
x_Vr_tur = np.arange(0,6.5,0.1)
y_r_tur = np.empty(len(x_Vr_tur))
y_r_tur.fill(-R)
ax.plot(x_Vr_tur,y_r_tur,'r--')
y_r_tur.fill(R)
ax.plot(x_Vr_tur,y_r_tur,'r--')
# Limites da Figura
ax.set_xlim(0,15.1)
ax.set_title('Curvas Não Normalizadas')
ax.set_xlabel('Velocidade, V [m/s]')
ax.set_ylabel('Raio, r [mm]')
ax.grid() # VERIFICAR DEPOIS
#ax.legend(loc='upper left', bbox_to_anchor=(-0.25, -0.1),fancybox=True, shadow=True, ncol=1)

# Segundo Gráfico - Curvas Normalizadas
ax = axes[1]
# curva 1 - esc. laminar - Fig 3 da Tarefa
r = np.arange(-R,R,0.1)
r_estrela = r/R # ERRO NO VÍDEO DA TAREFA; APARECE COMO r*= R/r
# Fórmula da Fig 3
V_lam_estrela = 1 - (r_estrela**2)
ax.plot(V_lam_estrela,r_estrela,'b-',label=f'Escoamento em Regime Laminar com Re = {Re_lam} < 2300')

# curva 2 - esc. turbulento - Fig 5 da Terefa
r = np.arange(0,R,0.01)
r_estrela = r/R
# Fórmula da Fig 1
V_tur_estrela = ((1-r_estrela)**(1/7))
ax.plot(V_tur_estrela,r_estrela,'r-',label=f'Escoamento em Regime Turbulento com Re = {Re_tur} > 2300')
ax.plot(V_tur_estrela,-r_estrela,'r-')

# Para efeitos de Plotagem
x_V_tur_estrela = np.arange(0,0.35,0.1)
y_r_tur_estrela = np.empty(len(x_V_tur_estrela))
y_r_tur_estrela.fill(-R/R)
ax.plot(x_V_tur_estrela,y_r_tur_estrela,'r--')
y_r_tur_estrela.fill(R/R)
ax.plot(x_V_tur_estrela,y_r_tur_estrela,'r--')
# Limites da Figura
ax.set_xlim(0,1.005)
ax.set_title('Curvas Não Normalizadas')
ax.set_xlabel('V* [V/Vo]')
ax.set_ylabel('r* [r/R]')
ax.grid()
#ax.legend(loc='upper left', bbox_to_anchor=(0., -0.1),fancybox=True, shadow=True, ncol=1)

fig.legend(loc='upper left', bbox_to_anchor=(0.09, -0.0),fancybox=True, shadow=True, ncol=1)
ax.set_title('Curvas Normalizadas')

fig.suptitle('Perfil de Velocidades do Ar em Escoamento Laminar e Turbulento')
fig.tight_layout()
plt.show()
#fig.savefig(r"G:\LCT\plot_LCT_Tarefa_6.jpeg",dpi=300, bbox_inches='tight') #En
