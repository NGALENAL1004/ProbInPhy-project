#Mouvement d'une particule chargée dans un champ électrostatique 
#importation des modules 
import numpy as np
import matplotlib.pyplot as plt
import math 
import numpy as np 
from math import *


# paramètres physiques
m_e = 9.11e-31 # masse de l'électron
m_p = 1.67e-27 # masse du proton
e=1.602176634e-19 #charge de l'electron
x=np.arange(0,0.101,0.001)

ep=int(input("veillez faire un choix: \n1-Electron \n2-Proton \n"))
if ep==1:
    print("Votre particule est un électron")
    q=-1*e
    m=m_e
elif ep==2:
    print("Votre particule est un proton")
    q=e
    m=m_p
else:
    print("Vous avez fait un choix incorrecte")
    
v0 = float(input("Entrez la vitesse initiale comprise entre 1e7 et 3e7(en mètres/secondes):")) 
alpha_deg = float(input("Entrez la valeur de l'angle de tir avec le plan horizontale(en degrés):")) 
E = float(input("Entrez la valeur du champ E comprise entre 1e4 et 3e4:")) 
# Python calcule en radians
alpha = alpha_deg * np.pi / 180.0

y=(q*E*x**2)/(2*m*(v0*np.cos(alpha))**2)

#les axes
plt.figure(figsize=(12,8))
plt.axhline(0,c='k'); plt.axvline(0,c='k');
plt.text(-0.005,0.005,'0',color='k',fontsize=16)
plt.text(0.095,-0.005,'x',color='k',fontsize=16)
plt.text(-0.006,0.047,'y',color='k',fontsize=16)
#axes du condensateurs
plt.arrow(0,0,0.02,0,color='k',width=7e-4,head_width=3e-3,length_includes_head=True)
plt.text(0.013,-0.012,'$\overrightarrow(i)$',color='k',fontsize=16)
plt.arrow(0,0,0,0.02,color='k',width=7e-4,head_width=3e-3,length_includes_head=True)
plt.text(-0.008,0.01,'$\overrightarrow(j)$',color='k',fontsize=16)
#lignes du condensateur
plt.plot([0,0.1],[0.05,0.05],c='#E6A32E',linewidth=3)
plt.plot([0,0.1],[-0.05,-0.05],c='#E6A32E',linewidth=3)
#les signes du condensateurs 
for i in range(int(x.shape[0]/10)-1):
    plt.text(x[::10][i+1],0.0465,'-',color="#E6A32E",fontsize=25)
    plt.text(x[::10][i+1],-0.0465,'+',color="#E6A32E",fontsize=15)    
#tracer de la trajectoire     
plt.plot(x,y,'b')
#tracer de E
plt.quiver(x[-30],0,0,E,color='g',scale=1e5,width=0.005)
plt.text(x[-30]+0.003,0.005,'$\overrightarrow(E)$',color='g',fontsize=16)
#Tracer de Vo
plt.quiver(0,0,v0*math.cos(alpha),v0*np.sin(alpha),color='r',scale=1.5e58,width=0.005)
plt.text(0.004,0.01,'$\overrightarrow(v_0)$',color='r',fontsize=16)
#paramètrs de la courbe
plt.grid(True)
plt.ylim([-0.0503,0.0505])
plt.xlim([-0.02,0.102])
plt.show()