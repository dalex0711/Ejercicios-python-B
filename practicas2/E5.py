
# Solicita al usuario su nombre y apellido de forma separada, luego muestra un saludo personalizado donde se incluya el nombre y apellido ingresado. 

nombre   = input("Ingresa tu nombre: ")
apellido = input("Ingresa el apellido: ")

print (f"Hola, {nombre.title()} {apellido.title()}")