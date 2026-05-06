# CodeWars - Tic-Tac-Toe Checker

def is_solved(board):
    if len(set(board[0])) == 1 and board[0][0] != 0:
        return board[0][0]
    if len(set(board[1])) == 1 and board[1][1] != 0:
        return board[1][1]
    if len(set(board[2])) == 1 and board[2][2] != 0:
        return board[2][2]
    
    if len(set(board[i][0] for i in range(3))) == 1 and board[0][0] != 0:
        return board[0][0]
    if len(set(board[i][1] for i in range(3))) == 1 and board[0][1] != 0:
        return board[0][1]
    if len(set(board[i][2] for i in range(3))) == 1 and board[0][2] != 0:
        return board[0][2]
    
    if len(set((board[i][i] for i in range(3)))) == 1 and board[0][0] != 0:
        return board[0][0]
    if len(set(board[2-i][i] for i in range(2, -1, -1))) == 1 and board[0][2] != 0:
        return board[0][2]
    
    for row in board:
        if any(num == 0 for num in row):
            return -1
    
    return 0
    
print(is_solved([[0,0,2],[0,0,0],[1,0,1]])) # -1
print(is_solved([[0,0,1],[0,1,0],[1,0,0]])) # 1
print(is_solved([[1,2,1],[2,1,2],[2,1,2]])) # 0