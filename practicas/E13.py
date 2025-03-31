
#Pide al usuario dos números enteros y muestra si son iguales (usar operadores de comparación, sin condicionales).

numero_uno = int(input("Ingresa un número: "))
numero_dos = int(input("Ingresa un número: "))

resultado = "iguales" * (numero_uno == numero_dos) or "diferentes" * (numero_uno != numero_dos)
print(f"Tu primer número {numero_uno} y segundo {numero_dos} son {resultado}") 