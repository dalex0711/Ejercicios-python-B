#Crea un programa que reciba una lista de números enteros y utilice un ciclo while para recorrerlos.
#  Si se encuentra un número negativo, se debe imprimir un mensaje y detener el ciclo utilizando la instrucción break.
#  Si el número es mayor que 100, se debe continuar con el siguiente número utilizando continue. 
# Al final, debe imprimir la cantidad de números procesados que son mayores que 50.





lista = []


cantidad_numeros = int(input("Cuantos números desea ingresar: "))

for i in range (1, cantidad_numeros +1):
    numeros = int(input("Ingrese un número entero: "))
    lista.append(numeros)       

x = 0
numeros_mayores = []
cantidad_numeros = 0
while x < (len(lista)):

    if lista[x] < 0:
        print("El número es negativo")

        break

    elif lista[x] > 100:

        continue

    elif lista[x] > 50 :
        numeros_mayores.append(lista[x])
        cantidad_numeros += 1
    
    x += 1

if cantidad_numeros > 0:

    print(f"La cantidad de números mayores a 50 son: {cantidad_numeros}: {numeros_mayores}")


     



