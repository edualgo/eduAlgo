import time

from __init__ import print_msg_box


# binary search algorithm
def binary_search(array, x, hint=False):
    # array is sorted
    dict1 = {array[i]: i for i in range(len(array))}
    array = sorted(array)
    flag= -1
    start = time.time()
    low = 0
    high = len(array) - 1
    while low <= high and x>=array[low] and x<=array[high]:
        if array[low] == x:
            flag= low
            break

        mid = int(low + high) / 2

        if array[mid] == x:
            flag= mid
            break

        if array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
    end = time.time()
    if (hint == True):
        binary_hint()
    print("Binary Runtime = {}".format(end - start))
    return dict1[array[flag]]


def binary_search_hint():
    message = """
    Binary Search
    ------------------------------------
    Purpose : searching a required number in a sorted uniformly distributed array
    SORTED ARRAY- Arranged in ascending order
    Method : Searching first in the position(index) that has maximum probability of having required element.
    Time Complexity: Best case- Ω(1)
                     Worst case- O(logn)
    Hint :
    Starting from 0th element of array[] and comparing every element to x search one by one.
Formula used :                         high+low
       Middle position(pos) =   int (------------)
                                          2
                                where low is the lowest index 
                                      high is the highest index 
                                      x is the number to be searched 
                                      arr[i] is the ith element in the given sorted array 
    Pseudocode:
        while low<=high and array[low]<=array[high]
            if array[low]==x
                return low
            *calculate middle position(pos) with formula above
            if array[pos]< x
                low = pos+1
            else
                high = pos-1 
    Visualization:
    Number to search => x=3
    Given Array : arr[]
index-   0     1     2     3
      +-----+-----+-----+-----+
      |  1  |  3  |  4  |  6  |
      +-----+-----+-----+-----+
    First Iteration :
    +-----+-----+-----+-----+    low = 0            high = 3
    |  1  |  2  |  3  |  6  |    arr[low] = 1       arr[high] = 6
    +-----+-----+-----+-----+
    pos = int(0+3/2) = 1
  =>It will check at arr[pos]==x or not which is not and arr[pos]<x 
  => low = pos+1 = 2
    Second Iteration :
    +-----+-----+-----+-----+    low = 2            high = 3
    |  1  |  3  |  4  |  6  |    arr[low] = 3       arr[high] = 6
    +-----+-----+-----+-----+
    pos = int(2+3/2) = 2 
  =>It will check at arr[pos]==x which is true 
  => It will return 2
    If no element in the array matched x=3 then it would return -1
    Learn More Here - https://www.geeksforgeeks.org/interpolation-search/
    """
    print_msg_box(message)
