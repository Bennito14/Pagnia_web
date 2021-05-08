#el programa debe solicitar el nombre al usuario, su edad 
#guardarlo en un archivo y agregar el archivo
#el archivo debe de poder revisarse la informacion

import io

archivo = open("Frase.txt","r")

gestion_archivos = archivo.readlines()

print(gestion_archivos)

