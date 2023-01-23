# importation des modules 
import numpy as np 
import matplotlib.pyplot as plt
from math import *
# paramètres physiques
g = 9.81 # accélération de la pesanteur
h = float(input("Entrez la hauteur initiale(en mètres):")) 
b = float(input("Entrez la hauteur finale(en mètres):"))
# fonction associée à la loi horaire
def z(t,g,h):
  return h - g * t**2 / 2
# tracé des trajectoires
t_min = 0.0 # instant initial en s
t_max = sqrt((2*(h-b))/g) # instant final en s
n_t = 100 # nombre de points de calculs
# tableau des instants
tab_t = np.linspace(t_min,t_max,n_t)
# tableau des z
tab_z = z(tab_t,g,h)
# tracé de tab_z en fonction de tab_t
# option 'r-' : tracé en rouge (r)
# en reliant les points (-)
plt.xlabel('Temps (en seconde)')
plt.ylabel('Position de $M$ (en mètre)')
plt.title("Chute libre sans frottement et sans vitesse initiale")
plt.text(t_max/2,h,r'$h =$' + str(h) + ' mètres')
plt.text(t_max/2,h*90/100,r'$t_{max} =$'+str(t_max)+'secondes')
plt.plot(tab_t,tab_z,'g-')

# affichage de la courbe
plt.show()
