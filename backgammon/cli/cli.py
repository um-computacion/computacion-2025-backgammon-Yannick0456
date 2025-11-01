from backgammon.core.game import BackgammonGame
from backgammon.core.exceptions import InvalidMoveError

def render(game: BackgammonGame) -> str:
    b = game.board
    top = " ".join(f"{b.point(i).count():2d}" for i in range(23, 11, -1))
    bot = " ".join(f"{b.point(i).count():2d}" for i in range(0, 12))
    lines = [
        f"Turno: {game.turn}",
        top,
        "-"*72,
        bot,
        f"Moves: {game.moves}",
    ]
    if game.is_finished():
        lines.append(f"==> ¡Ganó {game.winner()}!")
    return "\n".join(lines)

def help_text() -> str:
    return (
        "Comandos:\n"
        "  roll                # tirar los dados\n"
        "  move SRC DST        # mover de SRC a DST (0..23)\n"
        "  enter VAL           # reingresar desde barra usando VAL (1..6)\n"
        "  bearoff SRC VAL     # sacar ficha desde SRC usando VAL (1..6)\n"
        "  board               # mostrar tablero\n"
        "  help                # ayuda\n"
        "  quit                # salir\n"
    )

def main() -> None:
    game = BackgammonGame()
    print("Backgammon CLI. Escribí 'help' para ver comandos.")
    print(render(game))
    while True:
        try:
            parts = input("> ").strip().split()
        except EOFError:
            break
        if not parts:
            continue
        cmd = parts[0].lower()
        try:
            if cmd == "quit":
                break
            elif cmd == "help":
                print(help_text())
            elif cmd == "board":
                print(render(game))
            elif cmd == "roll":
                d1, d2, values = game.roll()
                print(f"Tirada: {d1} {d2} -> {values}")
                print(render(game))
            elif cmd == "move" and len(parts) == 3:
                src, dst = int(parts[1]), int(parts[2])
                game.apply_move(src, dst)
                print(render(game))
            elif cmd == "enter" and len(parts) == 2:
                val = int(parts[1])
                game.enter_from_bar(val)
                print(render(game))
            elif cmd == "bearoff" and len(parts) == 3:
                src, val = int(parts[1]), int(parts[2])
                game.bear_off(src, val)
                print(render(game))
            else:
                print("Comando no reconocido. 'help' para ayuda.")
        except InvalidMoveError as e:
            print(f"Error de movimiento: {e}")
        except Exception as e:
            print(f"Error: {e}")
    print("bye!")

if __name__ == "__main__":
    main()
