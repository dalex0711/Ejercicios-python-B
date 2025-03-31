
# Escribe un programa que pida un número al usuario y determine si ese número está entre 10 y 20 (inclusive). 
# Si está dentro del rango, imprime "El número está en el rango". Si no está en el rango, imprime "El número no está en el rango".

numero_uno = float(input("Ingrese un número: "))

if numero_uno >= 10 or numero_uno <=20: 
    print("El número está en el rango")

else: 
    print("El número no está en el rango")