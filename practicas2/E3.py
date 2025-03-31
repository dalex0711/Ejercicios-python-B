
# Pide al usuario un número y muestra si es par o impar, además de indicar si el número es mayor que 10.


numero_uno = int(input("Ingrese un número: "))
mod = numero_uno % 2

if mod == 0:
    print ("El número es par.")
    if numero_uno > 10:
        print ("El número es mayor a 10.")
    else:
        print ("EL número es menor a 10.")    

else:
    print ("El número es impar")
    if numero_uno > 10:
        print ("El número es mayor a 10.")
    else:
        print ("EL número es menor a 10.")   

