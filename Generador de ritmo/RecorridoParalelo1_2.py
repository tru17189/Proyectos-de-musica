import random
from winsound import Beep, PlaySound, SND_FILENAME
import time

def PrimeraLista(relleno, Primertiempo):
    contador = 0
    lista = []
    for i in relleno:
        contador += 1
        if contador == Primertiempo:
            lista.append(1)
            Primertiempo = Primertiempo * 2
        else:
            lista.append(0)
        
    for i in lista:
        try:
            i = int(i)
        except:
            pass

        if i == 0:
            PlaySound('sound4.wav', SND_FILENAME)
        elif i == 1:
            PlaySound('sound7.wav', SND_FILENAME)

ClaveConRelleno = open('relleno.txt','r')
ClaveConRelleno = ClaveConRelleno.read()
division = open('division.txt','r')
division = int(division.read())
PrimeraLista(ClaveConRelleno, division)