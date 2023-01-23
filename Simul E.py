#Mouvement d'une particule chargée dans un champ électrostatique 
#importation des modules
from tkinter import * 
import numpy as np
import matplotlib.pyplot as plt
import math 
import numpy as np 
from math import *

#première fenêtre
first=Tk()
first.title("Simul E")
first.geometry("720x720")
first.minsize(500,500)
first.config(background='#c71910')

def opensecond():
    def electron():
        # paramètres physiques
        m= 9.11e-31 # masse de l'électron
        e=1.602176634e-19 #charge de l'electron
        q=-1*e
        x=np.arange(0,0.101,0.001)
        v0 = float(entry1.get()) 
        alpha_deg = float(entry2.get()) 
        E = float(entry3.get()) 
        # Python calcule en radians
        alpha = alpha_deg * np.pi / 180.0
        
        y=((q*E*x**2)/(2*m*(v0*np.cos(alpha))**2))+x*math.tan(alpha)
        
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
    second=Tk()
    second.title("Électron")
    second.geometry("720x720")
    second.minsize(1000,400)
    second.config(background='#4198B7')
    frame1= Frame(second,bg='#4198b7')
    label_title1=Label(frame1, text="Entrez la vitesse initiale comprise entre 1e7 et 3e7(en mètres/secondes):", font=("Arial",20),bg='#4198b7',fg='white')
    label_title1.pack()
    entry1=Entry(frame1 )
    entry1.pack()
    label_title2=Label(frame1, text="Entrez la valeur de l'angle de tir avec le plan horizontale(en degrés):", font=("Arial",20),bg='#4198b7',fg='white')
    label_title2.pack()
    entry2=Entry(frame1)
    entry2.pack()
    label_title3=Label(frame1, text="Entrez la valeur du champ E comprise entre 1e4 et 3e4:", font=("Arial",20),bg='#4198b7',fg='white')
    label_title3.pack()
    entry3=Entry(frame1)
    entry3.pack()
    b4_button=Button(frame1,text="Validez", font=("Arial",20), bg='white',command=electron)
    b4_button.pack(pady=20,fill=X)
    frame1.pack(expand=YES)
    second.mainloop()

def opentrois():
    def proton():
        # paramètres physiques
        m= 1.67e-27 # masse du proton
        e=1.602176634e-19 #charge de l'electron
        q=e
        x=np.arange(0,0.101,0.001)
        v0 = float(entry4.get()) 
        alpha_deg = float(entry5.get()) 
        E = float(entry6.get()) 
        # Python calcule en radians
        alpha = alpha_deg * np.pi / 180.0
        
        y=((q*E*x**2)/(2*m*(v0*np.cos(alpha))**2))+x*math.tan(alpha)
        
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
        
    trois=Tk()
    trois.title("Proton")
    trois.geometry("1000x720")
    trois.minsize(400,400)
    trois.config(background='#4198B7')
    frame2= Frame(trois,bg='#4198b7')
    label_title4=Label(frame2, text="Entrez la vitesse initiale comprise entre 1e7 et 3e7(en mètres/secondes)", font=("Arial",20),bg='#4198b7',fg='white')
    label_title4.pack()
    entry4=Entry(frame2)
    entry4.pack()
    label_title5=Label(frame2, text="Entrez la valeur de l'angle de tir avec le plan horizontale(en degrés)", font=("Arial",20),bg='#4198b7',fg='white')
    label_title5.pack()
    entry5=Entry(frame2)
    entry5.pack()
    label_title6=Label(frame2, text="Entrez la valeur du champ E comprise entre 1e4 et 3e4 ", font=("Arial",20),bg='#4198b7',fg='white')
    label_title6.pack()
    entry6=Entry(frame2)
    entry6.pack()
    b5_button=Button(frame2,text="Validez", font=("Arial",20), bg='white',command=proton)
    b5_button.pack(pady=20,fill=X)
    frame2.pack(expand=YES)
    trois.mainloop()
#frame
frame= Frame(first, bg='#c71910')

#texte
label_title = Label(first,text="Champ Électrostatique", font=("Arial",40), bg='#c71910', fg='white' )
label_title.pack()
label_name = Label(first,text="SIMUL E", font=("Engravers MT",70), bg='#c71910', fg='white' )
label_name.pack(pady=90)
label_subtitle = Label(frame,text="Veuillez choisir une particule", font=("Arial",30), bg='#c71910', fg='white')
label_subtitle.pack()

#button
b1_button=Button(frame,text="Électron", font=("Arial",20), bg='white',command=opensecond)
b1_button.pack(fill=X)
b2_button=Button(frame,text="Proton", font=("Arial",20), bg='white',command=opentrois)
b2_button.pack(fill=X)
frame.pack(expand=YES)
first.mainloop()
