#el programa debe solicitar el nombre al usuario, su edad 
#guardarlo en un archivo y agregar el archivo
#el archivo debe de poder revisarse la informacion

import io

files = pen("Frasoe.txt","a") #a para agregar sin borrar lo anterior

print("datos de estudiantes")
nombre = input("Digite su nombre completo: ")
edad = input("Digite su edad en años: ")

files.write("\n"+nombre+"\n"+edad)

files.close()