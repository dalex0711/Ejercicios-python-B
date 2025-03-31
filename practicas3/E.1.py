# Dada tupla donde contiene el nombre, apellido de una persona y su edad. 
# Escribe un programa que recorra la lista usando un ciclo for. 
# Si la edad de la persona es menor de 18 años, omítela utilizando continue. 
# Si la edad es mayor de 60, detén el ciclo utilizando break y muestra un mensaje indicando que se encontró una persona mayor de 60 años


datos = [
    ("Dal", "sajunan", "20"),
    ("jose", "olas", "60"),
    ("jose", "olas", "61")]


for nombre, apellido, edad in datos:

    edad = int(edad)

    if edad < 18:
        continue  
    
    if edad > 60:

        print(f"{nombre} {apellido},tiene más de 60 años. Tiene {edad} años")
        break 

   
