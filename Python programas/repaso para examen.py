#practica de examen

#Defina una funcion que calcule el area del triangulo con la formula de Heron

a = float(input("Digite 3 lados en cm: "))
b = float(input(""))
c = float(input(""))
def triangle_area():
    s = (a+b+c)/2

    import math

    area = round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)
    
    print("El area del triangulo es de: ", area,"cm2")

triangle_area()