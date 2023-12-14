def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-----")

def verificar_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True
    return False

def jugar_tic_tac_toe():
    tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    jugador = "X"
    jugando = True
    while jugando:
        imprimir_tablero(tablero)
        fila = int(input("Selecciona fila (0, 1, 2): "))
        columna = int(input("Selecciona columna (0, 1, 2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            if verificar_ganador(tablero):
                imprimir_tablero(tablero)
                print("¡Jugador", jugador, "ha ganado!")
                jugando = False
            else:
                jugador = "O" if jugador == "X" else "X"
        else:
            print("Esa casilla ya está ocupada. ¡Intenta de nuevo!")
    print("¡Gracias por jugar!")

jugar_tic_tac_toe()