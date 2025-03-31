
# Escribe un algoritmo que calcule el factorial de un número positivo ingresado por consola.

num = int(input("Ingrese el número: "))
n_factoriado = 1

for i in range(1,num + 1):
    n_factoriado *= i

print (f"El número factoriado: {n_factoriado} ")
