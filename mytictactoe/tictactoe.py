"""
Tic Tac Toe Player
"""

import copy
import random
import sys

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_num, o_num = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_num += 1
            elif board[i][j] == O:
                o_num += 1

    if x_num > o_num:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_list.append((i, j))

    return empty_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(new_board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != EMPTY:
        return board[2][0]
    
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    r = winner(board)
    if r == X:
        return 1
    if r == O:
        return -1

    return 0


def max_value(board):
    v = -1000

    if terminal(board):
        return utility(board)

    for a in actions(board):
        v = max(v, min_value(result(board, a)))

    return v


def min_value(board):
    v = 1000

    if terminal(board):
        return utility(board)

    for a in actions(board):
        v = min(v, max_value(result(board, a)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimal_action = None

    if player(board) == X:
        maximum = -1000
        for a in actions(board):
            v = min_value(result(board, a))
            if v > maximum:
                maximum = v
                optimal_action = a

    else:
        minimum = 1000
        for a in actions(board):
            v = max_value(result(board, a))
            if v < minimum:
                minimum = v
                optimal_action = a
    
    return optimal_action


