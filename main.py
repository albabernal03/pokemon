from clases.ataque import partida
from clases.ataque import ataque_jugador
from clases.ataque import ataque_maquina
from clases.ataque import is_alive
from clases.extension_ataque import partida
from clases.extension_ataque import ataque_jugador
from clases.extension_ataque import ataque_maquina
from clases.extension_ataque import is_alive
from clases.pokemon import pokemon_jugador
from clases.pokemon import pokemon_maquina
from clases.pokemon import menu
from clases.pokemon_extension import pokemon_jugador
from clases.pokemon_extension import pokemon_maquina
from clases.pokemon_extension import menu

if __name__ == '__main__':
  partida()
  ataque_jugador()
  ataque_maquina()
  is_alive()
  
if __name__ == '__main__':
  partida()
  ataque_jugador()
  ataque_maquina()
  is_alive()

if __name__ == '__main__':
  pokemon_jugador()
  pokemon_maquina()
  menu()
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

if __name__ == '__main__':
  pokemon_jugador()
  pokemon_maquina()
  menu()
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


          
  