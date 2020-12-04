import time

from __init__ import print_msg_box

# jump search algorithm
def jump_search(arr, n, search, hint=False):
    start = time.time()
    
    i = 0
    loc = -1
    step = math.floor(math.sqrt(n))
    for i in range(0, n, step-1):
        if(arr[i]==search):
            loc = i
            break
        elif(arr[i]<search):
            continue
        elif(arr[i]>search):
            j = i
            j -= (step-1)
            for k in range(j+1, i):
                if(arr[k]==search):
                    loc = k
                    break
                    
    end = time.time()
    
    if (hint == True):
        jump_search_hint()
    print("Jump Search Runtime = {}".format(end - start))
    
    return loc


def jump_search_hint():
    message = """
    Jump Search
    ------------------------------------
    Purpose: Searching a required number
    Method: Iterating, Comparing
    Time Complexity: The optimal size of a block to be jumped is (√n).
                     This makes the time complexity of Jump Search O(√n).
    Hint:
        Starting from 0th element of arr[], we comparing fewer elements (than linear search) by jumping ahead by fixed steps.
    Pseudocode:
        loc = -1
        step = math.floor(math.sqrt(n))
        for i in range[0,length of array,step to jump]:
            if(arr[i]==search)
                loc = i
                break
            else if(arr[i]<search)
                continue
            else if(arr[i]>search)
                j = i
                j -= (step-1)
                for k in range[j+1, i]
                    if(arr[k]==search)
                        loc = k
                        break
        if(loc<0):
            return "Not found!"
        else:
            return loc
    
    Visualization:
    Number to Search => search = 233
    Steps to be jumped = √n, where n = size of the array = √16 = 4
    
    Given Array :
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    
    First Iteration (i = 0):
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    [checking if arr[0] > search, which is not true so going on the next iteration]
    
    Second Iteration (i = 3):
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    [checking if arr[3] > search, which is not true so going on the next iteration]
    
    Third Iteration (i = 6):
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    [checking if arr[6] > search, which is not true so going on the next iteration]
    
    Fourth Iteration (i = 9):
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    [checking if arr[9] > search, which is not true so going on the next iteration]
    
    Fifth Iteration (i = 12):
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    [checking if arr[12] > search, which is not true so going on the next iteration]
    
    Sixth Iteration (i = 15):
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    [checking if arr[15] > search, which is true so we go to for loop as linear search starts from i = 13 and ends at i = 14]
    
    First Sub - Iteration (j = 13)
    +-----+-----+-----+
    | 233 | 377 | 610 |
    +-----+-----+-----+
    [checking if arr[13] == search, which is true so the search returns location of search in the array.]
    
    If no element in the array matched search = 233 then it would return "Not found!"
    
    Learn More Here - https://en.wikipedia.org/wiki/Jump_search
    """
    print_msg_box(message)
