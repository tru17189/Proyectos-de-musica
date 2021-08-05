teclado = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si",
           "Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si",
           "Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si",
           "do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si",
           "do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si",
           "do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

TECLADOMAYORES = []
TECLADOMENORES = []
TECLADOAUMENTADOS = []
posicion = 0
posicion_2 = 0

acorde_elegido = str(input("Escribe el acorde el cual quieres conocer su escala: "))
respuesta_acorde = []

for e in teclado:
    if acorde_elegido == e:
        respuesta_acorde.append("Original: "+teclado[posicion])
        TECLADOMAYORES.append(teclado[posicion])
        TECLADOMENORES.append(teclado[posicion-1])
        TECLADOAUMENTADOS.append(teclado[posicion+1])
        
        respuesta_acorde.append("Tono: "+teclado[posicion+2])
        TECLADOMAYORES.append(teclado[posicion+2])
        TECLADOMENORES.append(teclado[posicion+2-1])
        TECLADOAUMENTADOS.append(teclado[posicion+2+1])
        
        respuesta_acorde.append("Tono: "+teclado[posicion+4])
        TECLADOMAYORES.append(teclado[posicion+4])
        TECLADOMENORES.append(teclado[posicion+4-1])
        TECLADOAUMENTADOS.append(teclado[posicion+4+1])
        
        respuesta_acorde.append("1/2 Tono: "+teclado[posicion+5])
        TECLADOMAYORES.append(teclado[posicion+5])
        TECLADOMENORES.append(teclado[posicion+5-1])
        TECLADOAUMENTADOS.append(teclado[posicion+5+1])
        
        respuesta_acorde.append("Tono: "+teclado[posicion+7])
        TECLADOMAYORES.append(teclado[posicion+7])
        TECLADOMENORES.append(teclado[posicion+7-1])
        TECLADOAUMENTADOS.append(teclado[posicion+7+1])
        
        respuesta_acorde.append("Tono: "+teclado[posicion+9])
        TECLADOMAYORES.append(teclado[posicion+9])
        TECLADOMENORES.append(teclado[posicion+9-1])
        TECLADOAUMENTADOS.append(teclado[posicion+9+1])
        
        respuesta_acorde.append("Tono: "+teclado[posicion+11])
        TECLADOMAYORES.append(teclado[posicion+11])
        TECLADOMENORES.append(teclado[posicion+11-1])
        TECLADOAUMENTADOS.append(teclado[posicion+11+1])
        
        respuesta_acorde.append("1/2 Tono: "+teclado[posicion+12])
        TECLADOMAYORES.append(teclado[posicion+12])
        TECLADOMENORES.append(teclado[posicion+12-1])
        TECLADOAUMENTADOS.append(teclado[posicion+12+1])

        for u in range(1,7):
            TECLADOMAYORES.append(TECLADOMAYORES[u])
        for u in range(1,7):
            TECLADOMENORES.append(TECLADOMENORES[u])
        for u in range(1,7):
            TECLADOAUMENTADOS.append(TECLADOAUMENTADOS[u])

        print("ESCALA DE %s:" %e)
        print(respuesta_acorde)

        MAYORES = []
        MENORES = []
        DISMINUIDA = []
        AUMENTADOS = []
        for i in range(0, 7):
            MAYORES.append("*** %s ***: -%s-%s-%s" %(TECLADOMAYORES[posicion_2], TECLADOMAYORES[posicion_2], 
                                    TECLADOMAYORES[posicion_2+2], TECLADOMAYORES[posicion_2+4]))
            MENORES.append("*** %s ***: -%s-%s-%s" %(TECLADOMAYORES[posicion_2], TECLADOMAYORES[posicion_2], 
                                    TECLADOMENORES[posicion_2+2], TECLADOMAYORES[posicion_2+4]))
            DISMINUIDA.append("*** %s ***: -%s-%s-%s" %(TECLADOMAYORES[posicion_2], TECLADOMAYORES[posicion_2], 
                                    TECLADOMENORES[posicion_2+2], TECLADOMENORES[posicion_2+4]))
            AUMENTADOS.append("*** %s ***: -%s-%s-%s" %(TECLADOAUMENTADOS[posicion_2], TECLADOAUMENTADOS[posicion_2], 
                                    TECLADOAUMENTADOS[posicion_2+2], TECLADOAUMENTADOS[posicion_2+4]))
            posicion_2 += 1

        print("\n\nACORDES MAYORES DE LA ESCALA DE %s:" %e)
        print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" %(MAYORES[0], MAYORES[1], MAYORES[2],
                MAYORES[3], MAYORES[4], MAYORES[5], MAYORES[6]))
        
        print("\n\nACORDES MENORES DE LA ESCALA DE %s:" %e)
        print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" %(MENORES[0], MENORES[1], MENORES[2],
                MENORES[3], MENORES[4], MENORES[5], MENORES[6]))
        
        print("\n\nACORDES DISMINIIDO DE LA ESCALA DE %s:" %e)
        print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" %(DISMINUIDA[0], DISMINUIDA[1], DISMINUIDA[2],
                DISMINUIDA[3], DISMINUIDA[4], DISMINUIDA[5], DISMINUIDA[6]))
        
        print("\n\nACORDES AUMENTADOS DE LA ESCALA DE %s:" %e)
        print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" %(AUMENTADOS[0], AUMENTADOS[1], AUMENTADOS[2],
                AUMENTADOS[3], AUMENTADOS[4], AUMENTADOS[5], AUMENTADOS[6]))
        break
    posicion += 1
