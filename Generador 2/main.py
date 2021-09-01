import random
from winsound import Beep, PlaySound, SND_FILENAME
import time
import os
import multiprocessing

division = 0 

def Metrica():
    mylist = [3, 4, 5, 6, 7]
    numerador = random.choice(mylist)
    denominador = 4
    Metrica_final = str(numerador) + "/" + str(denominador)
    return Metrica_final, numerador, denominador

r, numerador, denominador = Metrica()
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

#print(ClaveConRelleno)

archivo1= "%s" % ClaveConRelleno
f = open('relleno.txt','w')
f.write(archivo1)
f.close()

archivo1= str(division)
f = open('division.txt','w')
f.write(archivo1)
f.close()

p1 = multiprocessing.Process(target=os.system("py PrimerInstrumento.py"))
p2 = multiprocessing.Process(target=os.system("py SegundoInstrumento.py"))
p3 = multiprocessing.Process(target=os.system("py TerceroInstrumento.py"))

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()
#SegundaLista(ClaveConRelleno)