
#Pide al usuario dos números y muestra si ambos son mayores que 10 (usar operador lógico and).

numero_uno = int(input("Ingresa un número: "))
numero_dos = int(input("Ingresa un número: "))
resultado = ( "Los números ({},{}) son mayores que 10".format(numero_uno,numero_dos) * (numero_uno and numero_dos > 10 ) or
              "Los números ({},{}) son menores que 10".format(numero_uno,numero_dos) * (numero_uno and numero_dos < 10 ))

print (resultado)