#Chaves_Fiorella_10-A

print("\033[3;31m" + " \n Proyecto de Fundamentos de electrónica,el proyecto consiste en la programación de una factura electrónica utilizando las distintas funciones estudiadas en clase \n ")

print("\033[3;37m" + (" ¡Buen día!"))
 
num1 = 26
while num1 == 26:

    nom = input("\033[3;35;40m" + " \n Por favor ingrese su nombre completo: \n ")

    micro = int(input(" \n ¿Cuántos microprocesadores desea adquirir? \n "))

    respuesta = input(" \n ¿La cantidad solicitada es la correcta? \n ")

    colones = 225*615
    if respuesta == "si":
        
        print("\033[3;36m" + "\n Extreme Tech S.A \n ")
        
        print("\033[0m" + "\n Centro Comercial Plaza Heredia, Local 4E, Heredia, 40101 \n ")
        
        print("Teléfono: (506) 4001 4991")

        from datetime import datetime
        print("fecha: ",datetime.now())
         
        print("Cliente:", nom )

        print("Ryzen 5 3600, 6 núcleos,3,6 GHz")
       
        print("La cantidad de microprocesadores es:", micro)
       
        print("El precio unitario por cada microprocesador: ", colones, "colones")

        subtot = colones*micro
        print("El subtotal es de:", subtot, "colones")
        
        discount = round(((4/100)*subtot),2)
        print("El descuento es de:", discount, "colones")

        iva = (13/100)*subtot
        print("El I.V.A es de:", iva, "colones" )

        total = subtot-discount+iva
        print("\033[3;32m"+ "El total de su compra es de:", total, "colones")
       
        print("\033[3;37m" + " \n Gracias por comprar en Extreme Tech S.A \n ")
        
        break
    else:
        micro = 27


