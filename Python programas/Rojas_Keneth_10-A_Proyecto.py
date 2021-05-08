#Rojas_Keneth_10-A

print("Bienvenido!")

print("\nProyecto de Fundamentos de Electronica, Se le indicara al usuario multiples datos de la compra de un microprocesador incluyendo precios, IVA y se le entregará una factura con datos como la fecha a la que se realizó la compra y lo que se pagó a la hora ed la compra.\n")
condicion = 1

while condicion == 1:
    n = input("\033[1;37;46mIngrese su nombre con al menos un apellido: ")

    c = int(input("\nIngrese la cantidad de microprocesadores que desea comprar: "))

    print("La cantidad de microprocesadores que desea comprar es: ",c,) 

    d = input("\nEs correcta?\n")
    if d == "si":
        print("\nEl precio por unidad de microprocesador Ryzen 5 3600(6 nucleos con 3,6 GHz), es de 225 dolares.\n")

        articulo = "Ryzen 5 3600(6 nucleos con 3,6 GHz)"

        precio = 225*615

        def factura():
            print("\033[1;37;45mExtreme Tech S.A")

            print("Centro Comercial Plaza Heredia, Local 4E, Heredia, 40101")

            print("Teléfono: (506) 4001 4991")

            from datetime import datetime

            print("Fecha: ",datetime.now())

            print("Cliente: ",n)

            print("Descripción del articulo: ",articulo, "Cantidad: ",c, "Precio unitario: ₡",precio,)

            subtotal = precio*c

            print("\033[3;30;47msubtotal: ₡",subtotal)

            desc = (4/100)*subtotal

            print("Descuento: ₡",desc)

            sin_iva = subtotal-desc

            iva = (13/100)*sin_iva

            print("IVA: 13%  = ₡",iva)

            total = sin_iva + iva

            print("Total: ₡",total)

        factura()

        break
    else: 
        n = 2

        