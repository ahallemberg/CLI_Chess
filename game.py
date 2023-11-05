from pieces import King, Queen, Bishop, Knight, Rook, Pawn, Empty
from logic import AN, FILES, RANKS

class Board: 
    def __init__(self) -> None:  
        # init 

        self._board = {
            AN("a1"): Rook(0),
            AN("b1"): Knight(0),
            AN("c1"): Bishop(0),
            AN("d1"): Queen(0),
            AN("e1"): King(0),
            AN("f1"): Bishop(0),
            AN("g1"): Knight(0),
            AN("h1"): Rook(0),
            AN("a2"): Pawn(0),
            AN("b2"): Pawn(0),
            AN("c2"): Pawn(0),
            AN("d2"): Pawn(0),
            AN("e2"): Pawn(0),
            AN("f2"): Pawn(0),
            AN("g2"): Pawn(0),
            AN("h2"): Pawn(0),
            AN("a3"): Empty(),
            AN("b3"): Empty(),
            AN("c3"): Empty(),
            AN("d3"): Empty(),
            AN("e3"): Empty(),
            AN("f3"): Empty(),
            AN("g3"): Empty(),
            AN("h3"): Empty(),
            AN("a4"): Empty(),
            AN("b4"): Empty(),
            AN("c4"): Empty(),
            AN("d4"): Empty(),
            AN("e4"): Empty(),
            AN("f4"): Empty(),
            AN("g4"): Empty(),
            AN("h4"): Empty(),
            AN("a5"): Empty(),
            AN("b5"): Empty(),
            AN("c5"): Empty(),
            AN("d5"): Empty(),
            AN("e5"): Empty(),
            AN("f5"): Empty(),
            AN("g5"): Empty(),
            AN("h5"): Empty(),
            AN("a6"): Empty(),
            AN("b6"): Empty(),
            AN("c6"): Empty(),
            AN("d6"): Empty(),
            AN("e6"): Empty(),
            AN("f6"): Empty(),
            AN("g6"): Empty(),
            AN("h6"): Empty(),
            AN("a7"): Pawn(1),
            AN("b7"): Pawn(1),
            AN("c7"): Pawn(1),
            AN("d7"): Pawn(1),
            AN("e7"): Pawn(1),
            AN("f7"): Pawn(1),
            AN("g7"): Pawn(1),
            AN("h7"): Pawn(1),
            AN("a8"): Rook(1),
            AN("b8"): Knight(1),
            AN("c8"): Bishop(1),
            AN("d8"): Queen(1),
            AN("e8"): King(1),
            AN("f8"): Bishop(1),
            AN("g8"): Knight(1),
            AN("h8"): Rook(1)
        }

    def move(self, coord1: str, coord2: str) -> None: 
        self._board[coord2] = self._board[coord1]
        self._board[coord1] = Empty()

    # check for end game
    def __str__(self) -> str: 
        print(end="   ")
        for file in FILES: print(file, end=" ")
        print("\n"+"  "+"-"*16)
        for rank in reversed(RANKS): 
            for file in FILES: 
                if file == "a": 
                    print(rank-1, end=" |")
                print(f'{self._board[AN(f"{file}{rank}")]}|', end="")
                if file == "h":
                    print("\n"+"  "+"-"*16)
                
 
Board().__str__()

