
# Retornará el tipo de dato ingresado (Int, Float, String)
dato = input("Ingresa el dato: ")

if dato.isdigit(): 
    if int(dato):
        print("Es entero")        

elif "." in dato:
    parte_decimal = dato.split(".")[1]

    if parte_decimal.isdigit():
        print("Es un número decimal.")

    else:
        print("Es un String")

else:
    print("Es un String")

