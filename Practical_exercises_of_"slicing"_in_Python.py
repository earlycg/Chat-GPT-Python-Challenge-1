# 20 ejercicios para practicar la notación de rebanado (slicing) en Python:

# 1. Dada una lista `nums`, obtener los primeros 5 elementos.

nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[0:5:1])

def clasif(list):
    for i in list[0:5:1]:
        print(i)

clasif(nums)

# 2. Dada una cadena `palabra`, obtener los últimos 3 caracteres.

palabras = ["manzana", "bicicleta", "computadora", "árbol", "montaña", "río", "gato", "libro", "sol", "estrella"]

print(palabras[-1:-4:-1])
print(palabras[-3:])

# 3. Dada una lista `numeros`, obtener todos los elementos excepto el primero y el último.

def Sin_pie_ni_cabeza(lista):
    for i in lista[1:-1:1]:
        print(i)

numeros = [1,2,3,4,5,6,7,8,9,10]
Sin_pie_ni_cabeza(numeros)

# 4. Dada una lista `letras`, obtener los elementos en índices pares.

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(alfabeto[0::2])

#5. Dada una cadena `frase`, obtener cada segundo carácter.

cadena = 'frase'

print(cadena[1::2])

#6. Dada una lista `pares`, obtener los elementos desde el segundo hasta el penúltimo, saltando de dos en dos.

pares = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(pares[1:-1:1])

#7. Dada una lista `nombres`, obtener los últimos tres elementos.

# Lista de nombres
nombres = ["Ana", "Juan", "María", "Pedro", "Luis", "Carmen", "Jorge", "Elena", "Carlos", "Laura"]

print(nombres[-3:])

print(nombres[-1:-4:-1])

#8. Dada una cadena `texto`, obtener una subcadena que incluya desde el tercer carácter hasta el séptimo.

cadena = 'tesalonisense'
print(cadena[2:7:1])

#9. Dada una lista `valores`, obtener una lista con los elementos en posiciones impares.

valores = ['manzana', 'banana', 'cereza', 'dátiles', 'uva', 'fresa', 'kiwi', 'limón', 'mango', 'naranja', 'pera', 'piña', 'sandía', 'papaya', 'melocotón', 'aguacate', 'ciruela', 'frambuesa', 'melón', 'granada']


print(valores[1::2])

#10. Dada una lista `edades`, obtener los elementos en índices impares, comenzando desde el segundo elemento.

edades = [20, 45, 10, 30, 55, 5, 25, 15, 35, 50]
print(edades[1::2])

#11. Dada una cadena `cadena`, obtener una subcadena que incluya los caracteres en posiciones pares.

edades = [20, 45, 10, 30, 55, 5, 25, 15, 35, 50]
print(edades[0::2])

#12. Dada una lista `numeros`, obtener una lista con los elementos en posiciones múltiplos de 3.

numeros = list(range(0, 101))
list1 = [numeros[1]]
list2 = numeros[3::3]
list1.extend(list2)
final = list1

print(final)

#13. Dada una lista `lista`, obtener una lista con los elementos en posiciones impares, pero en orden inverso.
#14. Dada una cadena `texto`, obtener una subcadena que contenga los últimos 4 caracteres en orden inverso.
#15. Dada una lista `nums`, obtener una lista con los elementos en posiciones pares, pero en orden inverso.
#16. Dada una lista `palabras`, obtener una lista con las palabras que tienen una longitud mayor a 5 caracteres.
#17. Dada una cadena `frase`, obtener una subcadena que contenga las palabras en posición par.
#18. Dada una lista `numeros`, obtener una lista con los elementos desde el tercer elemento hasta el quinto, en orden inverso.
#19. Dada una lista `elementos`, obtener una lista que contenga solo los elementos en índices impares, pero sin incluir el último elemento.
#20. Dada una cadena `texto`, obtener una subcadena que contenga los caracteres en posiciones impares, pero en orden inverso.
