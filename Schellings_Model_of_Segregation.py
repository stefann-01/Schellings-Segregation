import numpy as np
import random as rd
import matplotlib.pyplot as plt
import os

#dimenzija_matrice=50    #ovde se menjanju parametri
#nenaseljenost=0.1
#vidno_polje=1
#tolerancija=0.5
#broj_generacija=60
#odnos=0.5

#grad=np.zeros((dimenzija_matrice,dimenzija_matrice), dtype=np.int8)

def popuni_grad(d, o, n, grad): #popunjava početnu
    for i in range(d):          #konfiguraciju grada
        for j in range(d):
            r=rd.random()
            if r>o:
                grad[i][j]=1
            else:
                grad[i][j]=2
    for p in range(int(d**2*n)): #popunjavanje praznine
        i=int(rd.randrange(0,d))
        j=int(rd.randrange(0,d))
        grad[i][j]=0

def proveri(x, y, dimenzija, matrica):         #proverava koji agent (praznina)
                                                #se nalazi na odredjenom polju
    if(not(x>=0 and y>=0 and x<dimenzija and y<dimenzija)):
        return 0,0,0
    if matrica[x][y]==0:
        return 1,0,0
    if matrica[x][y]==1:
        return 1,1,0
    if matrica[x][y]==2:
        return 1,0,1


def nadji_selice(matrica, dimenzija, vidno_polje, tolerancija):     #proverava da li je agent nezadovoljan
    selice=[]                                                       #(ili je prazno polje) i dodaje u odredjeni niz
    prazna_mesta=[]
    for i in range(dimenzija):
        for j in range(dimenzija):

            if matrica[i][j]==0:
                prazna_mesta.append((i,j))
                continue

            crnci=0
            belci=0
            mesto=0
            for r in range(i-vidno_polje, i+vidno_polje+1):
                for k in range(j-vidno_polje, j+vidno_polje+1):
                    if r==i and k==j:
                        continue
                    polje,crno,belo=proveri(r, k, dimenzija, matrica)
                    mesto+=polje
                    crnci+=crno
                    belci+=belo
            if matrica[i][j]==1 and mesto and crnci*1.0/mesto<1-tolerancija:
                selice.append((i,j))
            if matrica[i][j]==2 and mesto and belci*1.0/mesto<1-tolerancija:
                selice.append((i,j))

    return selice, prazna_mesta

def preseli(matrica, slobodno, selice):     #seli nezadovoljne agente
    while len(selice)>0:
        if len(slobodno)==0:
            break
        covek=rd.randrange(len(selice))
        mesto=rd.randrange(len(slobodno))
        matrica[slobodno[mesto]]=matrica[selice[covek]]
        matrica[selice[covek]]=0
        slobodno.remove(slobodno[mesto])
        selice.remove(selice[covek])

def iteracije(matrica, broj_generacija, dimenzija, vidno_polje, tolerancija):
    for i in range(broj_generacija):
        selice, slobodno=nadji_selice(matrica, dimenzija, vidno_polje, tolerancija)
        print(zadovoljstvo(len(selice), dimenzija, len(slobodno)))
        preseli(matrica, slobodno, selice)
        if broj_generacija % 5 == 0:   #pravi sliku stanja za svaku petu generaciju
            plt.figure()
            plt.imshow(matrica)
            plt.show()

def zadovoljstvo(selice, dimenzija, prazno):      #racuna opste zadovoljstvo
    return 1-selice*1.0/(dimenzija**2-prazno)

if __name__ == "__main__":
    popuni_grad(dimenzija_matrice, odnos, nenaseljenost, grad)
    plt.figure(1)
    plt.imshow(grad)
    plt.show()
    iteracije(grad, broj_generacija, dimenzija_matrice, vidno_polje, tolerancija)
    plt.imshow(grad)
    plt.show()