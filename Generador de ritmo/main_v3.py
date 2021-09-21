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
    mylist = [3, 4, 5, 6, 7]
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
            relleno.append(1)
            i -= 1
    return relleno

filler = []
filler = crearRelleno(claveF, division)
labelRelleno = filler

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
print(filler)
print(Instrumento3)

# Recolectamos los sonidos
mixer.init()
sonido1 = mixer.Sound('sound4.ogg') 
sonido2 = mixer.Sound('sound5.ogg')    
sonido3 = mixer.Sound('sound6.ogg') 
sonido4 = mixer.Sound('sound7.ogg')  

# Metodo para recorrer las listas
def Run(filler, Instrumento3):
    bpm = 100
    beat_por_segundo = 60.0 / bpm / 4.0
    print(beat_por_segundo)
    for i, e in zip(filler, Instrumento3):
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
                Run(filler, Instrumento3)