import random
class Pokemon:
  def __init__(self, pokemon_1, pokemon_2, pokemon_3, pokemon_4, arma_1, arma_2, arma_3, arma_4, id, nombre, salud, lista_1,lista_2, arma):
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
       
    
        

  def pokemon_jugador(self):
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
        seleccion = print ('_El pokemon obtenido es el siguiente_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
        print(seleccion)
        
  def pokemon_maquina(self):
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
        seleccion_maquina = print ('_El pokemon obtenido es el siguiente_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
        print(seleccion_maquina)

  def menu(self):
      opcion = input('¿Quiere comenzar una partida (si/no):')
      if opcion == 'si':
          self.pokemon_jugador()
          self.pokemon_maquina()
          self.menu()
      elif opcion == 'no':
          print('Gracias por jugar')
      else:
          print('Opcion no valida')
          self.menu



print(Pokemon.menu('opcion'))
print( Pokemon.pokemon_jugador('seleccion'))
print(Pokemon.pokemon_maquina('seleccion_maquina'))