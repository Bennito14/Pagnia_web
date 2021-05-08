#calcule el IMC con el peso y la altura del usuario con la formula
#peso(kg)/altura(m) al cuadrado

peso = float(input("Digite su peso en Kg: "))

altura = float(input("Digite su altura en m: "))

imc = round((peso)/(pow(altura,2)),2)

print("su imc es de: ",imc)

if imc < 16:
    print("\033[1;37;41m"+"Usted esta en delgadez severa, contacte a un nutricionista.")

elif 16<= imc <18.5:
    print("\033[1;33m"+"Usted esta en delgadez moderada, debe mejorar un poco mas!")

elif 18.5 <= imc <25:
    print("\033[1;37;42m"+"Usted esta bien siga asi!")

elif 25<= imc <30:
     print("\033[1;33m"+"Usted esta en sobrepeso")

elif 30<= imc <35:
     print("\033[1;33m"+"Ustes esta en sobrepeso grado l")

else:
    print("\033[1;37;41m"+"Usted esta en sobre peso grado 2")