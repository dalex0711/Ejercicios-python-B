
#  Pide al usuario que ingrese dos números positivos y muestra el mayor de ellos.

numero_uno = int(input("Ingrese el primer número positivo: "))
numero_dos = int(input("Ingrese un segundo número positivo: "))


if numero_uno < 0 or numero_dos <0:
    print ("Ingresaste un número negativo, intentalo nuevamente: ")

else:
    if numero_uno > numero_dos:
        print (f"El mayor de los número es: {numero_uno}")
    else:
        print (f"El mayor de los números es: {numero_dos}")        
