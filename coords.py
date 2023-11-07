from __future__ import annotations
from typing import overload

FILES = ["a","b","c","d","e","f","g","h"]
RANKS = [1,2,3,4,5,6,7,8]

class ChessNotationError(Exception):
    pass

class AN:
    """ 
    Algebraic notation for sjakk
    """
    @overload
    def __init__(self, cord: str) -> None: ...
    
    @overload
    def __init__(self, file: str, rank: int) -> None: ... 

    def __init__(self, file: str, rank: int|None=None) -> None: 
        if len(file) == 2: 
            if not self.valid_notation(file):
                raise ChessNotationError(f"{file} er en ugyldig algebraisk sjakknotasjon")
            self._cord = file

        elif len(file) == 1: 
            if not self.valid_notation(file, rank):
                raise ChessNotationError(f"file: {file}, rank: {rank} er en ugyldig algebraisk sjakknotasjon")
        
            self._cord = f"{file}{rank}"
            
        else: 
            raise ChessNotationError
     
    def __hash__(self) -> int:
        return hash(self._cord+"__AN")
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, AN) and self._cord == other.cord
    
    def __str__(self) -> str: 
        return f"AN({self._cord})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    @overload
    @staticmethod
    def valid_notation(file: str, rank: int) -> bool: ...

    @overload
    @staticmethod
    def valid_notation(cord: str) -> bool: ...
    
    @staticmethod
    def valid_notation(file: str, rank: int|None=None) -> bool: 
        if len(file) == 2: 
            rank = int(file[1])
            file = file[0]
        elif len(file) != 1: 
            raise ChessNotationError
        
        if file not in FILES: 
            return False
        if rank not in RANKS: 
            return False 
        return True
    
    def left(self) -> AN: 
        if self.file == FILES[0]:
            raise ChessNotationError
        return AN(FILES[FILES.index(self.file)-1], self.rank)
    
    def right(self) -> AN:
        if self.file == FILES[len(FILES)-1]:
            raise ChessNotationError
        return AN(FILES[FILES.index(self.file)+1], self.rank)

    def over(self) -> AN: 
        if self.rank == RANKS[len(RANKS)-1]:
            raise ChessNotationError
        return AN(self.file, RANKS[RANKS.index(self.rank)+1])

    def under(self) -> AN: 
        if self.rank == RANKS[0]:
            raise ChessNotationError
        return AN(self.file, RANKS[RANKS.index(self.rank)-1])
    
    def rel_coords(self, deltas: list[tuple[int, int]]) -> list[AN]: 
        for delta in deltas: 
            try: 
                pass  

            except IndexError: 
                pass


    def horizontal(self) -> list[AN]: 
        return [AN(file, self.rank) for file in FILES]
    
    def vertical(self) -> list[AN]: 
        return [AN(self.file, rank) for rank in RANKS]
    
    def diagonal(self, topright: bool) -> list[AN]:
        coords: list[AN] = []

        if topright: 
            try: 
                current_cord = self
                while True: 
                    current_cord = current_cord.over().right()
                    coords.append(current_cord)
                    
            except ChessNotationError: pass

            try: 
                current_cord = self
                while True: 
                    current_cord = current_cord.under().left()
                    coords.append(current_cord)

            except ChessNotationError: pass 
        else: 
            try: 
                current_cord = self
                while True: 
                    current_cord = current_cord.over().left()
                    coords.append(current_cord)
                    
            except ChessNotationError: pass

            try: 
                current_cord = self
                while True: 
                    current_cord = current_cord.under().right()
                    coords.append(current_cord)

            except ChessNotationError: pass 
            
        return coords

    def diagonals(self) -> list[AN]: 
        return self.diagonal(True).extend(self.diagonal(False))

    @property
    def cord(self) -> str: 
        return self._cord

    @cord.setter
    def cord(self, val: str) -> None: 
        if not self.valid_notation(val):
            raise ChessNotationError(f"{val} er en ugyldig algebraisk sjakknotasjon")
        self._cord = val
        
    @property
    def file(self) -> str: 
        return self._cord[0]

    @file.setter 
    def file(self, val: str) -> None: 
        if val in FILES: 
            self._cord = val + self._cord[1]
    
    @property 
    def rank(self) -> int:
        return int(self._cord[1])

    @rank.setter
    def rank(self, val: int) -> None: 
        if val in RANKS: 
            self._cord = self._cord[0] + str(val) 
 

AN.relCoords([(1, 0), (0, 0)])