# N-Queens Problem via Backtracking

from __init__ import print_msg_box
from time import time as ti

def n_queens(board_size,hint=False):            #Main function argument =size of the board

    st=ti()
    
    #Occupied Diagonals and Columns
    diagonal1={};diagonal2={}                       #For right and left Diagonal respectively
    Col={}                                          #For Column which are already alloted to some queen 
    ans=place_queen(0,[],board_size,diagonal1,diagonal2,Col)                      
    print("Time Taken := "ti()-st)

    if hint:
        n_queens_hint()

    if not ans:
        return -1


    return ans

def place_queen(row,a,n,diagonal1,diagonal2,Col):                         #Recursive Function to check and place the queens
    #If the answer is found, row will be equal to the size of the board i.e. n
    if(row==n):                             
        return a
    R=row+1

    for C in range(1,n+1):

        #Check that particular Column is free to place a queen or not
        if((C not in Col) and ((R+C) not in diagonal1) and ((R-C) not in diagonal2)):   

            #Add the Column and their respective Diagonals to the dictionary to mark they are Occupied
            Col[C]=0
            diagonal1[R+C]=0;diagonal2[R-C]=0
            chk=place_queen(row+1,a+[(row,C-1)],n,diagonal1,diagonal2,Col)
            if chk:            #If the answer is found, Stop the recursion
                return chk
            
            #Deleaating the Column and Diagonals to vacant that place
            del diagonal1[R+C];del Col[C]
            del diagonal2[R-C]

    return False  

def n_queens_hint():
    message="""
                                N-Queens problem via Backtracking 
    ------------------------------------------------------------------------------------------    
   
    Purpose : To place n queens in an n X n Chessboard where no queen attack another queen
    in any form(such as diagonaly, through row or through Column), i.e. all the queen 
    place are safe.

    Method : Backtracking
    Time Complexity : 
        Worst Case - O(n!)
        Best Case  - O(n^2)
        
    Hint : Since we can put only one queen in a particular row/column, we can assume the 
        board to be a 1-d array where the index number of the array is the row number 
        and the value in that position is the column of the placed Queen. We must also 
        maintain seprate set for left and right diagonals. Then we can sequentially put
        the queen in every column of the given row and check wether the postition is right or
        not and recursively do so for the next row. If the recursion fails, we can backtrack
        and try a diffrent column and repeat the process.

    Pseudocode:
    --> Input: board_size
            1) Maintain a set of occupied Diagonals and Columns
                diagonal1={};diagonal2={}                      
                Col={}
                ans=[]
            2) Call the recursive function for row=0    
            3) In the Function,for a given row=R, try every Column C between 0 to n-1:
                    Check if the Column is occupied and the respective diagonal (R-C) and 
                    (R+C) are occupied or not.
                        If free, then add the column C and the Diagonals in their respective 
                        sets and call the recursive function for next row, i.r row=R+1

                        If not free, then try another column.
            4) If in the recursive function, row= board_size. That means all the queens are placed 
                and now we can stop the recursion.

    Visualization:
    --> board_size = 3
        For R=0,
        placing queen at C=0 i.e at (0,0)
            +-------+-------+-------+
            |       |       |       |
            |   X   |       |       |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |       |       |       |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |       |       |       |
            |       |       |       |
            +-------+-------+-------+
        For R=1,
        Placing Queen at C=0, i.e at (1,0)
            But, column 0 is already occupied,so try next Col

        Placing Queen at C=1, i.e at (1,1)
            But, Diagonal2(R+C) i.e. 0 is already occupied

        Placing Queen at C=2, i.e. at (1,2)
            +-------+-------+-------+
            |       |       |       |
            |   X   |       |       |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |       |       |   X   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |       |       |       |
            |       |       |       |
            +-------+-------+-------+
                Queen is safe
        For R=2
        Placing Queen at C=0, i.e at (2,0)
            +-------+-------+-------+
            |       |       |       |
            |   X   |       |       |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |       |       |   X   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   X   |       |       |
            |       |       |       |
            +-------+-------+-------+
                But, column 0 is already occupied,so try next Col

        Placing Queen at C=1, i.e.at (2,1)
            But, Diagonal1(R-C) i.e 1 already exist,
        Placing Queen at C=2, i.e at (2,2)
            But, column 2 is already occupied,so try next Col
        Placing Queen at C=3, but thats out of the board
            Hence recursion fails

        We back track to R=1, and place the queen in next Col
        
        And this will go On but there in no solution  for a board of 
        size 3, Hence the program will return -1.

        But for a board_size =4, the following will be one of the answer,
            [(0, 1), (1, 3), (2, 0), (3, 2)]

            +-------+-------+-------+-------+
            |       |       |       |       |
            |       |   X   |       |       |
            |       |       |       |       |
            +---------------+-------+-------+
            |       |       |       |       |
            |       |       |       |   X   |
            |       |       |       |       |
            +-------+-------+-------+-------+
            |       |       |       |       |
            |   X   |       |       |       |
            |       |       |       |       |
            +-------+-------+-------+-------+
            |       |       |       |       |
            |       |       |   X   |       |
            |       |       |       |       |
            +-------+-------+-------+-------+
            
    """
    print_msg_box(message) 
#print(n_queens(4))