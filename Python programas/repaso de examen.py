print("hola mundo")  #" "  ' '
print('hola mundo')

nombre = input("como te llamas?")
print("te llamas",nombre)


numero = float(input("digite un numero cualquiera: "))# float permite numeros de todo tipo, enteros y decimales
print("El numero que digitó es: ",numero)

decision = input("Desea continuar? ")

if decision == "si":   #==(igual al total) =(no existe) <(menor que) >(mayor que) =<(diferente de)
    print("Usted desea continuar")    

elif  decision == "no": #sigue siendo condicion, pero solo si no se cumple la anterior
    print('Va pa la mierda entonces')

else: #del todo no se cumple
    print("adio")





