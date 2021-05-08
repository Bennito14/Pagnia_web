
('\n Registro 2021 \n')
registro = []
si=1
while si <= 3:
    eleccion = input('Desea agregar un nuevo usuario(si/no): ')

    if eleccion == 'si':
        usuario=input('Ingrese el nuevo nombre de usuario: ')
        registro.append(usuario)
 
    elif eleccion == 'no':
        print('Muchas Gracias, vuelva pronto.')
        break
    
    else:
        print('Usted no ha ingresado si o no.')

print(registro)
print('\n Muchas gracias, vuelva pronto \n')






