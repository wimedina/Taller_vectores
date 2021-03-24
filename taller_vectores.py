# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 00:02:13 2021

@author: William Medina
"""

# De los n elementos de un vector dado calcule:
# a.a. La sumatoria
# b. La productoria
# c. El Mayor Elemento
# d. El menor Elemento

i = 0
j = 0
elementos = []
sumatoria = 0
productoria = 1
while True:
    elemento = float(input(f'Ingrese el elemento numero {i} o digite 0 para salir '))
    if elemento == 0:
        break
    elementos.append(elemento)
    i += 1
# sumatoria
sumatoria = sum(elementos)
# productoria
for j in elementos:
    productoria *= j
# Mayor elemento
mayor = max(elementos)
# Menor elemento
menor = min(elementos)

print(f'La sumatoria de los elementos es {sumatoria}')
print(f'La productoria de los elementos es {productoria}')
print(f'El mayor elemento del vector es {mayor}')
print(f'El menor elemento del vector es {menor}')

# De los n elementos de un vector dado calcule:
# a. Cantidad de elementos pares
# b. Cantidad de elementos impares
# c. Cantidad de elementos primos

i = 1
j = 0
m = 0
cont_prim = 0
cont_res = 0
elementos = []
pares = 0
impares = 0
while True:
    elemento = float(input(f'Ingrese el elemento numero {i} o digite 0 para salir '))
    if elemento == 0:
        break
    elementos.append(elemento)
    i += 1

# numeros primos
for m in elementos:
    n = 1
    cont_res = 0
    while n <= m:
        if m % n == 0:
            cont_res += 1     
        n += 1       
    if cont_res == 2:
        cont_prim += 1

#Elementos pares e impares
for j in elementos:
    if j % 2 == 0:
        pares += 1
    elif j % 2 == 1:
        impares += 1

print(elementos)
print(f'La cantidad de elementos pares es {pares}')
print(f'La cantidad de elementos impares es {impares}')
print(f'La cantidad de elementos primos es {cont_prim}')
        
        
        
# =============================================================================
# Dado un Vector v y un Vector v1 de cómo resultado un Vector resultante de
# las siguientes operaciones:
# a. Suma
# b. Resta      

vectorA = []
vectorB = []
resultadoSuma = []
resultadoResta = []
suma = 0
resta = 0
#x = 0
tamano = int(input('Defina el tamaño de los vectores '))

for i in range(1,tamano + 1):
    elementoA = float(input('Ingrese los elementos del vector A '))
    vectorA.append(elementoA)
    
for j in range(1,tamano + 1):
    elementoB = float(input('Ingrese los elementos del vector B '))
    vectorB.append(elementoB)

# print(vectorA)
# print(vectorB)

# suma de los vectores
for x in range(0,tamano):
    suma = vectorA[x] + vectorB[x]
    resultadoSuma.append(suma)
    suma = 0

for z in range(0,tamano):
    resta = vectorA[z] - vectorB[z]
    resultadoResta.append(resta)
    resta = 0
    
print(f'El vector A es {vectorA}')
print(f'El vector B es {vectorB}')
print(f'El resultado de la suma de los vectores es {resultadoSuma}')
print(f'El resultado de la resta de los vectores es {resultadoResta}')



# 4.De los n elementos de un vector dado identifique el número que mas se
# repite e indique cual es.


i = 1
elementos = []
cont_igual = 0
aux_igual = 0
repetido = 0
aux_rep = 0
while True:
    numero = float(input(f'Ingrese el elemento {i} o digite 0 para salir '))
    if numero == 0:
        break
    elementos.append(numero)
    i += 1
    
for j in elementos:
    for m in elementos:
        if j == m:
            cont_igual += 1
            repetido = m
            
    if cont_igual > aux_igual:
        aux_igual = cont_igual
        aux_rep = repetido
    cont_igual = 0
    
print(f'El numero {aux_rep} es el numero que mas se repite con {aux_igual} veces')


# 5. Dado un Vector v de longitud par, divida en 2 partes, en la primera parte
# realice la productoria y en la segunda la sumatoria. Entregue los valores
# resultantes.
            
elementos = []
z = 0
x = 0
sumatoria = 0
produc = 1
while True:
    numero = int(input('Ingrese el tamaño par del vector '))
    if numero % 2 != 0:
        print('Debe ingresar un número par')
    else:
        break
    
for z in range(0,numero):
    elemento = float(input(f'Ingrese el elemento {z} '))
    elementos.append(elemento)

mitad = len(elementos)/2
mitad_Int = int(mitad)
a = elementos[:mitad_Int]
b = elementos[mitad_Int:]

#sumatoria
sumatoria = sum(b)
#productoria
for x in a:
    produc *= x 

print(f'El vector original es \n'
      f'{elementos}')
print(f'La  productoria de la primera parte del vector es {produc}') 
print(f'La sumatoria de la segunda parte del vector es {sumatoria}')

# 6. Dado un vector v, indique si es simétrico, un vector es simétrico si siendo
# longitud par los números de la primera mitad son iguales al inverso de la
# otra mitad por ejemplo: X=[1,2,3,3,2,1], en el ejemplo x es un vector
# simétrico, en caso que la longitud del vector sea impar, se ignorará el
# elemento central y se seguirá la misma lógica anterior, por ejemplo:
# Y=[3,5,7,8,7,5,3], en este ejemplo Y es simétrico.

i = 0
m = 0
n = 0
vector = []
simetrico = True
while True:
    numero = int(input(f'Ingrese el elemento {i} del vector o digite 0 para salir '))
    if numero == 0:
        break
    vector.append(numero)
    i += 1
                  
if len(vector) % 2 == 0 :  
    m = 0
    n = len(vector) - 1
    for j in vector:      
        if vector[m] != vector[n]:
            simetrico = False
            print('El vector no es simetrico')
            break       
        else:
            simetrico = True
            m += 1
            n -= 1
    
    if simetrico:
        print('El vector es simetrico')

elif len(vector) % 2 == 1:
    medio = int((len(vector) - 1) / 2)
    vector.pop(medio)
    m = 0
    n = len(vector) - 1
    for j in vector:
        if vector[m] != vector[n]:
            simetrico = False
            print('El vector no es simetrico')
            break
        else:
            simetrico = True
            m += 1
            n -= 1
    
    if simetrico:
        print('El vector es simetrico')
                      
                         

# 7. Dado dos vectores númericos A y B debe realizar las siguiente operaciones
# con conjuntos:
# a. Unión: Conjunto que contiene(sin repetir) los elementos de A y B.
# b. Intersección: Conjunto que contiene los elementos comunes que
# aparecen en los conjuntos A y B
# c. Diferencia(A-B) Conjunto formado por los elementos que pertenecen
# al conjunto A y no pertenecen al conjunto B.
# d. Diferencia (B-A) Conjunto formado por los elementos que pertenecen
# al conjunto B y no pertenecel al conjunto A.
    

vectorA = []
vectorB = []
vector_Dif_AB = []
vector_Dif_BA = []
vectorInter = []
aux_conj = False
i = 1
j = 1
m = 0
n = 0

while True:
    numero = int(input(f'Ingrese el elemento {i} del vector A o digite 0 para salir '))
    if numero == 0:
        break
    vectorA.append(numero)
    i += 1

while True:
    numero = int(input(f'Ingrese el elemento {j} del vector B o digite 0 para salir '))
    if numero == 0:
        break
    vectorB.append(numero)    
    j += 1
    
for m in range(0, len(vectorA)):
    for n in range(0, len(vectorB)):
        if (vectorA[m] == vectorB[n - 1]):
            vectorB.pop(n - 1)
            vectorInter.append(vectorB[n - 1])
        else:
            aux_conj = True
    if (aux_conj):
        vector_Dif_AB.append(vectorA[m])
        aux_conj = False
        
aux_conj = False
m = 0
n = 0     
for m in range(0, len(vectorB)):
    for n in range(0, len(vectorA)):
        if (vectorB[m] != vectorA[n - 1]):
            aux_conj = True
    if (aux_conj):
        vector_Dif_BA.append(vectorB[m])
        aux_conj = False

print(f'La union del vector A y B es{vectorA + vectorB}')
print(f'Interseccion Vector A y B: {vectorInter}')
print(f'La diferencia de A-B es: {vector_Dif_AB}')
print(f'La diferencia de B-A: {vector_Dif_BA}')

            









