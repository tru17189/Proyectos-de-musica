import random
from winsound import Beep, PlaySound, SND_FILENAME
import time
import multiprocessing

division = 0 

def Metrica():
    mylist = [3, 4, 5, 6, 7]
    numerador = random.choice(mylist)
    denominador = 4
    Metrica_final = str(numerador) + "/" + str(denominador)
    return Metrica_final, numerador, denominador

r, numerador, denominador = Metrica()
print(r) 

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
print("Clave: %s" %claveF)

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
            if i == 0:
                pass
            elif i == 1:
                PlaySound('sound7.wav', SND_FILENAME)
    
    print(lista)

def SegundaLista(relleno):        
        for i in relleno:
            if i == 0:
                PlaySound('sound5.wav', SND_FILENAME)
            elif i == 1:
                PlaySound('sound4.wav', SND_FILENAME)
        print(relleno)

def TerceraLista(relleno):        
        for i in relleno:
            if i == 0:
                pass
            elif i == 1:
                PlaySound('sound4.wav', SND_FILENAME)
        print(relleno)

processes = []
for x in range(2):
    p2 = multiprocessing.Process(target=SegundaLista(ClaveConRelleno),args=[1])
    p1 = multiprocessing.Process(target=PrimeraLista(ClaveConRelleno, division),args=[1])
    if __name__ == "__main__":
        #p2.start()
        processes.append(p2.start())
        #p1.start()
        processes.append(p1.start())

for p in processes:
    p.join()