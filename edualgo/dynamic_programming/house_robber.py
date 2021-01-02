from __init__ import print_msg_box
import time 

def house_robber(house,hint=False):
    start = time.time()
    if hint:
        house_robber_hint()
    n = len(house)
    if n == 0:
        return 0
    if n == 1:
        return house[0]
    if n == 2:
        return max(house[0],house[1])

    val1 = house[0]
    val2 = house[1]
    max_val = None

    for i in range(2,n):
        max_val = max(house[i]+val1, val2)
        val1 = val2 
        val2 = max_val
    
    end = time.time()
    print("Time Taken: ",end-start)

    return max_val

def house_robber_hint():
    message="""
                                House Robber Problem
    ------------------------------------------------------------------------------------------
    Purpose : There are n houses build in a line, each of which contains some value in it.
    A thief is going to steal the maximal value of these houses,
    but he can’t steal in two adjacent houses because the owner of the stolen houses will
    tell his two neighbours left and right side. What is the maximum stolen value?

    Method : Dynamic Programming

    Time Complexity : O(n)
    Space Complexity : O(1)

    Hint :
    Apply Dynamic Programming on value array of houses to find maximum amount.

    Pseudocode: 
        house: array of houses which contain some values

        Initialize:
            val1 = house[0]
            val2 = house[1]

            Loop(i=2,size)
            (a) max_val = max(house[i]+val1, val2)
            (b) val1 = val2
            (b) val2 = max_val

            return max_val

    Visualization:
        Input: house = [2,1,1,3]
        
        val1 = house[0] = 2
        val2 = house[1] = 1
        
        for i=2,
        max_val = max(house[i]+val1, val2) = max(1+2,1) = 3
        val1 = val2 = 1
        val2 = max_val = 3

        for i=3,
        max_val = max(house[i]+val1, val2) = max(3+1,3) = 4
        val1 = val2 = 3
        val2 = max_val = 4

        FINAL RESULT = max_val = 4

    Learn More:
    - Dynamic Programming - https://en.wikipedia.org/wiki/Dynamic_programming
       
    """
    print_msg_box(message)

# print(house_robber([2,1,1,3],True))
