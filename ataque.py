from pokemon import Pokemon
import random 

pokemon_jugador = Pokemon.pokemon_jugador()
pokemon_maquina = Pokemon.pokemon_maquina()

# definir funcion ataque
def ataque(pokemon_jugador, pokemon_maquina):
    if pokemon_jugador.arma == 'puñetazo':
        pokemon_maquina.salud == pokemon_maquina.salud - 5
    elif pokemon_jugador.arma == 'patada':
        pokemon_maquina.salud == pokemon_maquina.salud - 3
    elif pokemon_jugador.arma == 'codazo':
        pokemon_maquina.salud == pokemon_maquina.salud - 3
    elif pokemon_jugador.arma == 'cabezazo':
        pokemon_maquina.salud == pokemon_maquina.salud - 4
    else:
        print('No se ha podido realizar el ataque')
        

