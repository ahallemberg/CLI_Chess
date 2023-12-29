# chess engine based on minimax algorithm with alpha-beta pruning
from src.board import Board, checkmate, AN

class Engine: 
    def __init__(self, player: int) -> None:
        self.player = player
    
    def get_best_move(self, board: Board) -> tuple[AN, AN]:
        """
        Gets best move for the engine using minimax algorithm with alpha-beta pruning
        """
        best_move = None
        best_eval = float('-inf')
        for move1, move2 in board.get_moves(self.player):
            board_cp = board.copy()
            board_cp.move(move1, move2)
            eval = self.minimax(board_cp, 3, float('-inf'), float('inf'), False)
            if eval > best_eval:
                best_eval = eval
                best_move = (move1, move2)
        return best_move

    def minimax(self, board: Board, depth: int, alpha, beta, maximizing_player: bool = True) -> int:
        """
        Minimax algorithm with alpha-beta pruning
        """
        if depth == 0 or type(checkmate(board)) == int:
            return self.evaluate_board(board)

        if maximizing_player:
            max_eval = float('-inf')
            for move1, move2 in board.get_moves(self.player):
                board_cp = board.copy()
                board_cp.move(move1, move2)
                eval = self.minimax(board_cp, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move1, move2 in board.get_moves(self.player):
                board_cp = board.copy()
                board_cp.move(move1, move2)
                eval = self.minimax(board_cp, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def evaluate_board(self, board: Board) -> int:
        """
        Evaluates the board and returns a score based on the pieces on the board
        """
        score = 0
        for piece in board.pieces():
            if piece.player == self.player:
                score += piece.value
            else:
                score -= piece.value
        return score