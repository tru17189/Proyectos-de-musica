import tkinter as tk
import random
from winsound import Beep, PlaySound, SND_FILENAME
import time
import os

division = 0 

def Metrica():
    mylist = [3, 4, 5, 6, 7]
    numerador = random.choice(mylist)
    denominador = 4
    Metrica_final = str(numerador) + "/" + str(denominador)
    return Metrica_final, numerador, denominador

r, numerador, denominador = Metrica()
labelritmo = r
#print(r) 

def Clave(numerador, denominador):
    clave = []
    subdivision = [1, 2, 4]
    Psubdivision = random.choice(subdivision)
    semicorcheas = numerador * Psubdivision

    while semicorcheas > 0:
        posibles_opciones = [2, 3]
        opcion_elegida = random.choice(posibles_opciones)
        semicorcheas -= opcion_elegida
        if semicorcheas < 0:
            semicorcheas += opcion_elegida
            semicorcheas = numerador * Psubdivision
            clave = []
        else:
            clave.append(opcion_elegida)
    
    return clave, denominador

claveF, division = Clave(numerador, denominador)
labelClave = claveF
#print("Clave: %s" %claveF)

def crearRelleno(clave, division):
    relleno = []
    for i in clave:
        relleno.append(0)
        i = i * (division)
        i -= 1
        while i != 0:
            relleno.append(1)
            i -= 1
    
    return relleno

ClaveConRelleno = []
ClaveConRelleno = crearRelleno(claveF, division)
labelRelleno = ClaveConRelleno

#print(ClaveConRelleno)

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

def TerceraLista(relleno):      
        for i in relleno:
            try:
                i = int(i)
            except:
                pass

            if i == 0:
                time.sleep(0.1)
                print("yeah")
            elif i == 1:
                PlaySound('sound4.wav', SND_FILENAME)
                time.sleep(0.3)

r = tk.Tk()
r.title('Generador de ritmos')

ourMessage ='Metrica: %s' % labelritmo
messageVar = tk.Message(r, width=160, text = ourMessage)
messageVar.config(bg='blue')
messageVar.pack( )

ourMessage2 ='clave: %s' % labelClave
messageVar2 = tk.Message(r, width=160, text = ourMessage2)
messageVar2.config(bg='lightblue')
messageVar2.pack( )

ourMessage3 ='clave con relleno: %s' % labelRelleno
messageVar3 = tk.Message(r, width=300, text = ourMessage3)
messageVar3.config(bg='blue')
messageVar3.pack( )

button = tk.Button(r, text='play', width=25, command=lambda: [PrimeraLista(ClaveConRelleno, division), TerceraLista(ClaveConRelleno)])
button.config(bg='lightgreen')
button.pack()

button2 = tk.Button(r, text='Stop', width=25, command=r.destroy)
button2.config(bg='red')
button2.pack()
r.mainloop()