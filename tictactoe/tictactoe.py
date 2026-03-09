"""
Tic Tac Toe Player
"""

import math
import numpy as np
import copy

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
    if(board==[[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]):
        return X
    
    np_board=np.array(board)
    if (np.count_nonzero(np_board == X)) > (np.count_nonzero(np_board == O)):
        return O
    else:
        return X
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_s=set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                action_s.add((i,j))
    return action_s
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j=action

    new_board=copy.deepcopy(board)
    new_board[i][j]=player(board)
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if(board[0][0]==board[0][1]==board[0][2]==X) or (board[1][0]==board[1][1]==board[1][2]==X) or (board[2][0]==board[2][1]==board[2][2]==X) or (board[0][0]==board[1][0]==board[2][0]==X) or (board[0][1]==board[1][1]==board[2][1]==X) or (board[0][2]==board[1][2]==board[2][2]==X) or (board[0][0]==board[1][1]==board[2][2]==X) or (board[0][2]==board[1][1]==board[2][0]==X):
        return X
    elif(board[0][0]==board[0][1]==board[0][2]==O) or (board[1][0]==board[1][1]==board[1][2]==O) or (board[2][0]==board[2][1]==board[2][2]==O) or (board[0][0]==board[1][0]==board[2][0]==O) or (board[0][1]==board[1][1]==board[2][1]==O) or (board[0][2]==board[1][2]==board[2][2]==O) or (board[0][0]==board[1][1]==board[2][2]==O) or (board[0][2]==board[1][1]==board[2][0]==O):   
        return O
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) is not None):
        return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j]==EMPTY):
                return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board)==X):
        return 1
    elif(winner(board)==O):
        return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)==True):
        return None
    

    def minimaxvalue(n_board):
        if(terminal(n_board)==True):
            return utility(n_board)
        
        if(player(n_board)==X):
            best_score=-math.inf
            actions_s=actions(n_board)
            for action in actions_s:
                new_board=result(n_board,action)
                score=minimaxvalue(new_board)
                if score>best_score:
                    best_score=score
            return best_score
        
        else:
            best_score=math.inf
            actions_s=actions(n_board)
            for action in actions_s:
                new_board=result(n_board,action)
                score=minimaxvalue(new_board)
                if score<best_score:
                    best_score=score
            return best_score


    turn=player(board)  

    if(turn==X):
        best_score= -math.inf
        best_action=None
        actions_s=actions(board)
        for action in actions_s:
            new_board=result(board,action)
            score=minimaxvalue(new_board)
            if score>best_score:
                best_score=score
                best_action=action
        return best_action
    
    else:
        best_score= math.inf
        best_action=None
        actions_s=actions(board)
        for action in actions_s:
            new_board=result(board,action)
            score=minimaxvalue(new_board)
            if score<best_score:
                best_score=score
                best_action=action
        return best_action
    

    
    raise NotImplementedError
