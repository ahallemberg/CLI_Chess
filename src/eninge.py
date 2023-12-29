# chess engine based on minimax algorithm with alpha-beta pruning
from src.board import Board, check, checkmate, AN

class Engine: 
    def __init__(self, player: int) -> None:
        self.player = player
    
    def get_best_move(self, board: Board) -> tuple[AN, AN]:
        best_move = None
        best_eval = float('-inf')
        for move1, move2 in board.get_moves(self.player):
            eval = self.minimax(board.move(move1, move2), 3, float('-inf'), float('inf'), False)
            if eval > best_eval:
                best_eval = eval
                best_move = (move1, move2)
        return best_move

    def minimax(self, board: Board, depth: int, alpha, beta, maximizing_player: bool = True) -> int:
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

    def evaluate_board(self, board: Board) -> int:
        score = 0
        for piece in board.pieces():
            if piece.player == self.player:
                score += piece.value
            else:
                score -= piece.value
        return score