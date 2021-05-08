print('\n Tablas de multiplicar \n')
num1 = int(input('Digite un numero: '))
 
for i in range(1,11):
    result = num1*i
    print(num1,'x',i,'=',result)
    if i == 10:
        break
