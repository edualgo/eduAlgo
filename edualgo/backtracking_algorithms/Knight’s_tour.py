from __init__ import print_msg_box
import time

def isSafe(n, x, y, board):  # function to check if x,y are valid indexes
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False

def printSolution(n, board):  # function to print Chessboard matrix
    print('Result: ')
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

# function solves the Knight Tour problem using Backtracking.
def knightTour(n, hint=False):
    start = time.time()
    if hint:
        knight_tour_hint()
    end = time.time()
    # Initialization of Chess Board matrix
    board = [[-1 for i in range(n)]for i in range(n)]

    # move_x and move_y define next move of Knight.
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]  # move_x is for next value of x
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]  # move_y is for next value of y

    board[0][0] = 0     # Initially Knight at the first block
    pos = 1             # Step counter for knight's position

    # Checking if solution exists or not
    if(not knightTourUtil(n, board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        printSolution(n, board)
    print("Time Taken: ", end-start)

def knightTourUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
    if(pos == n**2):
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(n, new_x, new_y, board)):
            board[new_x][new_y] = pos
            if(knightTourUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
                return True
            board[new_x][new_y] = -1        # Backtracking
    return False

def knight_tour_hint():
    message = """
                 The Knight's Tour Problem
    -------------------------------------------------------------
    Purpose :  Given a N*N Chess board with the Knight placed
    on the first block of an empty board. Our task is to move 
    according to the rules of chess knight must visit each 
    square exactly once. Print the order of each the cell in 
    which they are visited.

    Method: Backtracking, Recursion
    Time Complexity: O(8^(N*N)) 

    Hint: 
    We choose a move of the knight from all the moves 
    available, and then recursively check if this will lead 
    us to the solution or not. If not, then we will backtrack 
    and choose a different path.

    Pseudocode: 
    A Knight can make maximum eight moves.
    
            +-------+-------+-------+-------+-------+
            |       | (i-2, |       | (i-2, |       |
            |       |  j-1) |       | j+1)  |       |
            +-------+-------+-------+-------+-------+
            | (i-1, |       |       |       | (i-1, |
            |  j-2) |       |       |       |  j+2) |
            +-------+-------+-------+-------+-------+
            |       |       | (i,j) |       |       |
            |       |       |       |       |       |
            +-------+-------+-------+-------+-------+
            | (i+1, |       |       |       | (i+1, |
            |  j-2) |       |       |       |  j+2) |
            +-------+-------+-------+-------+-------+
            |       | (i+2, |       | (i+2, |       |
            |       |  j-1) |       |  j+1) |       |
            +-------+-------+-------+-------+-------+
            
    1. Add one of the next moves to solution list and recursively 
    check if this move leads to a solution.
    2. If the move chosen in the above step doesn't lead to a 
    solution then remove that move from the solution list and 
    try other alternative moves.
    3. If none of the moves work then return false.
       ("No Soultion Exist")
       Else if all the squares are visited "Print the Soultion".

    Visualization:
    Suppose we have a Chess Board of 5X5 size as Below:
    INPUT: n=5

    Output: 
            +-----+-----+-----+-----+-----+
            | 1   | 14  | 9   | 20  | 3   |
            +-----+-----+-----+-----+-----+
            | 24  | 19  | 2   | 15  | 10  |
            +-----+-----+-----+-----+-----+
            | 13  | 8   | 23  | 4   | 21  |
            +-----+-----+-----+-----+-----+
            | 18  | 25  | 6   | 11  | 16  |
            +-----+-----+-----+-----+-----+
            | 7   | 2   | 17  | 22  | 5   |
            +-----+-----+-----+-----+-----+

    Learn More:
    The Knight's Tour Problem - 
    https://en.wikipedia.org/wiki/Knight%27s_tour
   
       
    """
    print_msg_box(message)
# knightTour(8, True)
