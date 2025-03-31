
#  Pide al usuario dos números y muestra si al menos uno es mayor que 10 (usar operador lógico or).

numero_uno = int(input("Ingresa un número: "))
numero_dos = int(input("Ingresa un número: "))
resultado  = ("Solo el {} es mayor que 10".format(numero_uno,numero_dos) * (numero_uno or numero_dos > 10)) 