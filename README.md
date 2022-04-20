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
1. [Clase Pokemon](#id1)
2. [Clase Ataque](#id2)
3. [Clase Pokemon2](#id3)
4. [Clase Ataque2](#id4)

***

## Clase Pokemon:<a name="id1"></a>

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

**UML:**

***

## Clase Ataque:<a name="id2"></a>

**Código**

```
from clases.pokemon import Pokemon
import random 

class Ataque:
    def __init__(self, defensa_jugador, defensa_maquina, pokemon_jugador, pokemon_maquina):
        self.pokemon_jugador = pokemon_jugador
        self.pokemon_maquina = pokemon_maquina
        self.defensa_jugador = defensa_jugador
        self.defensa_maquina = defensa_maquina
    
    def partida(self):
        pokemon_jugador = Pokemon.pokemon_jugador()
        pokemon_maquina = Pokemon.pokemon_maquina()
        turno = random.randint(1,2)
        defensa_jugador = random.randint(1,10)
        defensa_maquina = random.randint(1,10)
        while pokemon_jugador.salud > 0 and pokemon_maquina.salud > 0: 
            if turno == 1 and Ataque.ataque_jugador > defensa_maquina:
                Ataque.ataque_jugador(pokemon_jugador, pokemon_maquina)
                print()
                print (f'{pokemon_jugador.nombre} ataca, {pokemon_maquina.nombre} ahora tiene {pokemon_maquina.salud} de salud')
                print('==PRÓXIMA RONDA==')
                
            elif turno == 1 and Ataque.ataque_jugador < defensa_maquina:
                print('No se ha podido realiza el ataque')
                print('==PRÓXIMA RONDA==')
                
            elif turno == 2 and Ataque.ataque_maquina > defensa_jugador:
                Ataque.ataque_maquina(pokemon_maquina, pokemon_jugador)
                print()
                print(f'{pokemon_maquina.nombre} ataca, {pokemon_jugador.nombre} ahora tiene {pokemon_jugador.salud} de salud')
                print('==PRÓXIMA RONDA==')
            elif turno == 2 and Ataque.ataque_maquina < defensa_jugador:
                print('No se pudo realizar el ataque')
                print('==PRÓXIMA RONDA==')
            
        if pokemon_maquina.salud <= 0:
            print(f'{pokemon_jugador.nombre} gana la partida contra {pokemon_maquina.nombre}')
        else:
             print(f'{pokemon_maquina.nombre} gana la partida contra {pokemon_jugador.nombre}') 
             
    def ataque_jugador(pokemon_jugador, pokemon_maquina):
        if pokemon_jugador.arma == 'puñetazo':
            pokemon_maquina.salud == pokemon_maquina.salud - 5
        elif pokemon_jugador.arma == 'patada':
            pokemon_maquina.salud == pokemon_maquina.salud - 3
        elif pokemon_jugador.arma == 'codazo':
            pokemon_maquina.salud == pokemon_maquina.salud - 3
        elif pokemon_jugador.arma == 'cabezazo':
            pokemon_maquina.salud == pokemon_maquina.salud - 2
        else:
            print('No se ha podido realizar el ataque')

    def ataque_maquina(pokemon_maquina, pokemon_jugador):
        if pokemon_maquina.arma == 'puñetazo':
            pokemon_jugador.salud == pokemon_jugador.salud - 5
        elif pokemon_maquina.arma == 'patada':
            pokemon_jugador.salud == pokemon_jugador.salud - 3
        elif pokemon_maquina.arma == 'codazo':
            pokemon_jugador.salud == pokemon_jugador.salud - 3
        elif pokemon_maquina.arma == 'cabezazo':
            pokemon_jugador.salud == pokemon_jugador.salud - 4
        else:
            print('No se ha podido realizar el ataque')
        
#Funcion que verifica el estado del pokemon del jugador 
    def is_alive(pokemon_jugador):
        if pokemon_jugador.salud <= 0:
            return False
        else:
            return True

#Funcion que verifica el estado del pokemon de la maquina
    def is_alive(pokemon_maquina):
        if pokemon_maquina.salud <= 0:
            return False
        else:
            return True

```
**UML:**


***

## Clase Pokemon2:<a name="id3"></a>

**Código**

```
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

```

**UML:**


***

## Clase Ataque2:<a name="id4"></a>

**Código**

```
from clases.extension_pokemon import Pokemon2
import random 

class Ataque2:
    def __init__(self, defensa_jugador, defensa_maquina, pokemon_jugador, pokemon_maquina):
            self.pokemon_jugador = pokemon_jugador
            self.pokemon_maquina = pokemon_maquina
            self.defensa_jugador = defensa_jugador
            self.defensa_maquina = defensa_maquina

    def partida(self):
        pokemon_jugador = Pokemon2.pokemon_jugador()
        pokemon_maquina = Pokemon2.pokemon_maquina()
        turno = random.randint(1,2)
        if pokemon_jugador.seleccion_jugador == 'tierra' or 'agua':
            defensa_jugador = random.randint(11,20)
        elif pokemon_jugador.selecciom_jugador == 'aire' or 'electricidad':
            x = random.randint(1,2)
        if x == 1:
            defensa_jugador = random.randint(11,20)*2
        else:
            defensa_jugador = random.randint(11,20)
        
        if pokemon_maquina.seleccion_maquina == 1 or 2:
            defensa_maquina = random.randint(11,22)
        
        elif pokemon_jugador.selecciom_jugador == 3 or 4:
            x = random.randint(1,2)
        if x == 1:
            defensa_jugador = random.randint(11,20)*2
        else:
            defensa_jugador = random.randint(11,20)

        while pokemon_jugador.salud > 0 and pokemon_maquina.salud > 0: 
            if turno == 1 and Ataque2.ataque_jugador > defensa_maquina:
                Ataque2.ataque_jugador(pokemon_jugador, pokemon_maquina)
                print()
                print (f'{pokemon_jugador.nombre} ataca, {pokemon_maquina.nombre} ahora tiene {pokemon_maquina.salud} de salud')
                print('==PRÓXIMA RONDA==')
            elif turno == 1 and Ataque2.ataque_jugador < defensa_maquina:
                print('No se ha podido realiza el ataque')
                print('==PRÓXIMA RONDA==')
            elif turno == 2 and Ataque2.ataque_maquina > defensa_jugador:
                Ataque2.ataque_maquina(pokemon_maquina, pokemon_jugador)
                print()
                print(f'{pokemon_maquina.nombre} ataca, {pokemon_jugador.nombre} ahora tiene {pokemon_jugador.salud} de salud')
                print('==PRÓXIMA RONDA==')
            elif turno == 2 and Ataque2.ataque_maquina < defensa_jugador:
                print('No se pudo realizar el ataque')
                print('==PRÓXIMA RONDA==')
            
        if pokemon_maquina.salud <= 0:
            print(f'{pokemon_jugador.nombre} gana la partida contra {pokemon_maquina.nombre}')
        else:
            print(f'{pokemon_maquina.nombre} gana la partida contra {pokemon_jugador.nombre}') 


    def ataque_jugador(pokemon_jugador, pokemon_maquina):
        if pokemon_jugador.arma == 'puñetazo':
            pokemon_maquina.salud == pokemon_maquina.salud - 5
        elif pokemon_jugador.arma == 'patada':
            pokemon_maquina.salud == pokemon_maquina.salud - 3
        elif pokemon_jugador.arma == 'codazo':
            pokemon_maquina.salud == pokemon_maquina.salud - 3
        elif pokemon_jugador.arma == 'cabezazo':
            pokemon_maquina.salud == pokemon_maquina.salud - 2
        else:
            print('No se ha podido realizar el ataque')

    def ataque_maquina(pokemon_maquina, pokemon_jugador):
        if pokemon_maquina.arma == 'puñetazo':
            pokemon_jugador.salud == pokemon_jugador.salud - 5
        elif pokemon_maquina.arma == 'patada':
            pokemon_jugador.salud == pokemon_jugador.salud - 3
        elif pokemon_maquina.arma == 'codazo':
            pokemon_jugador.salud == pokemon_jugador.salud - 3
        elif pokemon_maquina.arma == 'cabezazo':
            pokemon_jugador.salud == pokemon_jugador.salud - 4
        else:
            print('No se ha podido realizar el ataque')
        
#Funcion que verifica el estado del pokemon del jugador 
    def is_alive(pokemon_jugador):
        if pokemon_jugador.salud <= 0:
            return False
        else:
            return True

#Funcion que verifica el estado del pokemon de la maquina
    def is_alive(pokemon_maquina):
        if pokemon_maquina.salud <= 0:
            return False
        else:
            return True

```

**UML:**

***

