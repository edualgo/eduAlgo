from __init__ import print_msg_box
import time


def maximum_weight(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                              + K[i-1][w-wt[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


def knapSack(W, wt, val, hint=False):
    start = time.time()
    if hint:
        knapsack_hint()
    n = len(val)
    ans = maximum_weight(W, wt, val, n)
    end = time.time()
    print("Time Taken: ", end-start)
    return ans


def knapsack_hint():
    message = """
                            Knapsack Problem
    ------------------------------------------------------------------------------------------
    Purpose : Given weights and values of n items, put these items in a knapsack of 
    capacity W to get the maximum total value in the knapsack. You cannot break an item,
    either pick the complete item or don’t pick it (0-1 property).

    Method : Dynamic Programming

    Time Complexity : O(N*W)

    Space Complexity :  O(N*W)

    Hint : Apply Dynamic Programming.
    
    Pseudocode: 
        > Create a DP[][] table consider all the possible weights 
          from ‘1’ to ‘W’ as the columns and weights that can be kept as the rows. 
        > The state DP[i][j] will denote maximum value of ‘j-weight’ considering
          all values from ‘1 to ith’. 
        > Consider ‘wi’ (weight in ‘ith’ row) we can fill it in all columns 
          which have ‘weight values > wi’. 

    Visualization:
    
    Input:
    Let weight elements = {1, 2, 3}
    Let weight values = {10, 15, 40}
    Capacity=6

            
            0   1   2   3   4   5   6
         
            0  0   0   0   0   0   0   0
            1  0  10  10  10  10  10  10
            2  0  10  15  25  25  25  25
            3  0
    
    Explanation:
    For filling 'weight = 2' we come 
    across 'j = 3' in which 
    we take maximum of 
    (10, 15 + DP[1][3-2]) = 25   

            0   1   2   3   4   5   6

            0   0   0   0   0   0   0   0
            1   0  10  10  10  10  10  10
            2   0  10  15  25  25  25  25
            3   0  10  15  40  50  55  65

    Explanation:
    For filling 'weight=3', 
    we come across 'j=4' in which 
    we take maximum of (25, 40 + DP[2][4-3]) 
    = 50

    For filling 'weight=3' 
    we come across 'j=5' in which 
    we take maximum of (25, 40 + DP[2][5-3])
    = 55

    For filling 'weight=3' 
    we come across 'j=6' in which 
    we take maximum of (25, 40 + DP[2][6-3])
    = 65

    Output: 65
    Learn More:
    https://en.wikipedia.org/wiki/Knapsack_problem
       
    """
    print_msg_box(message)


val = [10, 15, 40]
wt = [1, 2, 3]
W = 6
print(knapSack(W, wt, val, True))
