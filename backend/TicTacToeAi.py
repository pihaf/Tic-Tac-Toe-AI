import copy
import random


class TicTacToeAI:
    def __init__(self, player):
        self.player = player

    def get_move(self, board, size):
        # Find all available positions on the board
        size = int(size)
        available_moves = []
        for i in range(size):
            for j in range(size):
                if board[i][j] == ' ':
                    available_moves.append((i, j))
                    
        # If there are no available moves, return None
        if not available_moves:
            return None
        # Choose a random available move
        return available_moves[random.randint(0, len(available_moves) - 1)]
# import copy
# import random

# class TicTacToeAI:
#     def __init__(self, player):
#         self.player = player
#         self.opponent = 'O' if player == 'X' else 'X'

#     def get_move(self, board, size):
#         size = int(size)
#         available_moves = []
#         for i in range(size):
#             for j in range(size):
#                 if board[i][j] == ' ':
#                     available_moves.append((i, j))

#         if not available_moves:
#             return None

#         best_move = None
#         best_score = float('-inf')
#         alpha = float('-inf')
#         beta = float('inf')
#         for move in available_moves:
#             new_board = copy.deepcopy(board)
#             new_board[move[0]][move[1]] = self.player
#             score = self.minimax(new_board, size, 0, False, alpha, beta)
#             if score > best_score:
#                 best_score = score
#                 best_move = move
#             alpha = max(alpha, score)
#             if alpha >= beta:
#                 break

#         return best_move

#     def minimax(self, board, size, depth, is_maximizing, alpha, beta):
#         result = self.check_winner(board, size)
#         if result is not None:
#             return result

#         if is_maximizing:
#             best_score = float('-inf')
#             for i in range(size):
#                 for j in range(size):
#                     if board[i][j] == ' ':
#                         board[i][j] = self.player
#                         score = self.minimax(board, size, depth + 1, False, alpha, beta)
#                         board[i][j] = ' '
#                         best_score = max(score, best_score)
#                         alpha = max(alpha, best_score)
#                         if alpha >= beta:
#                             return best_score
#             return best_score
#         else:
#             best_score = float('inf')
#             for i in range(size):
#                 for j in range(size):
#                     if board[i][j] == ' ':
#                         board[i][j] = self.opponent
#                         score = self.minimax(board, size, depth + 1, True, alpha, beta)
#                         board[i][j] = ' '
#                         best_score = min(score, best_score)
#                         beta = min(beta, best_score)
#                         if alpha >= beta:
#                             return best_score
#             return best_score

#     def check_winner(self, board, size):
#         # Check rows
#         for i in range(size):
#             if board[i][0] == board[i][1] == board[i][2] != ' ':
#                 return 1 if board[i][0] == self.player else -1

#         # Check columns
#         for j in range(size):
#             if board[0][j] == board[1][j] == board[2][j] != ' ':
#                 return 1 if board[0][j] == self.player else -1

#         # Check diagonals
#         if board[0][0] == board[1][1] == board[2][2] != ' ':
#             return 1 if board[0][0] == self.player else -1
#         if board[0][2] == board[1][1] == board[2][0] != ' ':
#             return 1 if board[0][2] == self.player else -1

#         # Check for tie
#         for i in range(size):
#             for j in range(size):
#                 if board[i][j] == ' ':
#                     return None
#         return 0