import numpy as np
import random as rd
import matplotlib.pyplot as plt
import os
import statistics

from Selingov_model_segregacije import popuni_grad, nadji_selice, preseli, zadovoljstvo

def crtaj_grafik_veliki(zadovoljstvo,promenljiva,put,ime,broj_iteracija,greske):      #crta grafik
                                                                                    #zadovoljstva od promenljive
    fig=plt.figure()
    plt.xlabel(ime)
    plt.ylabel("Задовољство агената након " + str(broj_iteracija) + " генерација [%]")
    plt.errorbar(promenljiva,zadovoljstvo,greske)
    plt.plot(promenljiva,zadovoljstvo,'ro',promenljiva,zadovoljstvo)
    plt.grid(True)
    plt.title("Зависност задовољста агената од ненасељености")
    fig.savefig(put+'/Zadovoljstvo_od_nenaseljenosti.png')

    
    
def variranje(broj_ponavljanja, broj_tacaka, broj_generacija, dimenzija_matrice, odnos, nenaseljenost, vidno_polje, grad, tolerancija):
    put="D:/Stari Desktop/Selingov model/Nenaseljenost/"
    promenljiva=[]
    standardna_devijacija=[]
    srednja_vrednost=[] #aritmeticka sredina zadovoljstva po koracima

    for i in range(broj_tacaka):    #varira promenljivu
        nenaseljenost=0.05+0.05*i
        nenaseljenost=round(nenaseljenost,2)
        putt=put+str(nenaseljenost)
        if not os.path.exists(putt):    #pravi foldere za slike
            os.makedirs(putt)

        zadovoljstvo_po_pokusaju=[] #cuva krajnje zadovljstvo za svaku simulaciju
        
        for j in range(broj_ponavljanja):   #ponavlja simulaciju sa istim parametrom
            put_pokusaj=putt+'/'+str(j)
            if not os.path.exists(put_pokusaj):  #pravi folder za ponavljanja
                os.makedirs(put_pokusaj)

            #grad=np.zeros((dimenzija_matrice,dimenzija_matrice), dtype=np.int8) #za variranje dimenzija
            popuni_grad(dimenzija_matrice, odnos, nenaseljenost, grad)

            for generacija in range(broj_generacija):   #iterira simulaciju

                selice, prazno = nadji_selice(grad, dimenzija_matrice, vidno_polje, tolerancija)
                duzina = len(selice)
                prazno_duzina = len(prazno)
                preseli(grad, prazno, selice)

                if generacija %50==0:   #cuva svaku 50. sliku
                    put_slike=put_pokusaj+'/'+str(generacija)+".png"
                    fig=plt.figure()
                    plt.imshow(grad)
                    fig.savefig(put_slike)
                
            zadovoljstvo_po_pokusaju.append(float(zadovoljstvo(duzina, dimenzija_matrice, prazno_duzina))) #zadovoljstvo za kraju svake pojedinacne simulacije
                
        srednja_vrednost.append(np.mean(zadovoljstvo_po_pokusaju)*100)     #upisuje srednja vrednost od 3 pokusaja
        standardna_devijacija.append(statistics.stdev(zadovoljstvo_po_pokusaju)*100)    #upisuje gresku
        promenljiva.append(nenaseljenost*100)   #cuva vrednosti promenljive
    crtaj_grafik_veliki(srednja_vrednost,promenljiva,put,"Ненасељеност",broj_generacija,standardna_devijacija)

if __name__ == "__main__":
    dimenzija_matrice=50
    nenaseljenost=0.10
    vidno_polje=1
    tolerancija=0.5
    broj_generacija=101
    odnos=0.5
    broj_ponavljanja=3
    broj_tacaka=10   #broj koraka

    grad=np.zeros((dimenzija_matrice,dimenzija_matrice), dtype=np.int8)
    variranje(broj_ponavljanja,broj_tacaka,broj_generacija,dimenzija_matrice,odnos,nenaseljenost,vidno_polje,grad,tolerancija)