from os import terminal_size
import tkinter as tk
import random
from playsound import playsound
import time
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process

global mixed1

division = 0 
mixed1 = 0

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

    if Psubdivision == 1:
        Psubdivision = 4
    elif Psubdivision == 4:
        Psubdivision = 1

    return clave, Psubdivision

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

filler = []
filler = crearRelleno(claveF, division)
labelRelleno = filler

def TerceraLista(relleno):
    contador = 0
    lista = []
    for i in relleno:
        if contador == 0:
            lista.append(1)
            contador += 1
        elif contador == 3:
            lista.append(0)
            contador = 0
        else:
            lista.append(0)
            contador += 1
    
    return lista

Instrumento3 = TerceraLista(filler)

def soundCreator():
    audio2 = AudioSegment.from_file('sound6.wav') 
    audio3 = AudioSegment.from_file('sound7.wav') 

    mixed1  = audio2.overlay(audio3)          
    mixed1.export("mixed1.wav", format='wav') #export mixed  audio file      

soundCreator()             

def Run(relleno, Primertiempo):
    contador = 0
    for i in relleno:
        if i == 0:
            print("sound 1")
            playsound('sound5.wav')
        elif i == 1:
            playsound('sound6.wav')
            print("sound 2")
        if contador == 0:
            playsound('mixed1.wav')  
            print("sound 3")
            contador = 0
        contador += 1            

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

button = tk.Button(r, text='play', width=25, command=lambda: Run(filler, division))
button.config(bg='lightgreen')
button.pack()

r.mainloop()