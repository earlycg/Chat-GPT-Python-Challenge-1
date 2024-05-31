#30 ejercicios para practicar el bucle `while` en Python, organizados en orden creciente de dificultad:

### Ejercicios Básicos

#1. **Imprimir números del 1 al 10:** Usa un bucle `while` para imprimir los números del 1 al 10.

conta = -1

while conta < 10:
    conta += 1
    print(conta)


#2. **Sumar números del 1 al 10:** Usa un bucle `while` para sumar los números del 1 al 10 y mostrar el resultado.
conta = 1
const = 1
while conta < 10: 
    suma = conta + const
    conta += 1
    print(suma)
    
#3. **Imprimir elementos de una lista:** Dada una lista `["a", "b", "c"]`, imprime cada elemento usando un bucle `while`.

a = ['a', 'b', 'c', 'd']
b = ['e', 'f', 'g', 'h']
c = ['i', 'j', 'k', 'l']

comb = [a, b, c]
x = 0
y = 0

while y < len(comb):
    if x < len(comb[y]):
        print(comb[y][x])
        x += 1
    else:
        x = 0
        y += 1

    
"""
while x < len(comb):
    y = 0
    sub_comb = comb[x]
    print(comb[x])
    while y < len(comb[x]):
        print(sub_comb[y])
        y += 1
    x += 1
"""


#4. **Imprimir caracteres de una cadena:** Dada una cadena `"Python"`, imprime cada carácter usando un bucle `while`.

#5. **Imprimir números pares del 2 al 20:** Usa un bucle `while` para imprimir los números pares del 2 al 20.

### Ejercicios Intermedios

#6. **Sumar elementos de una lista:** Dada una lista de números `[1, 2, 3, 4, 5]`, suma todos sus elementos y muestra el resultado.

#7. **Contar elementos en una lista:** Dada una lista `["manzana", "banana", "cereza"]`, cuenta el número de elementos en la lista.

#8. **Imprimir los primeros n números naturales:** Dado un número `n`, imprime los primeros `n` números naturales.

# 9. **Imprimir una lista en orden inverso:** Dada una lista `["a", "b", "c"]`, imprime sus elementos en orden inverso.

#10. **Imprimir la tabla de multiplicar del 5:** Usa un bucle `while` para imprimir la tabla de multiplicar del 5.

### Ejercicios Avanzados

#11. **Imprimir números impares del 1 al 20:** Usa un bucle `while` para imprimir los números impares del 1 al 20.

#12. **Calcular el factorial de un número:** Dado un número `n`, calcula su factorial usando un bucle `while`.

#13. **Contar vocales en una cadena:** Dada una cadena, cuenta el número de vocales que contiene.

#14. **Encontrar el número máximo en una lista:** Dada una lista de números, encuentra el número máximo.

#15. **Generar una lista de cuadrados:** Dado un número `n`, genera una lista de los primeros `n` cuadrados perfectos.

#16. **Contar palabras en una frase:** Dada una frase, cuenta el número de palabras que contiene.

#17. **Imprimir los primeros n números de Fibonacci:** Dado un número `n`, imprime los primeros `n` números de la secuencia de Fibonacci.

#18. **Eliminar duplicados en una lista:** Dada una lista con elementos duplicados, crea una nueva lista sin duplicados.

#19. **Multiplicar elementos de dos listas:** Dadas dos listas del mismo tamaño, multiplica sus elementos correspondientes y muestra el resultado.

#20. **Sumar las diagonales de una matriz:** Dada una matriz cuadrada, suma los elementos de sus diagonales principal y secundaria.

### Ejercicios de Aplicación

#21. **Contar letras y dígitos en una cadena:** Dada una cadena, cuenta cuántas letras y cuántos dígitos contiene.

#22. **Convertir lista de Celsius a Fahrenheit:** Dada una lista de temperaturas en Celsius, convierte cada una a Fahrenheit.

#23. **Imprimir números primos en un rango:** Dado un rango de números, imprime todos los números primos dentro de ese rango.

#24. **Ordenar una lista:** Dada una lista de números, ordénala en orden ascendente usando un algoritmo de ordenación simple.

#25. **Calcular el promedio de una lista de números:** Dada una lista de números, calcula su promedio.

#26. **Concatenar listas:** Dadas dos listas, concaténalas en una sola lista.

#27. **Encontrar el segundo número más grande en una lista:** Dada una lista de números, encuentra el segundo número más grande.

#28. **Contar apariciones de cada elemento en una lista:** Dada una lista, cuenta cuántas veces aparece cada elemento.

#29. **Generar un patrón de asteriscos:** Usa bucles para generar un patrón de asteriscos, como un triángulo o un cuadrado.

#30. **Verificar si una cadena es un palíndromo:** Dada una cadena, verifica si es un palíndromo (se lee igual de adelante hacia atrás y viceversa).
