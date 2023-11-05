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
        return self.__str__
    
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
        pass
    
    def right(self) -> AN:
        pass

    def over(self) -> Self: 
        pass

    def under(sekf) -> Self: 
        pass

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
    
coord1 = AN("a1")

coord1.rank += 1
coord1.file += ""
coord1.left().right()

print(coord1)
