board = [
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ]


def is_valid(board,row,col,num):
    for i in range(9):
        if board[row][i]==num and i!=col:return False
    for i in range(9):
        if board[i][col]==num and i!=row:return False
    x=row//3
    y=col//3
    for i in range(x*3,x*3+3):
        for j in range(y*3,y*3+3):
            if board[i][j]==num and (i!=row or j!=col):
                return False            
    return True

def solve(board):
    find=empty(board)
    if not find:
        return True
    else:
        row,col=find

    for i in range(1,10):
        if is_valid(board,row,col,i):
            board[row][col]=i
            if solve(board):return True
            board[row][col]=0
    return False

def empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:return (i,j)
    return None

solve(board)

for i in board:
    print(i)