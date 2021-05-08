#uso del while

print("\nHola mundo\n") #\n es para salto de linea verticalmente
print("holamundo")

#para el uso del while se necesita de una condicion cualquiera mientras sea posible que se cumpla, o no, preferiblemente numerica



condicion = 1



while condicion == 1:
   
    print("\nHola nuevamente\n")
    pregunta = float(input("En que numero estoy pensando? "))
    
    if pregunta == 5:
        print("correctooooo")
        break
    
    else:
       pregunta = 2 # numero diferente de la condicion del while para que se ejecute todo dentro del while nuevamente