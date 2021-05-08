#listas

i = 1
nombres = []
while i == 1 :
    
    c = input("Desea agregar un nombre: ")
    
    if c == "si":
        
       nombre = input("Agregue un nombre a la lista: ")
       nombres.append(nombre) #appen == agregar datos a el nombre de la variable variable.append(variable de donde se agrega)
       c = 2
    elif c == "no":
        
        print("Gracias")
        break

    else:
        print("usted no digito si/no")
        c = 2
    print(nombres) 

