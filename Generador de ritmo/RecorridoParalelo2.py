import random
from winsound import Beep, PlaySound, SND_FILENAME
import time

def TerceraLista(relleno):      
        for i in relleno:
            try:
                i = int(i)
            except:
                pass

            if i == 0:
                time.sleep(0.1)
            elif i == 1:
                PlaySound('sound4.wav', SND_FILENAME)
                time.sleep(0.3)

ClaveConRelleno = open('relleno.txt','r')
ClaveConRelleno = ClaveConRelleno.read()
TerceraLista(ClaveConRelleno)