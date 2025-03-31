
# Escribe un programa que utilice un ciclo for para sumar los números impares entre 1 ny 100. Luego, imprime el resultado de la suma.

suma = 0


for i in range (100):
    if i % 2 != 0:
        suma += i
print(f"La suma de los números impares es: {suma}") 




