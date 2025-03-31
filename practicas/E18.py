
#Pide al usuario dos números y muestra si el primero NO es igual al segundo (usar operador lógico not combinado con comparación).

numero_uno = int(input("Ingresa un número: "))
numero_dos = int(input("Ingresa un número: "))

resul = ("Número {} es diferente del {}".format(numero_uno,numero_dos) * (not (numero_uno == numero_dos)) or
         "Número {} es igual que {}".format(numero_uno,numero_dos) * (numero_uno == numero_dos))

print(resul)