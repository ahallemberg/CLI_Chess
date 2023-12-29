from src.board import Board, check, checkmate
from src.coords import AN, ChessNotationError
from src.engine import Engine
from src.spinner import Spinner
from pylibs.uinput import Input, Init, ExitProgram

class RestartGameException(Exception): 
    pass

Init.setCommands({"q": ExitProgram, "r": RestartGameException})

def make_player_move(board: Board, current_player: int) -> tuple[AN, AN]:
    while True: 
        try: 
            # velger brikke som skal flyttes ut fra koordinat
            coord1 = AN(Input("Skriv inn koordinaten til brikken du vil flytte: ").str)
            if board[coord1].player != current_player: 
                print(f"Dette er ikke en koordinat til en brikke som er din...")
                continue
            pb_moves = board[coord1].possible_moves(coord1, board)
            if len(pb_moves) == 0: 
                print("Du kan ikke flytte denne brikken...")
                continue
            break 

        except ChessNotationError: 
            print("Ugyldig koordinat")

    while True: 
        try: 
            # hvor brikken skal flyttes
            coord2 = AN(Input("Hvor skal brikken flyttes: ").str)
            if board[coord2].player == current_player: 
                print(f"Dette er en koordinat hvor du allerede har en brikke...")
                continue
            
            if coord2 in pb_moves: 
                board.move(coord1, coord2)
                break
            else: 
                print(f"Dette er ikke et gyldig trekk...")

        except ChessNotationError: 
            print("Ugyldig koordinat")

    
def main() -> None: 
    board = Board()
    current_player = 0 
    opponent = 0
    print(f'Sjakk 1v1\nNyttig info:\n- Skriv når som helst "q" for å avslutte spillet\n- Skriv "r" når som helst for å starte på nytt')
    print("Ønsker du å spille mot en annen spiller eller mot en bot(b/s?)")
    try: 
        match Input().case({1: ["b", "bot"], 0: ["s", "spiller"]}):
            case 0: 
                opponent = 0
                print("Spiller mot en annen spiller")
            case 1: 
                opponent = 1
                print("Spiller mot en bot")

    except ValueError: 
        pass
    
    try: 
        if opponent == 0: # game logic for playing against another player
            while True: 
                print(board)
                print(f'{"Hvit sin tur" if current_player == 0 else "Svart sin tur"}')

                make_player_move(board, current_player)

                player_in_check = check(board)
                if player_in_check != None: 
                    if player_in_check == current_player: 
                        print(f"Du kan ikke gjøre et trekk som gjør at du er i sjakk. Spiller {0 if current_player != 0 else 1} vant!")
                        break
                    else: 
                        print(f"Spiller {player_in_check} er i sjakk")
                        if checkmate() == player_in_check: 
                            print(f"Spiller {current_player} vant!")
                            break
                        current_player = 0 if current_player != 0 else 1
                else: 
                    current_player = 0 if current_player != 0 else 1

        elif opponent == 1: # game logic for playing against a bot
            engine = Engine(1)

            while True: 
                print(board)
                if current_player == 0: 
                    print("Din tur")
                    make_player_move(board, current_player)

                else: 
                    print("Bot sin tur")
                    spinner = Spinner()
                    spinner.start()
                    # make bot move
                    board.move(*engine.get_best_move(board))
                    spinner.stop()

                current_player = 0 if current_player != 0 else 1

                
    except ExitProgram:
        quit()

    except RestartGameException: 
        print("Restarter spillet...")
        main()

if __name__ == "__main__": 
    main()
else: 
    print(f"{__file__} cannot be imported")

