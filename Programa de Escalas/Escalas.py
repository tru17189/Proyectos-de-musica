teclado = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si",
           "Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si",
           "Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
teclado_nuevo = []
posicion = 0
posicion_2 = 0

acorde_elegido = str(input("Escribe el acorde el cual quieres conocer su escala: "))

for e in teclado:
    if acorde_elegido == e:
        print("Original: "+teclado[posicion])
        teclado_nuevo.append(teclado[posicion])
        
        print("Tono: "+teclado[posicion+2])
        teclado_nuevo.append(teclado[posicion+2])
        
        print("Tono: "+teclado[posicion+4])
        teclado_nuevo.append(teclado[posicion+4])
        
        print("1/2 Tono: "+teclado[posicion+5])
        teclado_nuevo.append(teclado[posicion+5])
        
        print("Tono: "+teclado[posicion+7])
        teclado_nuevo.append(teclado[posicion+7])
        
        print("Tono: "+teclado[posicion+9])
        teclado_nuevo.append(teclado[posicion+9])
        
        print("Tono: "+teclado[posicion+11])
        teclado_nuevo.append(teclado[posicion+11])
        
        print("1/2 Tono: "+teclado[posicion+12])
        teclado_nuevo.append(teclado[posicion+12])

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

        print("\n\n-------Acordes-------")
        for i in range(0, 7):
            print("---"+teclado_nuevo[posicion_2]+"---")
            print("->"+teclado_nuevo[posicion_2])
            print("->"+teclado_nuevo[posicion_2+2])
            print("->"+teclado_nuevo[posicion_2+4])
            print("\n")
            posicion_2 += 1
        break
    posicion += 1
