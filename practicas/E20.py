
#Pide al usuario un número entero y muestra si el número es divisible entre 5 (usar operador de módulo % y comparación).

numero_uno = int(input("Ingresa un número: "))
historial = []
historial.append(numero_uno)
numero_uno %= 5
historial.append(numero_uno)

resul = ((historial[1] == 0)  * ("El número {}, es divisible de 5".format(historial[0])) or 
         ((historial[1]!= 0))  * ("El número {}, es no divisible de 5".format(historial[0])) )

print (resul)


