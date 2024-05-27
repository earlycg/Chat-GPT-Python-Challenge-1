# 20 ejercicios para aprender a declarar variables en Python. Estos ejercicios están diseñados para cubrir desde conceptos básicos hasta un poco más avanzados:

### Ejercicio 1: Declaración básica
# Declara una variable llamada `nombre` y asígnale tu nombre como valor. Imprime la variable.
nombre = 'Early'
print(nombre)
### Ejercicio 2: Números enteros
# Declara una variable llamada `edad` y asígnale tu edad como valor. Imprime la variable.
edad = 34
print(edad)

### Ejercicio 3: Números decimales
# Declara una variable llamada `altura` y asígnale tu altura en metros. Imprime la variable.
altura = 1.70
print(altura)

### Ejercicio 4: Booleanos
# Declara una variable llamada `es_estudiante` y asígnale un valor booleano que indique si eres estudiante o no. Imprime la variable.

es_estudiante = True
print(es_estudiante)

### Ejercicio 5: Concatenación de cadenas
# Declara dos variables `nombre` y `apellido`, y asígnales tu nombre y apellido. Luego, concatena las dos variables e imprime el resultado.

nombres = 'Early Start'
apellidos = 'Diaz Buelvas'

print(f"{nombres} {apellidos}")

print(nombres +" "+ apellidos)


### Ejercicio 6: Suma de enteros
# Declara dos variables `a` y `b`, asígnales valores enteros, suma las dos variables e imprime el resultado.

a = 32
b = 57

print(a+b)

suma = a + b

print(suma)

### Ejercicio 7: Resta de decimales
# Declara dos variables `x` y `y`, asígnales valores decimales, resta las dos variables e imprime el resultado.

x = 100
y = 50

resta = x - y
resta_inver = y - x

print(resta,  resta_inver)


### Ejercicio 8: Multiplicación
# Declara dos variables `m` y `n`, asígnales valores enteros, multiplícalos e imprime el resultado.

m = 5
y = 8

def multi(num1, num2):
    print(num1 * num2)

multi(m, y)

### Ejercicio 9: División
# Declara dos variables `p` y `q`, asígnales valores enteros, divide `p` entre `q` e imprime el resultado.
p = 40
q = 2

print(p / q)

### Ejercicio 10: Potenciación
# Declara una variable `base` y otra `exponente`. Calcula `base` elevado a `exponente` e imprime el resultado.
base = 4
exponente = 8

print(base ** exponente)


### Ejercicio 11: Módulo
# Declara dos variables `dividendo` y `divisor`, calcula el módulo (residuo de la división) e imprime el resultado.

dividendo = 100
divisor = 4
print(100 % 4 )

### Ejercicio 12: Declaración múltiple
# Declara tres variables `a`, `b` y `c` en una sola línea, asígnales valores e imprímelas.

a, b, c = 1, 2, 3

print(a, b, c)


### Ejercicio 13: Intercambio de valores
# Declara dos variables `a` y `b`, asígnales valores e intercambia sus valores. Imprime los valores antes y después del intercambio.

a = 1
b = 2
print(a,b)
temp = a
a = b
b = temp

print(a,b)

### Ejercicio 14: Variables con listas
# Declara una variable `frutas` que sea una lista de tres frutas diferentes. Imprime la lista.

### Ejercicio 15: Variables con diccionarios
# Declara una variable `persona` que sea un diccionario con llaves `nombre`, `edad` y `ciudad`. Asigna valores adecuados e imprime el diccionario.

### Ejercicio 16: Actualización de variables
# Declara una variable `contador`, asígnale el valor 0. Luego, incrementa su valor en 1 e imprime el resultado.

### Ejercicio 17: Tipos de datos
# Declara variables de diferentes tipos de datos: `cadena`, `entero`, `flotante` y `booleano`. Imprime los tipos de datos de cada variable.

### Ejercicio 18: Variables locales
# Escribe una función llamada `mostrar_nombre` que declare una variable local `nombre` e imprima su valor.

### Ejercicio 19: Variables globales
# Declara una variable global `contador` fuera de cualquier función. Escribe una función llamada `incrementar` que incremente el valor de `contador` en 1 cada vez que se llame. Imprime `contador` antes y después de llamar a la función.

### Ejercicio 20: Variables con tuplas
# Declara una variable `punto` que sea una tupla con dos valores: coordenadas x e y. Imprime la tupla."""
