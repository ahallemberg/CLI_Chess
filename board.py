from coords import AN, FILES, RANKS
from pieces import Piece, King, Queen, Rook,  Knight, Pawn, Bishop, Empty
from copy import deepcopy

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
    def get_moves(self, player: int) -> list[tuple[AN, AN]]:
        _list = []
        for coord in self._board: 
            if self._board[coord].player == player: 
                for move in self._board[coord].possible_moves(coord, self): 
                    _list.append((coord, move))
        
        return _list

    def pieces(self) -> list[Piece]: 
        return list(self._board.values())
    
    def copy(self) -> 'Board': 
        cp = Board()
        cp._board = deepcopy(self._board)
        return cp
    
    def __getitem__(self, index: AN) -> Piece: 
        return self._board[index]

    def move(self, coord1: str, coord2: str) -> None: 
        self._board[coord2] = self._board[coord1]
        self._board[coord1] = Empty()

    # check for end game
    def __str__(self) -> str: 
        _str = "\n   "
        for file in FILES: _str += file + " "
        _str += "\n"+"  "+"-"*16 + "\n"
        for rank in reversed(RANKS): 
            for file in FILES: 
                if file == "a": 
                    _str += f"{rank} |"
                _str += f'{self._board[AN(f"{file}{rank}")]}|'
                if file == "h":
                    _str += "\n"+"  "+"-"*16 + "\n"
        
        return _str 

def check(board: Board) -> None|int:
    king_coord_0 = None
    king_coord_1 = None 
    pb_moves_player_0: list[AN] = []
    pb_moves_player_1: list[AN] = []

    for coord in board._board: 
        if isinstance(board[coord], King): 
            if board[coord].player == 0: 
                king_coord_0 = coord
            elif board[coord].player == 1: 
                king_coord_1 = coord

        else: 
            if board[coord].player == 0: 
                [pb_moves_player_0.append(val) for val in board[coord].possible_moves(coord, board)]
                
            elif board[coord].player == 1: 
                [pb_moves_player_1.append(val) for val in board[coord].possible_moves(coord, board)]

    if king_coord_0 in pb_moves_player_1: 
        return 0
     
    elif king_coord_1 in pb_moves_player_0: 
        return 1
        
def checkmate(board: Board) -> None|int:
    king_coord_0 = None
    king_coord_1 = None 
    pb_moves_player_0: list[AN] = []
    pb_moves_piece_and_coord_0: dict[AN, list[Piece, AN]] = {}
    pb_moves_player_1: list[AN] = []
    pb_moves_piece_and_coord_1: dict[AN, list[Piece, AN]] = {}

    for coord in board._board: 
        if isinstance(board[coord], King): 
            if board[coord].player == 0: 
                king_coord_0 = coord
          

            elif board[coord].player == 1: 
                king_coord_1 = coord

        else: 
            if board[coord].player == 0: 
                [pb_moves_player_0.append(val) for val in board[coord].possible_moves(coord, board)]
                pb_moves_piece_and_coord_0[coord] = [board[coord], coord]

            elif board[coord].player == 1: 
                [pb_moves_player_1.append(val) for val in board[coord].possible_moves(coord, board)]
                pb_moves_piece_and_coord_1[coord] = [board[coord], coord]
    
    # check king 0 
    king_0_pb_moves = board[king_coord_0].possible_moves(king_coord_0, board)
    is_checkmate = True
    # check if any of the pieces can be moved to any of the places
    for mv in king_0_pb_moves: 
        if mv not in pb_moves_player_1: 
            is_checkmate = False
        else: 
            if mv in pb_moves_player_0: # can block
                is_checkmate = False

            # check if can take piece 
            if pb_moves_piece_and_coord_1[mv][1] in pb_moves_player_0: 
                is_checkmate = False
    
    if is_checkmate: 
        return 0
      # check king 1
    king_1_pb_moves = board[king_coord_1].possible_moves(king_coord_1, board)
    is_checkmate = True
    # check if any of the pieces can be moved to any of the places
    for mv in king_1_pb_moves: 
        if mv not in pb_moves_player_0: 
            is_checkmate = False
        else: 
            if mv in pb_moves_player_1: # can block
                is_checkmate = False

            # check if can take piece 
            if pb_moves_piece_and_coord_0[mv][1] in pb_moves_player_1: 
                is_checkmate = False
    
    if is_checkmate: 
        return 1