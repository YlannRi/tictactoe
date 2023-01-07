
winning_combinations = [
    [0, 1, 2],  # rows
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],  # columns
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],  # diagonals
    [2, 4, 6]
]

board =[    [" ", [" "], [" "]],
            [" ", [" "], [" "]],
            [" ", [" "], [" "]]
]
def makemove(col,row):
    rowp1 = int(input("What row do you want to choose(chose between 0-2):"))
    colp1 = int(input("What colon do you want to choose(chose between 0-2):"))
    board[rowp1][colp1] = "X"
    print(board)
    rowp2 = int(input("What row do you want to choose(chose between 0-2):"))
    colp2 = int(input("What colon do you want to choose(chose between 0-2):"))
    board[rowp2][colp2] = "O"
    print(board)

    
