from clases.extension_pokemon import Pokemon2
import random 

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
        



