# importation des modules
import numpy as np
import matplotlib.pyplot as plt

def eulerExp(t_min,t_max,n_t,g,h,v0,tau):
# création d'un tableau vide des vitesses à (n_t + 1) éléments
    tab_v = np.zeros(n_t)
# affectation de la vitesse initiale au premier élement du tableau
    tab_v[0] = v0
# calcul de delta_t
    delta_t = (t_max - t_min) / n_t
# boucle de calcul des vitesses approchées
    for i in range(n_t-1):
        tab_v[i+1] = (1 - delta_t / tau) * tab_v[i] + g * delta_t
    return tab_v
# paramètres physiques
g = 9.81 # accélération de la pesanteur
m = float(input("Entrez la masse de la particule (en Kilogrammes):")) 
lamb = float(input("Entrez le coefficient de frottements (<1) :"))# coef. de frottement
tau = m / lamb
v0 = 0.0 # vitesse initiale
h = float(input("Entrez la hauteur initiale(en mètres):")) 
t_min = 0.0 # instant initial
t_max = h * tau # instant final
n_t = 100
tab_t = np.linspace(t_min,t_max,n_t)
tab_v = eulerExp(t_min,t_max,n_t,g,h,v0,tau)
plt.plot(tab_t,tab_v,'r-',label="h = " + str(h) + " m")
plt.xlabel('Temps (en s)')
plt.ylabel('Vitesse de $M$ (en m/s)')
plt.title("Chute libre avec frottements fluides et sans vitesse initiale")
plt.text(t_max*10/100,10.0,r'$h = ' + str(h) + '$ m')
plt.text(t_max*30/100,5.0,r'$t_{max} = ' + str(t_max) + '$ s')
plt.text(t_max*55/100,15.0,r'$m = ' + str(m) +'$ kg')
plt.text(t_max*70/100,20.0,r'$\lambda = ' +str(lamb) + '$ kg/s')# h = 10.0 # hauteur initiale
plt.show()