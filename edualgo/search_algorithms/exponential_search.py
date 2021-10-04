import time

from __init__ import print_msg_box

# binary search algorithm
def binary_search(arr, left, right, search):
    if(left > right):
        return -1
    
    mid = (left + right)//2
    
    if(search == arr[mid]):
        return mid
    elif(search < arr[mid]):
        return binary_search(arr, left, mid - 1, search)
    else:
        return binary_search(arr, mid + 1, right, search)

# exponential search algorithm
def exponential_search(arr, n, search, hint=False):
    start = time.time()
    
    if(arr[n-1]<search):
        return -1
    
    bound = 1
    
    while((bound < n) and (arr[bound] < search)):
        bound *= 2
        
    return binary_search(arr, bound//2, min(bound, n), search)
                    
    end = time.time()
    
    if (hint is True):
        exponential_search_hint()
    print("Exponential Search Runtime = {}".format(end - start))

def exponential_search_hint():
    message = """
    Exponential Search
    ------------------------------------
    Purpose: Searching a required number
    Method: Iterating, Comparing
    Time Complexity: O(1) for the best case. O(log2 i) for average or worst case. 
                     (Where i is the location where search key is present)
    Hint:
        Exponential search is also known as doubling or galloping search.
        This mechanism is used to find the range where the search key may present.
        If L and U are the upper and lower bound of the list, then L and U both are the power of 2.
        For the last section, the U is the last position of the list.
        For that reason, it is known as exponential.
        After finding the specific range, it uses the binary search technique to find the exact location of the search key.
        
    Pseudocode:
        # binary search algorithm
        def binary_search(arr, left, right, search):
            if(left > right)
                return -1

            mid = (left + right)//2

            if(search == arr[mid])
                return mid
            else if(search < arr[mid])
                return binary_search(arr, left, mid - 1, search)
            else
                return binary_search(arr, mid + 1, right, search)

        # exponential search algorithm
        def exponential_search(arr, n, search):
            if(arr[n-1]<search):
                return -1
        
            bound = 1

            while((bound < n) and (arr[bound] < search))
                bound *= 2

            return binary_search(arr, bound//2, min(bound, n), search)
    
    Visualization:
    Number to Search => search = 233
    Steps to be jumped => bound = 2*bound, where bound = 1 (initially)
    
    Given Array:
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    
    Calls Exponential Search:
    First Iteration (bound = 1):
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    [checking if bound < 16 and arr[1] < search, which is true so going on the next iteration]
    
    Second Iteration (bound = 2):
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    [checking if bound < 16 and arr[2] < search, which is true so going on the next iteration]
    
    Third Iteration (bound = 4):
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    [checking if bound < 16 and arr[4] < search, which is true so going on the next iteration]
    
    Fourth Iteration (bound = 8):
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    [checking if bound < 16 and arr[8] < search, which is true so going on the next iteration]
    
    Fifth Iteration (bound = 16):
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +---+---+---+---+---+---+---+----+----+----+----+----+-----+-----+-----+-----+
    [checking if bound < 16, which is not true so going to call Binary Search]
    
    Calls Exponential Search:
    
    1st Call:
    Values: arr = [21, 34, 55, 89, 144, 233, 377, 610], left = bound//2 = 8, right = min(bound, n) = 16, search = 233
    
    mid value = 12 (=(left+right)//2)
    
    +----+----+----+----+-----+-----+-----+-----+
    | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 |
    +----+----+----+----+-----+-----+-----+-----+
    [checking if arr[mid] == search, which is not true so going to call Binary Search]
    
    2nd Call:
    Values: arr = [233, 377, 610], left = mid+1 = 13, right = 16, search = 233
    
    mid value = 14 (=(left+right)//2)
    
    +-----+-----+
    | 233 | 377 |
    +-----+-----+
    [checking if arr[14] == search, which is not true so going to call Binary Search]
    
    3rd Call:
    Values: arr = [233, 377, 610], left = 13, right = mid-1 = 13, search = 233
    
    mid value = 13 (=(left+right)//2)
    
    +-----+
    | 233 |
    +-----+
    [checking if arr[13] == search, which is true so the search returns location of search in the array.]
    
    If no element in the array matched search = 233 then it would return "Not found!"
    
    Learn More Here - https://en.wikipedia.org/wiki/Exponential_search
    """
    print_msg_box(message)