teclado = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si",
           "do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si",
           "do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

TECLADOMAYORES = []
TECLADONUMEROS = []
posicion = 0
posicion_2 = 0

acorde_elegido = str(input("Escribe el acorde el cual quieres conocer su escala: "))
respuesta_acorde = []

for e in teclado:
    if acorde_elegido == e:
        respuesta_acorde.append("Original: "+teclado[posicion])
        TECLADOMAYORES.append(teclado[posicion])
        respuesta_acorde.append("Tono: "+teclado[posicion+2])
        TECLADOMAYORES.append(teclado[posicion+2])
        respuesta_acorde.append("Tono: "+teclado[posicion+4])
        TECLADOMAYORES.append(teclado[posicion+4])
        respuesta_acorde.append("1/2 Tono: "+teclado[posicion+5])
        TECLADOMAYORES.append(teclado[posicion+5])
        respuesta_acorde.append("Tono: "+teclado[posicion+7])
        TECLADOMAYORES.append(teclado[posicion+7])
        respuesta_acorde.append("Tono: "+teclado[posicion+9])
        TECLADOMAYORES.append(teclado[posicion+9])
        respuesta_acorde.append("Tono: "+teclado[posicion+11])
        TECLADOMAYORES.append(teclado[posicion+11])
        respuesta_acorde.append("1/2 Tono: "+teclado[posicion+12])
        TECLADOMAYORES.append(teclado[posicion+12])

        for u in range(1,7):
            TECLADOMAYORES.append(TECLADOMAYORES[u])

        print("ESCALA DE %s:" %e)
        print(respuesta_acorde)

        MAYORES = []
        for i in range(0, 7):
            sumatoria = 0   
            SumTime = False                     
            for i in teclado:
                if i == TECLADOMAYORES[posicion_2]:
                    SumTime = True
                if i == TECLADOMAYORES[posicion_2+2] and SumTime == True:
                    SumTime = False
                    break
                if SumTime == True:
                    sumatoria += 0.5
            segunda = sumatoria

            sumatoria = 0   
            SumTime = False                     
            for i in teclado:
                if i == TECLADOMAYORES[posicion_2+2]:
                    SumTime = True
                if i == TECLADOMAYORES[posicion_2+4] and SumTime == True:
                    SumTime = False
                    break
                if SumTime == True:
                    sumatoria += 0.5
            tercera = sumatoria

            palabra = ""
            if segunda == 2.0 and tercera == 1.5:
                palabra = "MAYOR"
            elif segunda == 1.5 and tercera == 2.0:
                palabra = "MENOR"
            elif segunda == 2.0 and tercera == 2.0:
                palabra = "AUMENTADA"
            elif segunda == 1.5 and tercera == 1.5:
                palabra = "DISMINUIDA"
            
            MAYORES.append("*** %s ***: -%s-%s-%s\t%s" %(TECLADOMAYORES[posicion_2], TECLADOMAYORES[posicion_2], 
                                    TECLADOMAYORES[posicion_2+2], TECLADOMAYORES[posicion_2+4], palabra))


            posicion_2 += 1

        print("\n\nACORDES DE LA ESCALA DE %s:" %e)
        print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" %(MAYORES[0], MAYORES[1], MAYORES[2],
                MAYORES[3], MAYORES[4], MAYORES[5], MAYORES[6]))

        break
    posicion += 1
