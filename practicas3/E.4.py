# Escribe un programa que utilice un ciclo for para iterar desde 1 hasta 200.
# Si el número es múltiplo de 4, debe saltar a la siguiente iteración usando continue. 
# Si el número es mayor que 150, debe detener el ciclo inmediatamente usando break. 
# Imprime todos los números que no sean múltiplos de 4 y sean menores o iguales a 150.



menor_igual_150 = []
no_multiplos = []
for i in range (1, 200 +1):

    if i % 4 == 0:
     
     continue
    no_multiplos.append(i)    
   
    if i < 150:
       menor_igual_150.append(i)
       if i > 150:
         break
       

print(f"Menores de 150: {menor_igual_150}")

print (f"\nNo_multiplos {no_multiplos}")

