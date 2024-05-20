"""¡Por supuesto! Aquí tienes otros 20 ejercicios
para practicar el uso del rango `range(start, stop, step)`
en Python:"""


#----------------------------------------------------------------------------------

"""

# 1. Imprimir los números del 1 al 10.

def print_1_10(num1, num2):
    for i in range(num1,num2 + 1):
        print(i)

print_1_10(1,10)

# 2. Imprimir los números del 5 al 15.

def print_5_15(num1, num2):
    for i in range(num1,num2 + 1):
        print(i)

print_5_15(5,15)

# 3. Imprimir los números pares del 2 al 10.

def print_par_2_10(num1,num2):
    for i in range(num1, num2 + 1,2):
        print(i)

print_par_2_10(2,10)

# 4. Imprimir los números impares del 1 al 9.

def print_imp_1_9(num1,num2):
    for i in range(num1,num2 +1,2):
        print(i)

print_imp_1_9(1,9)

# 5. Imprimir los números del 10 al 1 en orden descendente.

def print_10_1_des(num1,num2):
    for i in range(num1,num2 -1 ,-1):
        print(i)

print_10_1_des(num2=1,num1=10)

# 6. Imprimir los números del 20 al 0 en decrementos de 2.

def print_20_0_des(num1,num2):
    for i in range(num1,num2 -1 ,-2):
        print(i)

print_20_0_des(num2=0,num1=20)

# 7. Imprimir los números múltiplos de 5 del 0 al 25.

def mult_5_0_25(mult, rang_1, rang_2):
    for i in range(rang_1, rang_2+1):
        if i % mult == 0:
            print(i)

mult_5_0_25(5,0,25)

# 8. Imprimir los números del 100 al 200 en incrementos de 10.

def mult_5_0_25(rang_1, rang_2, incre):
    for i in range(rang_1, rang_2+1, incre):
        print(i)

mult_5_0_25(100,200,10)

# 9. Imprimir los números del -5 al 5.

def impri_nega_m5_5(rang_a, rang_b, incre):
    for i in range(rang_a, rang_b + 1 , incre):
        print(i)

impri_nega_m5_5(-5,5,1)

# 10. Imprimir los números del -10 al 10 en incrementos de 2.

def impri_nega_m10_10_2(rang_a, rang_b, incre):
    for i in range(rang_a, rang_b + 1 , incre):
        print(i)

impri_nega_m10_10_2(-10,10,2)

# 11. Imprimir los números del 5 al 50 en incrementos de 5.

def impri_5_50_5(rang_a, rang_b, incre):
    for i in range(rang_a, rang_b + 1 , incre):
        print(i)

impri_5_50_5(5,50,5)

# 12. Imprimir los números del -10 al 0 en orden descendente.

def impri_m10_0(num_1,num_2,incre):
    for i in range(num_1,num_2-1,incre):
        print(i)

impri_m10_0(0,-10,-1)

# 13. Imprimir los números impares del 1 al 10 en orden descendente.

def impar_num_1_10(num_1,num_2,incre):
    for i in range(num_1,num_2+1,incre):
        print(i)

impar_num_1_10(1,10,2)

# 14. Imprimir los números múltiplos de 3 del 30 al 0 en orden descendente.

def multi_3_30_0(num_1,num_2,incre):
    for i in range(num_1, num_2+1, incre):
        print(i)

multi_3_30_0(3,30,3)

# 15. Imprimir los números del 1 al 10, saltando de 3 en 3.

def impri_1_10_3(num_1, num_2, incre):
    for i in range(num_1, num_2+1, incre):
        print(i)

impri_1_10_3(1,10,3)

# 16. Imprimir los números del 10 al 1 en decrementos de 3.

def impri_10_1_3(num_1,num_2,incre):
    for i in range(num_1,num_2-1,incre):
        print(i)

impri_10_1_3(10,1,-3)

# 17. Imprimir los números del 0 al 100, omitiendo los múltiplos de 7.

def impri_0_100_om7(num_1,num_2,incre):
    for i in range(num_1,num_2+1,incre):
        if i % 7 != 0:
            print(i)
impri_0_100_om7(0,100,1)

# 18. Imprimir los números del 100 al 0 en decrementos de 7.

def impri_100_0_de_7(num_1,num_2,incre):
    for i in range(num_1,num_2-1,incre):
        print(i)

impri_100_0_de_7(100,0,-7)

# 19. Imprimir los números impares del 15 al 35.

def impri_15_35(num_1,num_2,incre):
    for i in range(num_1,num_2+1,incre):
        print(i)

impri_15_35(15,35,2)

# 20. Imprimir los números pares del 50 al 20 en orden descendente.

def impri_50_20_des_par(num_1,num_2,incre):
    for i in range(num_1, num_2-1, incre):
        print(i)

impri_50_20_des_par(50,20,-1)

# 21. Imprimir los números del 15 al 45, omitiendo los múltiplos de 2 y los números que contienen el dígito 4.

def impri_15_45_om2__om4(num_1,num_2,incre):
    for i in range(num_1, num_2+1, incre):
        if i % 2 != 0 and '4' not in str(i) :
                print(i)

impri_15_45_om2__om4(5,45,1)

# 22. Imprimir los números del 1 al 50, omitiendo los múltiplos de 5.

def impr_1_50_om5(num_1,num_2,incre):
    for i in range(num_1, num_2+2, incre):
        if i % 5 != 0:
            print(i)

impr_1_50_om5(1,50,1)

# 23. Imprimir los números del 10 al 30, omitiendo los números que contienen el dígito 2.

def imp_10_30_om2dig(num_1, num_2,incre):
    for i in range(num_1,num_2+1,incre):
        if '2' not in str(i):
            print(i)

imp_10_30_om2dig(10,30,1)

#24. Imprimir los números del 50 al 100, omitiendo los múltiplos de 9.

def impr_50_100_mulom9(num_1, num_2, incre):
    for i in range(num_1, num_2+1, incre):
        if i % 9 != 0:
            print(i)
impr_50_100_mulom9(50,100,1)

#25. Imprimir los números del 0 al 20, omitiendo los múltiplos de 3 y los números que contienen el dígito 1.

def impri_0_20_mul3om_dig1om(num_1, num_2, incre):
    for i in range(num_1, num_2+1, incre):
        if i % 3 != 0 and '1' not in str(i):
            print(i)

impri_0_20_mul3om_dig1om(0,20,1)

# 26. Imprimir los números del 100 al 200, omitiendo los números que son múltiplos de 4 y terminan en 5.

def impri(num_1, num_2, incre):
    for i in range(num_1, num_2+1, incre):
        if i % 4 != 0 and str(i)[-1] != 5:
            print(i)

impri(100,200,1)

# 27. Imprimir los números del 1 al 100, omitiendo los múltiplos de 6 y los números que contienen el dígito 9.

def impr_1_100_om6mul_om9digi(num_1,num_2,incre):
    for i in range(num_1, num_2 + 1, incre):
        if i % 6 != 0 and '9' not in str(i):
            print(i)
impr_1_100_om6mul_om9digi(1,100,1)

# 28. Imprimir los números del 30 al 60, omitiendo los múltiplos de 8 y los números que 

terminan en 0.
def impri_30_60_om8mul_om0and(num_1,num_2,incre):
    for i in range(num_1, num_2 + 1, incre):
        if i % 8 != 0 and '0' != str(i)[-1]:
            print(i)

impri_30_60_om8mul_om0and(30,60,1)


# 29. Imprimir los números del 0 al 100, omitiendo los números que contienen los dígitos 3, 7 , 13, 17, 34 o 59.

def impri(num_1, num_2, incre, digitos):
    for i in range(num_1, num_2 + 1, incre):
        if all( str(d) not in str(i) for d in digitos):
            print(i)
impri(0,100,1, digitos=[3, 7 , 13, 17, 34, 59])
