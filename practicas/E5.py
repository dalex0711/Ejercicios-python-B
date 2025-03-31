
"""Pide al usuario una palabra y un número entero. Muestra la palabra repetida ese número de veces. """

palabra = input("Ingresa una palabra: ")
numero = int(input("Ingresa el número que la palabra se repetirá: "))

repeticion = " \n".join([palabra] * numero) # El join es  un metodo que nos va a permitir manipular los string. 
                                            # En este caso hacer un salto de linea en cada repeit de palabra
print(repeticion)

"""for i in range (numero):
    
    print(palabra * 1) """
