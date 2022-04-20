<h1 align="center">	⚡Pokemons⚡</h1>

***
<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/pokemon)

***
<h2>¿De qué trata esta tarea?</h2>

En esta tarea se nos pide que desarrollemos un programa parecido al juego de los pokemons, donde cada uno tiene asignado un id, nombre, salud y arma. En este juego encontramos dos jugadores, uno que somos nosotros y otro que es el ordenador; cada uno tendrá asignado una arma y salud aleatoria, al igual que el resto de variables y ambos pokemons deberán efrentarse hasta que uno de los dos salga victorioso.

Por otro lado luego se nos pide una ampliacion de este, en el que encontramos cuatro tipo de pokemon: tierra, agua, aire y electricidad. Lo último que varia en este caso es el índice de defensa asignado dependiendo el tipo.

***

## Índice
1. Clase Pokemon
2. Clase Ataque
3. Clase extension_pokemon
4. Clase estension_ataque

***

## Clase Pokemon

**Código**

```
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
        seleccion = print ('El pokemon obtenido es el siguiente_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
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
        seleccion_maquina = print ('_Pokemon al que se enfrenta_:''Pokemon ID', '{}'.format(id), 'con nombre', '{}'.format(nombre), 'tiene arma', '{}'.format(arma), 'y salud', '{}'.format(salud))
        print(seleccion_maquina)

    def menu(self):
        opcion = input('¿Quiere comenzar una partida (si/no):')
        if opcion == 'si':
            Pokemon.pokemon_jugador('seleccion')
            Pokemon.pokemon_maquina('seleccion_maquina')
            self.menu()
        elif opcion == 'no':
            print('Gracias por jugar')
        else: 
            print('Opcion no valida')
            self.menu()
    
print(Pokemon.menu('opcion'))
print( Pokemon.pokemon_jugador('seleccion'))
print(Pokemon.pokemon_maquina('seleccion_maquina'))
```
***

## Clase Ataque

**Código**
