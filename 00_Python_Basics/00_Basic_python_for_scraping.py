############################# LISTS ##################################
#   Van entre square brackets, separados por comas
#   Para acceder a cada elemento, lista[posicion]
#   Tambien puede accederse desde atras [-1], -1 es el 0 del final
states = ["California", "Texas", "Florida", "Newyork"]
print(states[3])
print(states[-2])
print("\n") #Separacion de ejercicios


#   Para acceder a todos los elementos de la lista
#   for state in states:
#       print(state)
for state in states:
    print(state)
print("\n") #Separacion de ejercicios

#   Los condicionales es otra cosa que se utilizará
#   if state == "Florida":
#       print(state)


########################## EXPORT DATA ###############################
# PRIMERA FORMA
#   Muchas veces queremos el material en un documento txt, por lo que
#   tendremos que manejar ficheros. 
with open('test.txt', 'w') as file:
    file.write("Data successfully scraped!")

# SEGUNDA FORMA
#   Utilizaremos PANDAS en el siguiente fichero
