from pokemon import Pokemon
import random 


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
        if turno == 1 and ataque_jugador > defensa_maquina:
            ataque_jugador(pokemon_jugador, pokemon_maquina)
            print()
            print (f'{pokemon_jugador.nombre} ataca, {pokemon_maquina.nombre} ahora tiene {pokemon_maquina.salud} de salud')
            print('==PRÓXIMA RONDA==')
        elif turno == 1 and ataque_jugador < defensa_maquina:
            print('No se ha podido realiza el ataque')
            print('==PRÓXIMA RONDA==')
        elif turno == 2 and ataque_maquina > defensa_jugador:
            ataque_maquina(pokemon_maquina, pokemon_jugador)
            print()
            print(f'{pokemon_maquina.nombre} ataca, {pokemon_jugador.nombre} ahora tiene {pokemon_jugador.salud} de salud')
            print('==PRÓXIMA RONDA==')
        elif turno == 2 and ataque_maquina < defensa_jugador:
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
        pokemon_maquina.salud == pokemon_maquina.salud - 4
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
        


