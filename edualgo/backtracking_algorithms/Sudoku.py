import time 

from __init__ import print_msg_box

# Function To Check whether the selected Number can be placed in that row...
def isRowSafe(board,row,num):
    for j in range(0,9):
        if(board[row][j]==num):
            return False
    return True    

# Function To Check whether the selected Number can be placed in that Column...
def isColSafe(board,col,num):
    for i in range(0,9):
        if(board[i][col]==num):
            return False
    return True    
    
# Function To Check whether the selected Number can be placed in current box of 3 x 3...
def isBoxSafe(board,row,col,num):
    rs = row - row%3
    cs = col - col%3
    for i in range(rs,rs+3):
        for j in range(cs,cs+3):
            if(board[i][j]==num):
                return False
    return True      

# Function that check wether it is safe to place the number in this specific cell 
def CanPlaceNum(board,row,col,num):
    if(isRowSafe(board,row,num)==False):
        return False
    if(isColSafe(board,col,num)==False):
        return False
    if(isBoxSafe(board,row,col,num)==False):
        return False
    return True
    
#  Main recursive function for sudoku solver    
def Sudoku_Solver(board):
    row=-1
    col=-1
    isEmpty = False
    for i in range(0,9):
        for j in range(0,9):
            if(board[i][j]==0):
                isEmpty = True
                row=i
                col=j
                break
        if(isEmpty):
            break
    if(isEmpty == False):
        for i in range(0,9):
            for j in range(0,9):
                print(board[i][j],end=" ")
            print()    
        return True
    for num in range(1,10):
        if(CanPlaceNum(board,row,col,num)):
            board[row][col] = num
            if(Sudoku_Solver(board)):
                return True
            board[row][col] = 0;
    return False        

def Sudoku_Solver_hint():
    message= """
    Sudoku
    ------------------------------------
    Purpose : To solve Sudoku Grid of 9 X 9.
    Method : Recursive , Backtracking
    Time Complexity: Worst Case - O(9^(n*n))
    Space Complexity:  O(n*n)
    
    Hint:
    * Find the first empty cell in the Sudoku Grid by simply searhing through two for loops
        if no cell is empty i.e. this is the base condition return back and Complexity
        if any cell is present empty then store the row and Column of that cell and break the loops
    
    *Now one bye one check whether any digit ranging from [1-9] can be placed in that cell. 
    For this checking we had used function CanPlaceNum this will inturn check for row, col and box.
        -> for Row the isRowSafe function will check whether any digit in this row is equal to the digit that we are going to place are equal
            if yes then return false else continue and return true at last.
        -> for Column the isColSafe function will check whether any digit in this Column is equal to the digit that we are going to place are equal
            if yes then return false else continue and return true at last.
        -> for Box that is the box that are of fixed size of 3 X 3, the  function isBoxSafe is used and do the same as above
            But one thing the start of row and column are important that is calculated using :
                            rs = row - row%3
                            cs = col - col%3
    * Now if we are unable to place the digit then we try the next digit and continue the process...
        and if we are able to place the digit then we will Recursively call the Sudoku_Solver() function ,if this call return true then 
        we will continue else we have to Backtrack by placing 0 to that cell and try another number in that place...
        
    Visualization:
    suppose we have a sudoku of 4 X 4 size as Below:
    INPUT:
         0    1  2     3
        +---------------+
    0   |1    3 |0     4|               
        |       |       |
    1   |2    0 |3     1|
        |-------+-------|
    2   |0     1|0     2|
        |       |       |
    3   |4     0|1     0|
        +---------------+
        
    0 -> Empty Cell 
    
    we found the first Empty cell (0,2).
    Now we will check numbers from [1-9].
    we find that we can place a 2.
    
          0    1  2     3
        +---------------+
    0   |1    3 |2     4|               
        |       |       |
    1   |2    0 |3     1|
        |-------+-------|
    2   |0     1|0     2|
        |       |       |
    3   |4     0|1     0|
        +---------------+
    Now Recursively finding the Empty cell 
    we found (1,1) and the Recursion continue
    
          0    1  2     3
        +---------------+
    0   |1    3 |2     4|               
        |       |       |
    1   |2    4 |3     1|
        |-------+-------|
    2   |0     1|0     2|
        |       |       |
    3   |4     0|1     0|
        +---------------+
        
          0    1  2     3
        +---------------+
    0   |1    3 |2     4|               
        |       |       |
    1   |2    4 |3     1|
        |-------+-------|
    2   |3     1|4     2|
        |       |       |
    3   |4     2|1     0|
        +---------------+
     
    FINAL RESULT:     
          0    1  2     3
        +---------------+
    0   |1    3 |2     4|               
        |       |       |
    1   |2    4 |3     1|
        |-------+-------|
    2   |3     1|4     2|
        |       |       |
    3   |4     2|1     3|
        +---------------+     
        
    """
    print_msg_box(message)
