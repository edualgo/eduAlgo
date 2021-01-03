from __init__ import print_msg_box
import time 

def longest_common_subsequence(X,Y,hint=False):
    start = time.time()
    if hint:
        longest_common_subsequence_hint()
    m = len(X) 
    n = len(Y)  
    L = [[None]*(n+1) for i in range(m+1)] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
    end = time.time()
    print("Time Taken: ",end-start)
    print(L)
    return L[m][n]

def longest_common_subsequence_hint():
    message="""
                                Longest Common Subsequence
    ------------------------------------------------------------------------------------------
    Purpose : The longest common subsequence problem is finding the longest sequence which exists in both the given strings.
    Method : Dynamic Programming

    Time Complexity : O(mn)
    Space Complexity : O(mn)

    Hint :
    Apply Dynamic Programming on both the strings to find Longest Common Subsequence.

    Pseudocode: 
        X and Y are strings
        m = len(X) 
        n = len(Y)  
        L = [[None]*(n+1) for i in range(m+1)] 
        for i in range(m+1): 
            for j in range(n+1): 
                if i == 0 or j == 0 : 
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]: 
                    L[i][j] = L[i-1][j-1]+1
                else: 
                    L[i][j] = max(L[i-1][j] , L[i][j-1]) 
        return L[m][n]

    Visualization:
        X = "ACDEU"
        Y = "ABCDE"

        Applying recursive formula at Longest Common Subsequence 2D Array 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 

            LCS  *  A  B  C  D  E
            *    0  0  0  0  0  0
            A    1  1  1  1  1  1
            C    0  1  1  2  2  2
            D    0  1  1  2  3  3
            E    0  1  1  2  3  4
            U    0  1  1  2  3  4 

        FINAL RESULT: L[m][n] = L[5][5] = 4



    Learn More:
    - Maximum Subarray Problem - https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
       
    """
    print_msg_box(message)

# print(longest_common_subsequence("ACDEU","ABCDE",True))
