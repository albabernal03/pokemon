import random
pokemon_1 = 'Venausaur'
pokemon_2 = 'Charmander'
pokemon_3 = 'Bulbasaur'
pokemon_4 = 'Squirtle'
arma_1 = 'puñetazo'
arma_2 = 'patada'
arma_3 = 'codazo'
arma_4 ='cabezazo'
lista_1 = [pokemon_1, pokemon_2, pokemon_3, pokemon_4]
lista_2 = [arma_1, arma_2, arma_3, arma_4]
nombre = random.choice(lista_1)
id = random.randint(1,100)
salud = random.randint(1,100)
arma = random.choice(lista_2)
seleccion_1= print('Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
seleccion_2 = print('Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))



#print(pokemon.definir_pokemon('pokemon_1', 'pokemon_2', 'pokemon_3', 'pokemon_4', 'arma_1', 'arma_2', 'arma_3', 'arma_4', 'lista_1', 'lista_2', 'nombre', 'id', 'salud', 'arma'))
