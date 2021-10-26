from os import terminal_size
import random
from playsound import playsound
import time
from pydub import AudioSegment
import pygame
from pygame import mixer

global mixed1

division = 0 
mixed1 = 0

# Se eligue la metrica random
def Metrica():
    mylist = [3, 4, 5, 6]
    numerador = random.choice(mylist)
    denominador = 4
    Metrica_final = str(numerador) + "/" + str(denominador)
    return Metrica_final, numerador, denominador

r, numerador, denominador = Metrica()
labelritmo = r

# Creamos los claves a partir de los resultados anteriores
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

# Rellenamos la clave para el filler 
def crearRelleno(clave, division):
    relleno = []
    for i in clave:
        relleno.append(0)
        i = i * (division)
        i -= 1
        while i != 0:
            posibles_opciones = [0, 1]
            opcion_elegida = random.choice(posibles_opciones)
            relleno.append(opcion_elegida)
            i -= 1
    return relleno

filler = []
filler = crearRelleno(claveF, division)

# Creamos la lista para el tercer instrumento
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

# Recolectamos los sonidos
mixer.init()
sonido1 = mixer.Sound('sound4.ogg') 
sonido1.set_volume(0.2)
sonido2 = mixer.Sound('sound8.ogg') 
sonido2.set_volume(0.2)
sonido3 = mixer.Sound('sound6.ogg') 
sonido3.set_volume(0.2)
sonido4 = mixer.Sound('sound7.ogg')  
sonido4.set_volume(0.2)

do = mixer.Sound('Sounds/do.ogg')
do.set_volume(1.0)
doMayor = mixer.Sound('Sounds/do#.ogg')
doMayor.set_volume(1.0)
re = mixer.Sound('Sounds/re.ogg')
re.set_volume(1.0)
reMayor = mixer.Sound('Sounds/re#.ogg')
reMayor.set_volume(1.0)
mi = mixer.Sound('Sounds/mi.ogg')
mi.set_volume(1.0)
fa = mixer.Sound('Sounds/fa.ogg')
fa.set_volume(1.0)
faMayor = mixer.Sound('Sounds/fa#.ogg')
faMayor.set_volume(1.0)
sol = mixer.Sound('Sounds/sol.ogg')
sol.set_volume(1.0)
solMayor = mixer.Sound('Sounds/sol#.ogg')
solMayor.set_volume(1.0)
la = mixer.Sound('Sounds/la.ogg')
la.set_volume(1.0)
laMayor = mixer.Sound('Sounds/la#.ogg')
laMayor.set_volume(1.0)
si = mixer.Sound('Sounds/si.ogg')
si.set_volume(1.0)

# Creacion de compases
def Compas_generator(filler, Instrumento3):
    lista_1 = []
    contador = 0
    while contador != 2:
        for i in filler:
            lista_1.append(i)
        contador += 1
    
    lista_2 = []
    contador = 0
    while contador != 2:
        for i in Instrumento3:
            lista_2.append(i)
        contador += 1
    
    return lista_1, lista_2

filler, Instrumento3 = Compas_generator(filler, Instrumento3)

def creador_ritmo_armonico(filler, numerador):
    lista_1 = []
    contador = 0
    while contador < 8:
        for i in range(0, numerador):
            lista_1.append(i)
        contador += 1
        
    return lista_1

Ritmo_Armonico = creador_ritmo_armonico(filler, numerador)

def Dominante_Tonica_Sub(Ritmo_Armonico):
    seccionA = []
    seccionB = []

    # acordes de do
    AcordesDo = {
        'tonica': ['do', 'mi', 'sol'],
        'sub': ['fa', 'la', 'do'],
        'dominante': ['sol', 'si', 're']
    }
    # acordes de do#
    AcordesDoSostenido = {
        'tonica': ['do#', 'fa', 'sol#'],
        'sub': ['fa#', 'la#', 'do#'],
        'dominante': ['sol#', 'do', 're#']
    }
    # acordes de re
    AcordesRe = {
        'tonica': ['re', 'fa#', 'la'],
        'sub': ['sol', 'si', 're'],
        'dominante': ['la', 'do#', 'mi']
    }
    # acordes de re#
    AcordesReSostenido = {
        'tonica': ['re#', 'sol', 'la#'],
        'sub': ['sol#', 'do', 're#'],
        'dominante': ['la#', 're', 'fa']
    }

    # decidimos como eleguir los tonos
    mylist = [AcordesDo, AcordesDoSostenido, AcordesRe, AcordesReSostenido]
    c = random.choice(mylist)
    tonos = ["tonica", "dominante", "dominante", "sub", "sub", "sub"]
    compas = 1
    contador = 0

    # creamos seccion A
    for i in Ritmo_Armonico:
        if i == 0:
            if compas == 1:
                Ritmo_Armonico[contador] = c['tonica'][0]
                Ritmo_Armonico[contador+1] = c['tonica'][1]
                Ritmo_Armonico[contador+2] = c["tonica"][2]
                compas += 1
            elif (compas == 2) or (compas == 3) or (compas == 4):
                d = random.choice(tonos)
                Ritmo_Armonico[contador] = c[d][0]
                Ritmo_Armonico[contador+1] = c[d][1]
                Ritmo_Armonico[contador+2] = c[d][2]
                compas += 1
        contador += 1
    
    A = len(Ritmo_Armonico)/2
    A2 = 0
    while A2 < A:
        seccionA.append(Ritmo_Armonico[A2])
        A2 += 1

    # creamos seccion B 

    print("Ritmo armonico: "+str(Ritmo_Armonico))
    print("Seccion A: "+str(seccionA))
    return Ritmo_Armonico

Ritmo_Armonico = Dominante_Tonica_Sub(Ritmo_Armonico)

'''print("filer: "+str(filler))
print("Instrumento: "+str(Instrumento3))
print("Ritmo armonico: "+str(Ritmo_Armonico))'''

# Metodo para recorrer las listas
def Run(filler, Instrumento3, Ritmo_Armonico, numerador, division):
    bpm = 80
    beat_por_segundo = 60.0 / bpm / 4.0
    repeticiones = 0
    tonicaOdominante = True
    while repeticiones < 3:
        for i, e, u in zip(filler, Instrumento3, Ritmo_Armonico):
            if i == 0:
                sonido2.play()
                print("sonido 2")
                time.sleep(beat_por_segundo)
            elif i == 1:
                sonido3.play()
                print("sonido 3")
                time.sleep(beat_por_segundo)
            if e == 0:
                pass
            elif e ==1:
                sonido4.play() 
                print("sonido 4")   
                time.sleep(beat_por_segundo) 
            if u == "do":
                do.play()
                print("do")
                time.sleep(beat_por_segundo)
            elif u == "do#":
                doMayor.play()
                print("do#")
                time.sleep(beat_por_segundo)
            elif u == "re":
                re.play()
                print("re")
                time.sleep(beat_por_segundo)
            elif u == "re#":
                reMayor.play()
                print("re#")
                time.sleep(beat_por_segundo)
            elif u == "mi":
                mi.play()
                print("mi")
                time.sleep(beat_por_segundo)
            elif u == "fa":
                fa.play()
                print("fa")
                time.sleep(beat_por_segundo)
            elif u == "fa#":
                faMayor.play()
                print("fa#")
                time.sleep(beat_por_segundo)
            elif u == "sol":
                sol.play()
                print("sol")
                time.sleep(beat_por_segundo)
            elif u == "sol#":
                solMayor.play()
                print("sol")
                time.sleep(beat_por_segundo)
            elif u == "la":
                la.play()
                print("la")
                time.sleep(beat_por_segundo)
            elif u == "la#":
                laMayor.play()
                print("la#")
                time.sleep(beat_por_segundo)
            elif u == "si":
                si.play()
                print("si")
                time.sleep(beat_por_segundo)
        repeticiones += 1

# Creacion de un menu sencillo
pygame.init()
screen = pygame.display.set_mode([500, 500])
screen.fill((255, 255, 255))

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def redrawWindow():
    screen.fill((255, 255, 255))
    greenButton.draw(screen, (0,0,0))

run = True
greenButton = button((0,255,0), 150, 225, 250, 100, "play")

while run:
    redrawWindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton.isOver(pos):
                pass
                Run(filler, Instrumento3, Ritmo_Armonico, numerador, division)