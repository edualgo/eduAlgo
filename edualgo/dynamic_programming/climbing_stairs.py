from __init__ import print_msg_box
import time 

def countWays(n): 
	res = [0 for x in range(n)] 
	res[0], res[1] = 1, 1
	for i in range(2, n): 
		res[i] = res[i-1] + res[i-2] 
	return res[n-1] 


def climbing_stairs(n,hint=False):
    start = time.time()
    if hint:
        climbing_stairs_hint()
    ans = countWays(n+1)
    end = time.time()
    print("Time Taken: ",end-start)
    return ans


def climbing_stairs_hint():
    message= """
                            Climb Stairs
    ------------------------------------------------------------------------------------------
    Purpose : There are n stairs, a person standing at the bottom and wants to reach the top.
        The person can climb either 1 stair or 2 stairs at a time. Count the number of ways,
        the person can reach the top.
    Method : Dynamic Programming
    Time Complexity : O(m*n)
    Space Complexity : O(n)
    Hint : Apply Dynamic Programming in bottom up manner.
    
    Pseudocode: 
        Create a res[] table in bottom up manner using the following relation:
           res[i] = res[i] + res[i-j] for every (i-j) >= 0
        such that the ith index of the array will contain 
        the number of ways required to reach the ith step considering
        all the possibilities of climbing (i.e. from 1 to i).
    
    Visualization:
    Input: n=3
               
                           ^                        ^                            ^
                        -------                  -------                      -------       
                    ^  |                        |                         ^  |
                  ------                   ------                       ------
               ^ |                     ^  |                            |
            ------                   ------                       ------   
         ^ |                     ^  |                         ^  |
      ------                  -------                      -------

   Output: 3
        
    Learn More:
    - - Dynamic Programming - https://en.wikipedia.org/wiki/Dynamic_programming
       
    """
    print_msg_box(message)

# print(climbing_stairs(3,True))