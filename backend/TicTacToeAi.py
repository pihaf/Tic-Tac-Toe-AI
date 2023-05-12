# import copy
# import random


# class TicTacToeAI:
#     def __init__(self, player):
#         self.player = player

#     def get_move(self, board, size):
#         # Find all available positions on the board
#         size = int(size)
#         available_moves = []
#         for i in range(size):
#             for j in range(size):
#                 if board[i][j] == ' ':
#                     available_moves.append((i, j))
                    
#         # If there are no available moves, return None
#         if not available_moves:
#             return None
#         # Choose a random available move
#         return available_moves[random.randint(0, len(available_moves) - 1)]

import copy

class TicTacToeAI:
    def __init__(self, player):
        self.player = player
        self.opponent = 'O' if player == 'X' else 'X'

    def get_move(self, board, size):
        if all([cell == ' ' for row in board for cell in row]):
            # Board is empty, choose center position
            return (size // 2, size // 2)
        else:
            best_score = float('-inf')
            best_move = None
            alpha = float('-inf')
            beta = float('inf')

            for i in range(size):
                for j in range(size):
                    if board[i][j] == ' ':
                        board_copy = copy.deepcopy(board)
                        board_copy[i][j] = self.player
                        score = self.minimax(board_copy, size, False, alpha, beta)
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
                        alpha = max(alpha, best_score)
                        if alpha >= beta:
                            break

            return best_move
        
    def minimax(self, board, size, is_maximizing, alpha, beta):
        print(f'minimax(board={board}, size={size}, is_maximizing={is_maximizing}, alpha={alpha}, beta={beta} \n)')
        winner = self.check_winner(board, size)
        if winner is not None:
            if winner == self.player:
                return 1
            elif winner == self.opponent:
                return -1
            else:
                return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(size):
                for j in range(size):
                    if board[i][j] == ' ':
                        board_copy = copy.deepcopy(board)
                        board_copy[i][j] = self.player
                        score = self.minimax(board_copy, size, False, alpha, beta)
                        best_score = max(best_score, score)
                        alpha = max(alpha, best_score)
                        if alpha >= beta:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(size):
                for j in range(size):
                    if board[i][j] == ' ':
                        board_copy = copy.deepcopy(board)
                        board_copy[i][j] = self.opponent
                        score = self.minimax(board_copy, size, True, alpha, beta)
                        best_score = min(best_score, score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

    def check_winner(self, board, size):
        print(f'check_winner(board={board}, size={size}) \n')
        # Check rows
        for i in range(size):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return board[i][0]

        # Check columns
        for j in range(size):
            if board[0][j] == board[1][j] == board[2][j] != ' ':
                return board[0][j]

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return board[0][0]

        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[0][2]

        # Check tie
        if all([cell != ' ' for row in board for cell in row]):
            return 'Tie'

        # Game is not over
        return None