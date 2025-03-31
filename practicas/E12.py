
# Pide al usuario su edad y muestra un mensaje que diga si su edad es mayor que 18 (usar operadores de comparación, sin condicionales).

num = int(input("Ingresa tu edad: "))

# depende de cual lado se cumpla (previo a 'or' o posterior), eso será lo que se almacenatá en la variable.
resultado = "tu edad indica que eres mayor edad." * (num >= 18) or "tu edad indica que eres menor de edad." * (num < 18) 


print (f"Tu edad es {num}, por ende {resultado}")



