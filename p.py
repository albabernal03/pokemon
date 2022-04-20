print('.:COMIENZA LA BATALLA:.')
while salud_jugador > muerte and salud_maquina != 0:
    try:
                jugar = str(print(input('¿Desea jugar? (si/no):')))
            except SyntaxError:
                print('Error de sintaxis')
            if jugar == 'si':
                x= print(input('¿Que desea hacer? (atacar/defender):'))
                if x == 'atacar':
                    ataque_jugador = random.randint(1,10)
                    ataque_maquina = random.randint(1,10)
                    if ataque_jugador < ataque_maquina:
                        salud_jugador -= 10
                        print('Perdiste esta ronda')
                    else:
                        salud_maquina -=10
                        print('Ha ganado esta ronda')
                elif x == 'defender':
                    defensa_jugador = random.randint(1,10)
                    defensa_maquina = random.randit(1,10)
                    if defensa_jugador < ataque_jugador:
                        salud_jugador -= 10
                        print('Perdiste esta ronda')
                    else:
                        salud_maquina -=10
                        print('Ha ganado esta ronda')
            else:
                print('Has salido del juego')