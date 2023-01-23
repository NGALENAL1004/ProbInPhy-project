#importation des modules python
from tkinter import *
import numpy as np 
import matplotlib.pyplot as plt
from math import *
import math


#première fenêtre
first=Tk()
first.title("Simular")
first.geometry("720x720")
first.minsize(500,500)
#first.iconbitmap("logo.ico")
first.config(background='#41B77F')
def opensecond():
    def chutelibre():
        g = 9.81 # accélération de la pesanteur
        h=float(entry1.get())
        b=float(entry2.get())
       
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
            
    second=Tk()
    second.title("chute libre")
    second.geometry("720x720")
    second.minsize(400,400)
    #second.iconbitmap("logo.ico")
    second.config(background='#4198B7')
    frame1= Frame(second,bg='#4198b7')
    label_title1=Label(frame1, text="Entrez la hauteur initiale(en mètres)", font=("Arial",20),bg='#4198b7',fg='white')
    label_title1.pack()
    entry1=Entry(frame1 )
    entry1.pack()
    label_title2=Label(frame1, text="Entrez la hauteur finale(en mètres)", font=("Arial",20),bg='#4198b7',fg='white')
    label_title2.pack()
    entry2=Entry(frame1)
    entry2.pack()
    b4_button=Button(frame1,text="Validez", font=("Arial",20), bg='white',command=chutelibre)
    b4_button.pack(pady=20,fill=X)
    frame1.pack(expand=YES)
    second.mainloop()
    
def opentrois():
    def Frottements():
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
        m=float(entry3.get()) 
        lamb=float(entry4.get())# coef. de frottement
        tau = m / lamb
        v0 = 0.0 # vitesse initiale
        h=float(entry5.get()) 
        t_min = 0.0 # instant initial
        t_max = h * tau # instant final
        n_t = 100
        tab_t = np.linspace(t_min,t_max,n_t)
        tab_v = eulerExp(t_min,t_max,n_t,g,h,v0,tau)
        plt.plot(tab_t,tab_v,'r-',label="h = " + str(h) + " m")
        plt.xlabel('Temps (en s)')
        plt.ylabel('Vitesse de $M$ (en m/s)')
        plt.title("Chute libre avec frottements fluides et sans vitesse initiale")
        plt.text(t_max*5/100,10.0,r'$h = ' + str(h) + '$ m')
        plt.text(t_max*20/100,5.0,r'$t_{max} = ' + str(t_max) + '$ s')
        plt.text(t_max*55/100,15.0,r'$m = ' + str(m) +'$ kg')
        plt.text(t_max*80/100,20.0,r'$\lambda = ' +str(lamb) + '$ kg/s')# h = 10.0 # hauteur initiale
        plt.show()
       
    trois=Tk()
    trois.title("frottements")
    trois.geometry("720x720")
    trois.minsize(400,400)
    #trois.iconbitmap("logo.ico")
    trois.config(background='#4198B7')
    frame2= Frame(trois,bg='#4198b7')
    label_title3=Label(frame2, text="Entrez la masse de la particule (en Kilogrammes)", font=("Arial",20),bg='#4198b7',fg='white')
    label_title3.pack()
    entry3=Entry(frame2)
    entry3.pack()
    label_title4=Label(frame2, text="Entrez le coefficient de frottements (<1)", font=("Arial",20),bg='#4198b7',fg='white')
    label_title4.pack()
    entry4=Entry(frame2)
    entry4.pack()
    label_title5=Label(frame2, text="Entrez la hauteur initiale(en mètres) ", font=("Arial",20),bg='#4198b7',fg='white')
    label_title5.pack()
    entry5=Entry(frame2)
    entry5.pack()
    b5_button=Button(frame2,text="Validez", font=("Arial",20), bg='white',command=Frottements)
    b5_button.pack(pady=20,fill=X)
    frame2.pack(expand=YES)
    trois.mainloop()

def openquatre():
    def Trajectoire():
        # paramètres physiques
        g = 9.81 # accélération de la pesanteur
        hi = float(entry6.get()) 
        hf=  float(entry7.get())
        v0 = float(entry8.get()) 
        alpha_deg = float(entry9.get()) 
        
        
        # Python calcule en radians
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
        plt.text(d_max/2,yf*90/100,r'La portée P =' + str(d_max) + ' mètres')
        plt.text(d_max/2,yf*95/100,r'La flêche =' + str(yf) + ' mètres')
        plt.show()
        
        plt.plot(tab_t,tab_y,'r-')
        plt.xlabel('Abscisse (en s)')
        plt.ylabel('Ordonnée (en m)')
        plt.title("Evolution de l'altitude en fonction du temps")
        plt.text(d_max/2,yf*80/100,r'$La portée =$' + str(yf) + ' mètres')
        plt.text(d_max/2,yf*92/100,r'$t_{max} =$'+str(t_max)+'secondes')
        plt.show()
        
        plt.plot(tab_t,tab_x,'b-')
        plt.xlabel('Abscisse (en S)')
        plt.ylabel('Ordonnée (en m)')
        plt.title("Evolution de la distance en fonction du temps")
        plt.show()

       
    quatre=Tk()
    quatre.title("Trajectoire")
    quatre.geometry("850x800")
    quatre.minsize(400,400)
    #quatre.iconbitmap("logo.ico")
    quatre.config(background='#4198B7')
    frame3= Frame(quatre,bg='#4198b7')
    label_title6=Label(frame3, text="Entrez la hauteur initiale(en mètres)", font=("Arial",20),bg='#4198b7',fg='white')
    label_title6.pack()
    entry6=Entry(frame3)
    entry6.pack()
    label_title7=Label(frame3, text="Entrez la hauteur finale(en mètres)", font=("Arial",20),bg='#4198b7',fg='white')
    label_title7.pack()
    entry7=Entry(frame3)
    entry7.pack()
    label_title8=Label(frame3, text="Entrez la vitesse initiale(en mètres/secondes)", font=("Arial",20),bg='#4198b7',fg='white')
    label_title8.pack()
    entry8=Entry(frame3)
    entry8.pack()
    label_title9=Label(frame3, text="Entrez la valeur de l'angle de tir avec le plan horizontale(en degrés)", font=("Arial",20),bg='#4198b7',fg='white')
    label_title9.pack()
    entry9=Entry(frame3)
    entry9.pack()
    b6_button=Button(frame3,text="Validez", font=("Arial",20), bg='white',command=Trajectoire)
    b6_button.pack(pady=20,fill=X)
    frame3.pack(expand=YES)
    quatre.mainloop()

#frame
frame= Frame(first, bg='#41B77F')

#texte
label_title = Label(first,text="Bienvenue sur Simular", font=("Arial",40), bg='#41B77F', fg='white' )
label_title.pack()
label_name = Label(first,text="SIMULAR", font=("Engravers MT",70), bg='#41B77F', fg='white' )
label_name.pack(pady=90)
label_subtitle = Label(frame,text="Veuillez faire un choix", font=("Arial",30), bg='#41B77F', fg='white')
label_subtitle.pack()

#button
b1_button=Button(frame,text="Chute libre sans vitesse initiale", font=("Arial",20), bg='white',command=opensecond)
b1_button.pack(fill=X)
b2_button=Button(frame,text="Chute libre sans vitesse initiale avec frottements", font=("Arial",20), bg='white',command=opentrois)
b2_button.pack(fill=X)
b3_button=Button(frame,text="Chute libre avec vitesse initiale", font=("Arial",20), bg='white',command=openquatre)
b3_button.pack(fill=X)
frame.pack(expand=YES)
first.mainloop()
