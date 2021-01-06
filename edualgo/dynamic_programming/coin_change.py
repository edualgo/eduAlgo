from __init__ import print_msg_box
import time 

def coin_change(coins, amount,hint=False):
    start = time.time()
    if hint:
        coin_change_hint()
    dp = [0]*(amount+1)
    for i in range(1, amount+1):
        if i in coins:
            dp[i] = 1
            continue
        min_coins = float("inf")
        for coin in coins:
            if i-coin >= 0:
                min_coins = min(dp[i-coin], min_coins)

        dp[i] = min_coins+1
    end = time.time()
    print("Time Taken: ",end-start)

    if dp[-1] == float("inf"):
        return -1
    print(dp)
    return dp[-1]

def coin_change_hint():
    message="""
                                Coin Change Problem
    ------------------------------------------------------------------------------------------
    Purpose : In this problem, We are given coins of different denominations and a total amount of money amount. 
    Calculate the fewest number of coins that we need to make up that amount. If no combination possible return -1.
    m = length of the coins array, n = amount

    Time Complexity : O(mn)
    Space Complexity : O(n)

    Hint :
    Apply Dynamic Programming on coins array to find the minimum required coins.

    Pseudocode: 
        dp = [0]*(amount+1)
        LOOP (i = 1, amount+1):
            if i in coins:
                dp[i] = 1
                continue
            min_coins = INFINITE
            LOOP coins array as coin:
                if i-coin >= 0:
                    min_coins = min(dp[i-coin], min_coins)
            dp[i] = min_coins+1
        return dp[-1]

    Visualization:
        coins = [1,2,5]
        amount = 6
        dp = [0]*(amount+1) = [0]*7
        index = [0,1,2,3,4,5,6] 
           dp = [0,0,0,0,0,0,0]

         Applying recursive formula at each index we get min coins
            min_coins = min(dp[index-coin], min_coins)
        
        * At index 1:
            index = [0,1,2,3,4,5,6] 
               dp = [0,1,0,0,0,0,0]

        * At index 2:
            index = [0,1,2,3,4,5,6] 
               dp = [0,1,1,0,0,0,0]

        * At index 3:
            index = [0,1,2,3,4,5,6] 
               dp = [0,1,1,2,0,0,0]

        * At index 4:
            index = [0,1,2,3,4,5,6] 
               dp = [0,1,1,2,2,0,0]

        * At index 5:
            index = [0,1,2,3,4,5,6] 
               dp = [0,1,1,2,2,1,0]

        * At index 6:
            index = [0,1,2,3,4,5,6] 
               dp = [0,1,1,2,2,1,2]

        FINAL RESULT = dp[-1] = 2

    Learn More:
    - Change Making - https://en.wikipedia.org/wiki/Change-making_problem
       
    """
    print_msg_box(message)

# print(coin_change([1,2,5],6,True))