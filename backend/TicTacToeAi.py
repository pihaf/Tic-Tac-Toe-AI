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

# class TicTacToeAI:
#     def __init__(self, player):
#         self.player = player
#         self.opponent = 'O' if player == 'X' else 'X'

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
        
#         # If there is only one available move, return it
#         if len(available_moves) == 1:
#             return available_moves[0]
        
#         # Use the minimax algorithm with alpha-beta pruning to choose the best move
#         best_move = None
#         max_score = float('-inf')
#         for move in available_moves:
#             new_board = copy.deepcopy(board)
#             new_board[move[0]][move[1]] = self.player
#             score = self.minimax(new_board, depth=4, alpha=float('-inf'), beta=float('inf'), maximizing_player=False)
#             if score > max_score:
#                 max_score = score
#                 best_move = move
        
#         return best_move
    
#     def minimax(self, board, depth, alpha, beta, maximizing_player):
#         # Check if the game is over
#         winner = self.get_winner(board)
#         if winner == self.player:
#             return 1
#         elif winner == self.opponent:
#             return -1
#         elif winner == 'Draw':
#             return 0
        
#         # Check if the maximum depth has been reached
#         if depth == 0:
#             return 0
        
#         # Use the minimax algorithm with alpha-beta pruning to choose the best move
#         if maximizing_player:
#             max_score = float('-inf')
#             for i in range(len(board)):
#                 for j in range(len(board)):
#                     if board[i][j] == ' ':
#                         new_board = copy.deepcopy(board)
#                         new_board[i][j] = self.player
#                         score = self.minimax(new_board, depth - 1, alpha, beta, False)
#                         max_score = max(max_score, score)
#                         alpha = max(alpha, score)
#                         if beta <= alpha:
#                             break
#             return max_score
#         else:
#             min_score = float('inf')
#             for i in range(len(board)):
#                 for j in range(len(board)):
#                     if board[i][j] == ' ':
#                         new_board = copy.deepcopy(board)
#                         new_board[i][j] = self.opponent
#                         score = self.minimax(new_board, depth - 1, alpha, beta, True)
#                         min_score = min(min_score, score)
#                         beta = min(beta, score)
#                         if beta <= alpha:
#                             break
#             return min_score
    
#     def get_winner(self, board):
#         size = len(board)
#         # Check rows
#         for i in range(size):
#             if all(board[i][j] == self.player for j in range(size)):
#                 return self.player
#             elif all(board[i][j] == self.opponent for j in range(size)):
#                 return self.opponent
#         # Check columns
#         for j in range(size):
#             if all(board[i][j] == self.player for i in range(size)):
#                 return self.player
#             elif all(board[i][j] == self.opponent for i in range(size)):
#                 return self.opponent
#         # Check diagonals
#         if all(board[i][i] == self.player for i in range(size)):
#             return self.player
#         elif all(board[i][i] == self.opponent for i in range(size)):
#             return self.opponent
#         elif all(board[i][size - 1 - i] == self.player for i in range(size)):
#             return self.player
#         elif all(board[i][size - 1 - i] == self.opponent for i in range(size)):
#             return self.opponent
#         # Check for a draw
#         if all(board[i][j] != ' ' for i in range(size) for j in range(size)):
#             return 'Draw'
#         # If the game is not over, return None
#         return None