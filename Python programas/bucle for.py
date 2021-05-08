print("\nbienvenido\n")

num1 = float(input("digite un numero: ")) #se le solicita un numero cualquiera al usuario

for i in range(1,11): #i representa el rango del 1-10
    op = i*num1
    print(num1,"*",i,"=",op)
    if i == 10: #condicion para que frene el programa apenas llegue al ultimo numero del rango
        break