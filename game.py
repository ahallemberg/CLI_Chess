from board import Board, check, checkmate
from coords import RANKS, FILES, AN, ChessNotationError
from pylibs.uinput import Input

def main() -> None: 
    board = Board()
    current_player = 0 
    print(f'Sjakk 1v1\nNyttig info:\n- Skriv når som helst "q" for å avslutte spillet\n- Skriv "r" når som helst for å starte på nytt')

    while True: 
        print(board)
        print(f'{"Hvit sin tur" if current_player == 0 else "Svart sin tur"}')
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
        
        player_in_check = check(board)
        if player_in_check != None: 
            if player_in_check == current_player: 
                print(f"Du kan ikke gjøre et trekk som gjør at du er i sjakk. Spiller {0 if current_player != 0 else 1} vant!")
                break
            else: 
                print(f"Spiller {player_in_check} er i sjakk")
                if checkmate() == player_in_check: 
                    print(f"Spilelr {current_player} vant!")
                    break
                current_player = 0 if current_player != 0 else 1
        else: 
            current_player = 0 if current_player != 0 else 1

if __name__ == "__main__": 
    main()
else: 
    print(f"{__file__} cannot be imported")

