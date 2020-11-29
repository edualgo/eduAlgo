from __init__ import print_msg_box
import time 

def permute(lst, l, r):
    if l==r:            
        solution = ''.join(lst)
        if solution not in result:  #if characters in the strings are not duplicate
            total_permutations[0]+=1
            result.append(''.join(lst))
    else:
        for i in range(l,r+1):
            lst[l], lst[i] = lst[i], lst[l]   #Swap
            permute(lst,l+1,r)                # Calling Recursive Function
            lst[l], lst[i] = lst[i], lst[l]  # backtrack 

result = []  # Storing total permutations of a string
total_permutations = [0]  # Count total permutations
def string_permutaions(string,hint=False):
    start = time.time()
    if hint:
        string_permutaions_hint()
    n = len(string)
    lst = list(string) #covert string to list
    permute(lst,0,n-1) 
    end = time.time()
    print("Time Taken: ",end-start)
    print("Total Permutations: ",total_permutations)
    return result

def string_permutaions_hint():
    message="""
                                Print All Permutations Of A Given String 
    ------------------------------------------------------------------------------------------
    Purpose : In this problem, we are given a string. Our task is to print all permutations 
    of a given string.
    Method : Backtracking

    Time Complexity : O(n*n!)

    Hint :
    Apply Backtracking to find permutations of a given string.

    Pseudocode: 
    1. Define a string.
    2. Fix a character and swap the rest of the characters.
    3. Call the recursive function for rest of the characters.
    4. Backtrack and swap the characters again.

    Visualization:
    Recursion Tree for Permutations of String "ABC"
    * represents fixed characters
                                                   +---+---+---+
                                                   | A | B | C |
                                                   +---+---+---+
                                                         |
                        --------------------------------------------------------------------
             swap A,A   |                   swap A,B     |                   swap A,C      |
                +---+---+---+                      +---+---+---+                      +---+---+---+                
                |*A | B | C |                      |*B | A | C |                      |*C | B | A |
                +---+---+---+                      +---+---+---+                      +---+---+---+
        A  fixed      |                     B  fixed     |                  C  fixed        |
            ---------------------              ---------------------              ---------------------          
  swap B,B  |         swap B,C  |     swap A,A |         swap A,C  |     swap B,B |         swap B,A  |
        +---+---+---+  +---+---+---+         +---+---+---+  +---+---+---+      +---+---+---+  +---+---+---+
        |*A |*B | C |  |*A |*C | B |         |*B |*A | C |  |*B |*C | A |      |*C |*B | A |  |*C |*A | B | 
        +---+---+---+  +---+---+---+         +---+---+---+  +---+---+---+      +---+---+---+  +---+---+---+
        AB  fixed      AC  fixed             BA  fixed      BC  fixed          CB  fixed      CA  fixed    
  
  FINAL RESULT = ABC, ACB, BAC, BCA, CBA, CAB

    Learn More:
    - Backtracking - https://en.wikipedia.org/wiki/Backtracking
    - Permutations - https://en.wikipedia.org/wiki/Permutation
       
    """
    print_msg_box(message)

# print(string_permutaions("ABCA",True))
  