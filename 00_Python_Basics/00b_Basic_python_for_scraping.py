import pandas as pd

states = ["California", "Texas", "Florida", "Newyork"]
population = [111111, 222222, 3333333, 4444444]

####################### DICTIONARY ########################
# Hay que utilizar llaves o curly braces
# Se forman, con el diccionario = {'key1':value1, 'key2':value2}
# Las keys no pueden ser iguales y dentro de los valores podemos meter
# sin problemas listas o valores individuales

dict_states = {'States':states, 'Population':population}

# Ahora crearemos el DATAFRAME
df_states = pd.DataFrame.from_dict(dict_states)
#print(df_states)

# Podemos exportar a una hoja CSV
df_states.to_csv('states.csv', index=False) #Para que no aparezcan indices