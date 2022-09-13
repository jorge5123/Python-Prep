def verifica_primo(num):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    
    return es_primo


def extrae_primos_de_lista(lista):
    lista_primos = []
    for elem in lista:
        if verifica_primo(int(elem)):
            lista_primos.append(elem)
    return lista_primos

lis_completa = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20.189]
lis_primos = extrae_primos_de_lista(lis_completa)
print(lis_primos)

def valor_modal(lista,menor):
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    if (menor):
        lista.sort()
    else:
        lista.sort(reverse=True)
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repeticiones[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repeticiones.append(1)
    moda = lista_unicos[0]
    maximo = lista_repeticiones[0]
    for i, elemento in enumerate(lista_unicos):
        if lista_repeticiones[i] > maximo:
            moda = lista_unicos[i]
            maximo = lista_repeticiones[i]
    return moda, maximo




lis = [10,1,5,6,8,10,22,5,6,4,11,10,9,5]
moda, repite = valor_modal(lis, False)
print('El valor modal es', moda, 'y se repite', repite, 'veces.')




def conversion_grados(valor,origen,destino):
    if (origen == 'C'):
        if(destino == 'C'):
            valor_destino = valor
        elif(destino == 'F'):
            valor_destino = (valor*9/5)+32
        elif(destino == 'K'):
            valor_destino = (valor+ 273.15)
        else:
            print('parametro de destino incorrecto')
    elif (origen == 'F'):
        if(destino == 'F'):
            valor_destino = valor
        elif(destino == 'C'):
            valor_destino = (valor-32)*5/9
        elif(destino == 'K'):
            valor_destino = ((valor-32)*5/9)+273.15
        else:
            print('parametro de destino incorrecto')
    elif (origen == 'K'):
        if(destino == 'K'):
            valor_destino = valor
        elif(destino == 'C'):
            valor_destino = (valor-273.15)
        elif(destino == 'F'):
            valor_destino = ((valor-273.15)*9/5)+32
        else:
            print('parametro de destino incorrecto')
    else:
        print('Parametro de Origen incorrecto')
    return valor_destino
a = conversion_grados(15,'C','K')
print(a)
print('1 grado Celsius a Celsius:', conversion_grados(1, 'C', 'C'))
print('1 grado Celsius a Kelvin:', conversion_grados(1, 'C', 'K'))
print('1 grado Celsius a Farenheit:', conversion_grados(1, 'C', 'F'))
print('1 grado Kelvin a Celsius:', conversion_grados(1, 'K', 'C'))
print('1 grado Kelvin a Kelvin:', conversion_grados(1, 'K', 'K'))
print('1 grado Kelvin a Farenheit:', conversion_grados(1, 'K', 'F'))
print('1 grado Farenheit a Celsius:', conversion_grados(1, 'F', 'C'))
print('1 grado Farenheit a Kelvin:', conversion_grados(1, 'F', 'K'))
print('1 grado Farenheit a Farenheit:', conversion_grados(1, 'F', 'F'))

print(verifica_primo(5))  

def factorial(numero):
    if(type(numero)!= int):
        return 'El numero debe ser entero'
    if(numero<0):
        return 'el numero debe se positivo'
    if(numero>1):
        numero=numero * factorial(numero-1)
    return numero
print(factorial(3))
        
    
  




