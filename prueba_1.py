import random

class pokemon:
  def __init__(self, pokemon_1, pokemon_2, pokemon_3, pokemon_4, arma_1, arma_2, arma_3, arma_4, id, nombre, salud, lista_1,lista_2, arma, seleccion):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.pokemon_3 = pokemon_3
        self.pokemon_4 = pokemon_4
        self.arma_1 = arma_1
        self.arma_2 = arma_2
        self.arma_3 = arma_3
        self.arma_4 = arma_4
        self.salud = salud
        self.id = id
        self.nombre = nombre
        self.lista_1 = lista_1
        self.lista_2 = lista_2
        self.arma= arma
        self.seleccion = seleccion
        

  def definir_pokemon(self):
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
        arma = random.choice(lista_2)
        salud = random.randint(1,100)
     

        seleccion= print('Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
        print(seleccion)

pokemon.definir_pokemon('seleccion')





