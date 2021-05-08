import io

files = open("datos.text","r")#r para leer los datos dentro del archivo
datos = files.readlines()
files.close()

print(datos)

nombre = input("Ingrese el nombre de la persona que desea buscar: ")

cuenta = datos.count(nombre+"\n")

if cuenta!=0:
    pos = datos.index(nombre+"\n")
    print("La edad de",nombre, "es de ",datos[(pos+1)])

else:
    print("no hay persona de nombre",nombre)