# 20 ejercicios para practicar y entender el concepto de `not in` en Python. Estos ejercicios están diseñados para que pienses en la lógica detrás del uso de `not in`:

"""

# 1. Dada una lista de números `[1, 2, 3, 4, 5]`, verifica si el número 7 no está en la lista.

lista = [1,2,3,4,5,7]

if 7 not in lista:
    print("7 no esta en la lista")
else:
    print("7 si esta en la lista")


# 2. Tienes la cadena `"Hola Mundo"`. Comprueba si el carácter `'a'` no está en la cadena.

saludo = "hola mundo"
contador = 0
if 'a' not in saludo:
    print("'a' no esta en la oración")

contador += 1
print(f"'a' si esta en la oración en {contador} ocasión")


#------------------------------------------------------------------------------

lista_palabras = ["hola mundo","hello wold", "saludos", "real"]

for j, i in enumerate(lista_palabras):
    if 'a' in i:
    print(f"'a' si esta en la oración por {j}")
print("'a' no esta en la oración")


#------------------------------------------------------------------------------

lista_palabras = ["hola mundo","hello wold", "saludos", "real"]
contador = 0
for j, i in enumerate(lista_palabras):
        if 'a' in i:
            contador += 1
            vez_veces = "vez" if contador == 1  else "veces"
            print(f"la letra (a) se ha encontrado por {contador} {vez_veces}, esta vez se encontró en la palabra {lista_palabras[j]}")

print(f"se han encontrado {contador} (a) hasta el momento")


#------------------------------------------------------------------------------



lista_palabras = ["hola mundo","hello wold", "saludos", "real"]
long = len(lista_palabras)
contador = 0
for b in range(long):
    for i in lista_palabras[b]:
        if 'a' in i:
            contador += 1
            vez_veces = "vez" if contador == 1  else "veces"
            print(f"la letra (a) se ha encontrado por {contador} {vez_veces}, esta vez se encontró en la palabra {lista_palabras[b]}")

print(f"se han encontrado {contador} (a) hasta el momento")

# 3. Dada una tupla `(10, 20, 30, 40, 50)`, verifica si el número 25 no está en la tupla.


def esta(num, lista):
    if num not in lista:
        print(f"{num} no esta en la lista")
    else:
        print(f"{num} si esta en la lista")
tupla = (10, 20, 30, 40, 50)
esta(20, tupla)



# 4. Tienes una lista de palabras `["perro", "gato", "ratón"]`. Comprueba si la palabra `"elefante"` no está en la lista.
animales = ["perro", "gato", "ratón"]
buscar = "elefante"
if buscar not in animales:
    print(f"{buscar} no esta en la lista")

else:
    print(f"{buscar} si esta en la lista")

# 5. Dado un diccionario `{"nombre": "Ana", "edad": 25}`, verifica si la clave `"dirección"` no está en el diccionario.
diccionario = {"nombre": "Ana", "edad": 25}
palabra = "dirección"
if palabra not in diccionario:
    print(f"{palabra} no se encuentra en el diccionario")
else:
    print(f"{palabra} si se encuentra en el diccionario")
