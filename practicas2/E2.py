
# Escribe un programa que pida al usuario una calificación (número entre 0 y 10).
# Luego, categoriza las calificaciones según el siguiente rango:
# Las calificaciones 9 a 10 se asociarán a la letra A, las calificaciones del 7 a 8.9 se asociarán a la letra B,
# las calificaciones del 5 a 6.9 quedarán asociadas a la letra C y por último si la calificación es menor a 5 se le asignará la letra F.


numero_uno = float(input("Ingrese su calificación: "))

if ((round(numero_uno) >= 9.0) and round(numero_uno) <= 10.0):
    print (f"--- \033[1mRESULTADO\033[0m ---\nTU CALIFICACIÓN:\033[1m A \033[0m \nTU NOTA: {numero_uno}")

elif ((round(numero_uno) >= 7.0) and round(numero_uno) <= 8.9):
     print (f"--- \033[1mRESULTADO\033[0m ---\nTU CALIFICACIÓN:\033[1m A \033[0m \nTU NOTA: {numero_uno}")

elif ((round(numero_uno) > 5.0) and round(numero_uno) <= 6.9):
     print (f"--- \033[1mRESULTADO\033[0m ---\nTU CALIFICACIÓN:\033[1m A \033[0m \nTU NOTA: {numero_uno}")

elif ((round(numero_uno) > 0) and round(numero_uno) <= 5):
     print (f"--- \033[1mRESULTADO\033[0m ---\nTU CALIFICACIÓN:\033[1m A \033[0m \nTU NOTA: {numero_uno}")

else: 
    print ("INGRESA UNA CALIFICACIÓN VALIDA (ENTRE 0 - 10)")    