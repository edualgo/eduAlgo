# Rat in a Maze Problme via Backtracking
# the function rat_in_a_maze() takes the maze as an input (as 0 and 1)
# Source      :- Top Left
# Destination :- Bottom Right
# Moves allowed is DOWN, UP, LEFT and RIGHT

from __init__ import print_msg_box
from time import time
import sys
sys.setrecursionlimit(150000)

def rat_in_a_maze(maze, way=1, hint=False):                     # Main Function which takes the maze and way as an input
    start=time()
    if hint:
        rat_in_a_maze_hint()
    
    # By default, 1 is considered as walls and 0 is considered as way
    n=len(maze);m=len(maze[0])                                  # Dimentions of the maze
    wall= way^1                                              
    direction=[[1,0,'D'],[0,1,'R'],[-1,0,'U'],[0,-1,'L']]       # Directions to move
    visited=[[0]*m for i in range(n)]                           # To maintain the already visited spot
    
    # Base Condition to check whether the source or destination contains a wall
    if wall in (maze[0][0], maze[n-1][m-1]):               
        return 'Not Possible'
    
    temp=move_rat(0,0, n, m, maze, visited,way,direction,[])
    ans="".join(temp[1]) if temp[0] else 'Not Possible'
    print("Time Taken := ", time()-start)
    return ans

def move_rat(xx, yy, n, m, maze, visited,way, direction,ans):
    visited[xx][yy]=1
    # If the rat reached the destination 
    if(xx == n-1 and yy == m-1):
        return [1,ans]
    
    for i in range(4):
        row = xx + direction[i][0]
        col = yy + direction[i][1]
        if(0<=row<n and 0<=col<m and not visited[row][col] and maze[row][col]==way):
            ans+=[direction[i][2]]
            temp=move_rat(row,col,n,m,maze,visited,way,direction,ans)
            if temp[0]:
                return temp
            ans.pop()
    
    return [0,-1]

def rat_in_a_maze_hint():
    message="""
    
                            Rat in a Maze problem via Backtracking 
    ------------------------------------------------------------------------------------------      
    Pupose: Consider a rat placed at (0, 0) in a maze of order N*M. It has to 
    reach the destination at (N-1, M-1). Find a possible paths that the rat can take 
    to reach from source to destination. The directions in which the rat can move are 
    'U'(up), 'D'(down), 'L' (left), 'R' (right). Maze is in the form of a binary matrix
    containing 0's and 1's only. By default 0 is considered as wall cell whereas 1 is
    considered to way cell. The rat can only on the way cell.

    Method: Backtracking
    Time Complexity:
        Worst case- O(2^N*M)
        Best case-  O(N*M)
    
    Hint: Say the position of the rat is (X,Y). Then check for all the cells accessable through
    the current possition i.e (X+1,Y), (X-1,Y), (X,Y+1) and (X,Y-1) and see whether they are 
    way of wall. If wall, then move the rat to that position and repeat the process. In case 
    there is no possible move from the current position, backtrack the previous move and check
    for the next possible move and repeat the process until you encounter (N-1,M-1).

    Pseudocode:
        1) Mantain a boolean matrix visited to keep a note on 
            already visited node and a list of all possible moves 
            from a given position i.e direction.
        2) Check for the base case
            if destnation or source contains wall:
                return False
            else
                return move_rat(0,0,maze)
        3) In the recursive function, first check whether the current 
            position is the destination or not
            if current is destination
                return ans
            else
                check for all the possible move from that position
                if move is valid and not visited and next_move is way
                    return move_rat(next_move)

            if no move is valid
            return False
        

    Visualization:
        maze=[[1,0,0],
              [1,1,1],
              [0,0,1]]

        Source :=      (0,0)
        Destination := (2,2)
        Wall:= X
        grapical representaion of maze:
            +-------+-------+-------+
            |       |       |       |
            |   R   |   X   |   X   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |       |       |       |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   X   |   X   |       |
            |       |       |       |
            +-------+-------+-------+

        Base Condition check, whether the the Source and destination are not wall
        Now the Rat is at (0,0)
        UP, move not valid
        DOWN, move valid
            +-------+-------+-------+
            |       |       |       |
            |   *   |   X   |   X   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   R   |       |       |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   X   |   X   |       |
            |       |       |       |
            +-------+-------+-------+

        Now the Rat is at (1,0)
        UP, already visited
        DOWN, invalid move, WALL
        RIGHT, valid move
            +-------+-------+-------+
            |       |       |       |
            |   *   |   X   |   X   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   *   |   R   |       |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   X   |   X   |       |
            |       |       |       |
            +-------+-------+-------+

        Now the Rat is at (1,1)
        UP, invalid move, Wall
        DOWN, invalid move, WALL
        RIGHT, valid move
            +-------+-------+-------+
            |       |       |       |
            |   *   |   X   |   X   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   *   |   *   |   R   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   X   |   X   |       |
            |       |       |       |
            +-------+-------+-------+
        
        Now the Rat is at (1,2)
        UP, invalid move, Wall
        DOWN, valid move
            +-------+-------+-------+
            |       |       |       |
            |   *   |   X   |   X   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   *   |   *   |   *   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   X   |   X   |   R   |
            |       |       |       |
            +-------+-------+-------+
        
        Now the Rat is at (2,2)
        this is the Destination cell, hence we will terminate the recursion
        Answer: DRRD

        For animated visulization:- https://github.com/karan236/Algorithm-Visualizer

    """
    print_msg_box(message) 

