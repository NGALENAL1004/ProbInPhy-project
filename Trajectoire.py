#importation des modules 
import numpy as np
import matplotlib.pyplot as plt
import math 
import numpy as np 
from math import *
# paramètres physiques
g = 9.81 # accélération de la pesanteur
hi = float(input("Entrez la hauteur initiale(en mètres):")) 
hf=  float(input("Entrez la hauteur finale(en mètres):")) 
v0 = float(input("Entrez la vitesse initiale(en mètres/secondes):")) 
alpha_deg = float(input("Entrez la valeur de l'angle de tir avec le plan horizontale(en degrés):")) 
alpha = alpha_deg * np.pi / 180.0 


# fonctions associées aux lois horaires
def x(t,g,v0,alpha):
 return v0 * math.cos(alpha) * t
def y(t,g,hi,v0,alpha):
 return hi + v0 * np.sin(alpha) * t - g *t**2 / 2

#fonction associée au mouvement
def f(d,g,v0,alpha,hi) :
    return (-g*d**2 / (2*v0**2*math.cos(alpha)**2)) + d*math.tan(alpha) +  hi

#Les données de la flêche
j=v0*np.sin(alpha)
tf=sqrt(j/g)
yf=hi + v0 * np.sin(alpha) * tf - g *tf**2 / 2

# intervalle temporel d'étude
delta1= v0**2*np.sin(alpha)**2 + 2*g*(hi-hf)
t_min = 0.0 # instant initial
t_max = (v0*np.sin(alpha)+sqrt(delta1))/g # instant final
n_t = 100 # nombre de points

# intervalle distanciel d'étude
a=math.tan(alpha)**2
b=2*g*(hi-hf)
c=math.cos(alpha)**2*v0**2
delta2= a + b/c
d_min=0
d_max=((math.tan(alpha)+sqrt(delta2))/g)*(v0**2*math.cos(alpha)**2)
n_d = 100

# tableaux
tab_t = np.linspace(t_min,t_max,n_t)
tab_d = np.linspace(d_min,d_max,n_d)
tab_x = x(tab_t,g,v0,alpha)
tab_y = y(tab_t,g,hi,v0,alpha)
tab_f = f(tab_d,g,v0,alpha,hi)

#tracée des courbes 
plt.plot(tab_d,tab_f,'r-')
plt.xlabel('Abscisse (en m)')
plt.ylabel('Ordonnée (en m)')
plt.title("Evolution de l'altitude en fonction de la distance")
plt.text(d_max/2,yf,r'La portée P =' + str(d_max) + ' mètres')
plt.text(d_max/2,yf*95/100,r'La flêche =' + str(yf) + ' mètres')

plt.show()

plt.plot(tab_t,tab_y,'r-')
plt.xlabel('Abscisse (en s)')
plt.ylabel('Ordonnée (en m)')
plt.title("Evolution de l'altitude en fonction du temps")
plt.show()

plt.plot(tab_t,tab_x,'r-')
plt.xlabel('Abscisse (en S)')
plt.ylabel('Ordonnée (en m)')
plt.title("Evolution de la distance en fonction du temps")
plt.show()
plt.plot([0,0.1],[0.05,0.05],c='#E6A32E',linewidth=3)
plt.plot([0,0.1],[-0.05,-0.05],c='#E6A32E',linewidth=3)