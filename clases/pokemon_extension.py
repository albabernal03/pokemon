import random
class Pokemon2:
    def __init__(self, pokemon_tierra_1, pokemon_tierra_2, pokemon_tierra_3, pokemon_agua_1,pokemon_agua_2, pokemon_agua_3, pokemon_aire_1, pokemon_aire_2, pokemon_aire_3, pokemon_electricidad_1, pokemon_electricidad_2, pokemon_electricidad_3, arma_1, arma_2, arma_3, arma_4, id, nombre, salud, lista_1,lista_2, arma):
        self.pokemon_tierra_1 = pokemon_tierra_1
        self.pokemon_tierra_2 = pokemon_tierra_2
        self.pokemon_tierra_3 = pokemon_tierra_3
        self.pokemon_agua_1 = pokemon_agua_1
        self.pokemon_agua_2 = pokemon_agua_2
        self.pokemon_agua_3 = pokemon_agua_3
        self.pokemon_aire_1 = pokemon_aire_1
        self.pokemon_aire_2 = pokemon_aire_2
        self.pokemon_aire_3 = pokemon_aire_3
        self.pokemon_electricidad_1 = pokemon_electricidad_1
        self.pokemon_electricidad_2 = pokemon_electricidad_2
        self.pokemon_electricidad_3 = pokemon_electricidad_3
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
        pokemon_tierra_1 = 'Geodude'
        pokemon_tierra_2 = 'Golem'
        pokemon_tierra_3 = 'Onix'
        pokemon_agua_1 = 'Sqirtle'
        pokemon_agua_2 = 'Psyduck'
        pokemon_agua_3 = 'Poliwag'
        pokemon_aire_1 = 'Charizard'
        pokemon_aire_2 = 'Butterfree'
        pokemon_aire_3 = 'Pidgey'
        pokemon_electricidad_1 = 'Pikachu'
        pokemon_electricidad_2 = 'Raichu'
        pokemon_electricidad_3 = 'Magneton'
        arma_1 = 'puñetazo'
        arma_2 = 'patada'
        arma_3 = 'codazo'
        arma_4 ='cabezazo'
        lista_tierra = [pokemon_tierra_1, pokemon_tierra_2, pokemon_tierra_3]
        lista_agua = [pokemon_agua_1, pokemon_agua_2, pokemon_agua_3]
        lista_aire = [pokemon_aire_1, pokemon_aire_2, pokemon_aire_3]
        lista_electricidad = [pokemon_electricidad_1, pokemon_electricidad_2, pokemon_electricidad_3]
        lista_2 = [arma_1, arma_2, arma_3, arma_4]
        nombre_tierra = random.choice(lista_tierra)
        nombre_agua = random.choice(lista_agua)
        nombre_aire = random.choice(lista_aire)
        nombre_electricidad = random.choice(lista_electricidad)
        id = random.randint(1,100)
        arma = random.choice(lista_2)
        salud = random.randint(1,100)

        seleccion_jugador = input('¿Que tipo de pokemon quieres? (tierra/agua/aire/electricidad):')

        if seleccion_jugador == 'tierra':
            print('//TIPO: TIERRA//')
            print('_El pokemon obtenido es el siguiente_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre_tierra), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
        
        elif seleccion_jugador == 'agua':
            print('//TIPO: AGUA//')
            print('_El pokemon obtenido es el siguiente_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre_agua), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
           
        elif seleccion_jugador == 'aire':
            print('//TIPO:AIRE//')
            print('_El pokemon obtenido es el siguiente_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre_aire), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
            
        elif seleccion_jugador == 'electricidad':
            print('//TIPO: ELECTRICIDAD//')
            print('_El pokemon obtenido es el siguiente_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre_electricidad), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))

    def pokemon_maquina(self):
        pokemon_tierra_1 = 'Geodude'
        pokemon_tierra_2 = 'Golem'
        pokemon_tierra_3 = 'Onix'
        pokemon_agua_1 = 'Sqirtle'
        pokemon_agua_2 = 'Psyduck'
        pokemon_agua_3 = 'Poliwag'
        pokemon_aire_1 = 'Charizard'
        pokemon_aire_2 = 'Butterfree'
        pokemon_aire_3 = 'Pidgey'
        pokemon_electricidad_1 = 'Pikachu'
        pokemon_electricidad_2 = 'Raichu'
        pokemon_electricidad_3 = 'Magneton'
        arma_1 = 'puñetazo'
        arma_2 = 'patada'
        arma_3 = 'codazo'
        arma_4 ='cabezazo'
        lista_tierra = [pokemon_tierra_1, pokemon_tierra_2, pokemon_tierra_3]
        lista_agua = [pokemon_agua_1, pokemon_agua_2, pokemon_agua_3]
        lista_aire = [pokemon_aire_1, pokemon_aire_2, pokemon_aire_3]
        lista_electricidad = [pokemon_electricidad_1, pokemon_electricidad_2, pokemon_electricidad_3]
        nombre_tierra = random.choice(lista_tierra)
        nombre_agua = random.choice(lista_agua)
        nombre_aire = random.choice(lista_aire)
        nombre_electricidad = random.choice(lista_electricidad)
        lista_2 = [arma_1, arma_2, arma_3, arma_4]
        id = random.randint(1,100)
        arma = random.choice(lista_2)
        salud = random.randint(1,100)
        seleccion_maquina = random.randint(1,4)

        if seleccion_maquina == 1:
            print('//TIPO: TIERRA//')
            print('_El pokemon al que se enfrenta_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre_tierra), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
        
        elif seleccion_maquina == 2:
            print('//TIPO: AGUA//')
            print('_El pokemon al que se enfrenta_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre_agua), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
           
        elif seleccion_maquina == 3:
            print('//TIPO: AIRE//')
            print('_El pokemon al que se enfrenta_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre_aire), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
            
        elif seleccion_maquina == 4:
            print('//TIPO: ELECTRICIDAD//')
            print('_El pokemon obtenido al que se enfrenta_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre_electricidad), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))



    def menu(self):
        opcion = input('¿Quiere comenzar una partida (si/no):')
        if opcion == 'si':
            Pokemon2.pokemon_jugador('seleccion_jugador')
            Pokemon2.pokemon_maquina('seleccion_maquina')
            self.menu()
        elif opcion == 'no':
            print('Gracias por jugar')
        else: 
            print('Opcion no valida')
            self.menu()

print(Pokemon2.menu('opcion'))
print(Pokemon2.pokemon_jugador('seleccion_jugador'))
print(Pokemon2.pokemon_maquina('seleccion_maquina'))
