#Rojas Vindas Keneth 10A


def datos():
    import io
    files = open("Usuarios.text","a")
    usuario = input("Digite un nombre de usuario: ")
    contraseña = input("Digite una contraseña de 6 Digitos: ")
    files.write("\n"+usuario+"\n"+contraseña)
    files.close

def lectura():
    import io
    files = open("Usuarios.text","r")
    datos = files.readlines()
    files.close()

    usuario = input("Digite su nombre de usuario: ")
    contraseña = input("Digite su contraseña: ")
    cuenta = datos.count(usuario+"\n"+contraseña+"\n")

print("fitness food\n")

print("Entrena tu alimentacion!")

condicion1 = 1

while condicion1 == 1:

  d =  input("Desea iniciar sesion(si) o ingresar como nuevo usuario(no)?")
  if d == "si":
      datos()
      a = 2 
  elif d == "no":
      lectura()
      busc = datos.index(usuario+"\n")
      print("\033[1;32m Bienvenido de vuelta!")
      break
  else:
      print("\033[1;31mUsted no se ha registrado en el sistema!")
      a = 2
