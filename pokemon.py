import random

class pokemon():
    def __init__(self,Venusaur, Charmander, Bulbasaur, Squirtle,id,puñetazo,patada,codazo,cabezazo,salud,ataque,defensa):
        self.Venusaur = Venusaur
        self.Charmander = Charmander
        self.Bulbasaur = Bulbasaur
        self.Squirtle = Squirtle
        self.id = id
        self.puñetazo = puñetazo
        self.patada = patada
        self.codazo= codazo 
        self.cabezazo = cabezazo
        self.salud = salud 
        self.ataque = ataque
        self.defensa = defensa

    def definir_pokemon(self):
        Venusaur = 'pokemon_1'
        pokemon_2 = self.Charmander
        pokemon_3 = self.Bulbasaur
        pokemon_4 = self.Squirtle
        arma_1 = self.puñetazo
        arma_2 = self.patada
        arma_3 = self.codazo
        arma_4 = self.cabezazo
        lista_2 = [arma_1, arma_2, arma_3, arma_4]
        lista= [pokemon_1,pokemon_2,pokemon_3,pokemon_4]
        nombre = random.choice(lista)
        id = random.randint(1,100)
        arma= random.choice(lista_2)
        salud = random.randint(1,100)
        print('Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))

