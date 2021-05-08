print("Bienvenido")

print("\nCalculador de impuestos mesuales\n")

salario_mensual = float(input("\nIngrese su salario mensual: \n"))

conidicion = 1

while conidicion == 1:
    dato = print("\nsu salario mensual es de: ",salario_mensual)

    if 0 < salario_mensual < 100000:
        imp1 = (5/100)*salario_mensual
        
        print('mensualmente usted pagara ',imp1,'de impuestos')
        break
    elif 100001 < salario_mensual < 200000:
        imp2 = (10/100)*salario_mensual
        
        print('mensualmente usted pagara ',imp2,'de impuestos')
        break
    elif 200001 < salario_mensual < 400000:
        imp3 = (15/100)*salario_mensual
        
        print('mensualmente usted pagara ',imp3,'de impuestos')
        break
    elif 400001 < salario_mensual == 600000:
        imp4 = (20/100)*salario_mensual
        
        print('mensualmente usted pagara ',imp4,'de impuestos')
        break
    else:
        imp5 = (25/100)*salario_mensual

        print('mensualmente usted pagara ',imp5,'de impuestos')
        break
    

