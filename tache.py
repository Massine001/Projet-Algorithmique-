import numpy as np 

def tri(g,d):                                 #####  Fonction qui tri un tableau du plus grand au plus petit élément  ####
    for i in range(1, len(g)):
        position = i
        element= g[i]
        date=d[i]

        while position>0 and element > g[position-1]:
            g[position]=g[position-1]
            d[position]=d[position-1]           #####pour trier aussi le vecteur des echéances d 
            position =position-1
        g[position]=element
        d[position]=date
    return g,d

def sum_gain(v):                               ###### Fonction qui calcule la somme des élément d'un tableau #####
    s=0
    for i in range(len(v)):
        s=s+v[i]
        
    return s

def max(d):                         ########  Fonction qui calcule le max d'un vecteur donnée 
    dmax=0
    for i in range(len(d)):              
        if d[i]>dmax :
            dmax=int(d[i])
    return dmax


                        
                               
def creneau_opt(dmax,g,d):        ################## 4eme étape: chercher un craneau optimal pour chaque tache i
    #tmp=np.zeros(dmax)                #initialisé un tableau de taille dmax à zero
    tmp=[0]*dmax
    creneau = np.full(int(dmax),True) 
    for i in range(len(g)):     
        k=int(d[i])
        
        while (k >= 1):
            
            if creneau[k-1]== True:              # tester si le créneau est disponible 
                creneau[k-1] = False                # si la condition est remplis donc le créneau sera non disponible pour les prochaine taches
                tmp[k-1]=g[i]                       # sauvegarder les valeur de gain dans le tableau tmp
                break                               #sortir de la boucle while (puisque on à trouver le créneau optimal pour la tache i)
            k=k-1
    return tmp       
      

######################################################### PROGRAMME PRINCIPAL MAIN ############################################################""""
#n=5
#d=[2,1,2,1,3]
#g=[100,19,27,25,15]

n=int (input("donnez le nombre de taches=="))

d=np.zeros(n)
g=np.zeros(n)
for i in range(n):
    d[i]=int (input("donnez la date limite d[i] de chaque tache")) #### initialiser le vecteur des dates limite  à zero

for i in range(n):
    g[i]=int (input("donnez le gain chaque tache"))                ####initialiser le vecteur des gains  à  zero



print(g)   
tri(g,d)                     #########################  1er étape: appel à la fonction de tri ####################
print("le vecteur des gain trié",g)
print("le vecteur dates d[i] trié",d)


dmax=max(d)                   ##################### 2eme étape appel à la fonction max  ###########

#print("max=",dmax)  

#
l=creneau_opt(dmax,g,d)

print("gain==",sum_gain(l))
    
