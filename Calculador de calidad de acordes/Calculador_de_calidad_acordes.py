teclado = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si",
           "Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si",
           "Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
teclado_nuevo = []
posicion = 0
posicion_2 = 0

acorde_elegido = str(input("Escribe el acorde el cual quieres conocer su escala: "))
respuesta_acorde = []

for e in teclado:
    if acorde_elegido == e:
        respuesta_acorde.append("Original: "+teclado[posicion])
        teclado_nuevo.append(teclado[posicion])
        
        respuesta_acorde.append("Tono: "+teclado[posicion+2])
        teclado_nuevo.append(teclado[posicion+2])
        
        respuesta_acorde.append("Tono: "+teclado[posicion+4])
        teclado_nuevo.append(teclado[posicion+4])
        
        respuesta_acorde.append("1/2 Tono: "+teclado[posicion+5])
        teclado_nuevo.append(teclado[posicion+5])
        
        respuesta_acorde.append("Tono: "+teclado[posicion+7])
        teclado_nuevo.append(teclado[posicion+7])
        
        respuesta_acorde.append("Tono: "+teclado[posicion+9])
        teclado_nuevo.append(teclado[posicion+9])
        
        respuesta_acorde.append("Tono: "+teclado[posicion+11])
        teclado_nuevo.append(teclado[posicion+11])
        
        respuesta_acorde.append("1/2 Tono: "+teclado[posicion+12])
        teclado_nuevo.append(teclado[posicion+12])

        print("ESCALA DE %s:" %e)
        print(respuesta_acorde)

        teclado_nuevo.append(teclado[posicion+2])
        teclado_nuevo.append(teclado[posicion+4])
        teclado_nuevo.append(teclado[posicion+5])
        teclado_nuevo.append(teclado[posicion+7])
        teclado_nuevo.append(teclado[posicion+9])
        teclado_nuevo.append(teclado[posicion+11])
        teclado_nuevo.append(teclado[posicion+12])
        teclado_nuevo.append(teclado[posicion+2])
        teclado_nuevo.append(teclado[posicion+4])
        teclado_nuevo.append(teclado[posicion+5])
        teclado_nuevo.append(teclado[posicion+7])
        teclado_nuevo.append(teclado[posicion+9])
        teclado_nuevo.append(teclado[posicion+11])
        teclado_nuevo.append(teclado[posicion+12])

        respuesta_acorde = []
        print("\n\nACORDES DE LA ESCALA DE %s:" %e)
        for i in range(0, 7):
            respuesta_acorde.append("*** %s ***: -%s-%s-%s" %(teclado_nuevo[posicion_2], teclado_nuevo[posicion_2], 
                                    teclado_nuevo[posicion_2+2], teclado_nuevo[posicion_2+4]))
            posicion_2 += 1

        print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" %(respuesta_acorde[0], respuesta_acorde[1], respuesta_acorde[2],
                respuesta_acorde[3], respuesta_acorde[4], respuesta_acorde[5], respuesta_acorde[6]))
        break
    posicion += 1
