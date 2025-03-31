
# Calculadora basica (suma,resta,multi,division)


numero_uno = float(input("Ingrese un número: "))
numero_dos = float(input("Ingrese un segundo número: "))

if numero_dos != 0:
    suma = int(numero_uno + numero_dos)
    resta = int(numero_uno - numero_dos)
    x =  int(numero_uno * numero_dos)
    div = numero_uno / numero_dos
    print (f"\033[1m---LOS RESULTADOS SON---\033[0m \nSuma:{suma} \nResta:{resta} \nMultiplicación:{x} \nDivisión:{div}")


else:
    suma = int(numero_uno + numero_dos)
    resta = int(numero_uno - numero_dos)
    x =  int(numero_uno * numero_dos)
    div = "No es posible dividir entre 0"
    
    print (f"\033[1m---LOS RESULTADOS SON---\033[0m\nSuma:{suma} \nResta:{resta} \nMultiplicación:{x} \nDivisión:{div}")

    
    
