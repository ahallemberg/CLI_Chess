# chess engine based on minimax algorithm with alpha-beta pruning
from board import Board, check, checkmate

class Engine: 
    def __init__(self, player: int) -> None:
        self.player = player
    
    def minimax(self, board: Board, depth: int, alpha, beta, maximizing_player: bool = True):
        board  = board.copy()

        if depth == 0 or checkmate(board):
            return self.evaluate_board(board)

        if maximizing_player:
            max_eval = float('-inf')
            for move1, move2 in board.get_moves(self.player):
                eval = self.minimax(board.move(move1, move2), depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move1, move2 in board.get_moves(self.player):
                eval = self.minimax(board.move(move1, move2), depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
        

    def evaluate_board(self, board: Board):
        score = 0
        for piece in board.pieces():
            if piece.player == self.player:
                score += piece.value
            else:
                score -= piece.value
        return score