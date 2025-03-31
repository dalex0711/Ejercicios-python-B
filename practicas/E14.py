
#Pide dos números y muestra si el primero es mayor que el segundo (usar operador de comparación).

numero_uno = int(input("Ingresa un número: "))
numero_dos = int(input("Ingresa un número: "))
resultado = ( "El {} es mayor que el {}".format(numero_uno,numero_dos) * (numero_uno > numero_dos) or
              "El {} es mayor que el {}".format(numero_uno,numero_dos) * (numero_dos>numero_uno))

print (resultado)