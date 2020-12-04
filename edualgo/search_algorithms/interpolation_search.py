import time

from __init__ import print_msg_box


# interpolation search algorithm
def interpolation_search(array, x, hint=False):
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

        probe_pos = low + int(((float(high - low) / (array[high] - array[low])) * (x - array[low])))

        if array[probe_pos] == x:
            flag= probe_pos
            break

        if array[probe_pos] < x:
            low = probe_pos + 1

        else:
            high = probe_pos - 1
    end = time.time()
    if (hint == True):
        interpolation_search_hint()
    print("Interpolation Search Runtime = {}".format(end - start))
    return dict1[array[flag]]


def interpolation_search_hint():
    message = """
    Interpolation Search
    ------------------------------------
    Purpose : searching a required number in a sorted uniformly distributed array
    SORTED ARRAY- Arranged in ascending order
    Method : Searching first in the position(index) that has maximum probability of having required element.
    Time Complexity: Best case- Ω(log(log(n)))
                     Worst case- O(n)

    Hint :
    Starting from 0th element of array[] and comparing every element to x search one by one.

Formula used :                                    (high-low)
       Probable position(pos) =   low + int (--------------------) X (x-arr[low])
                                              (arr[high]-arr[low])

                                where low is the lowest index 
                                      high is the highest index 
                                      x is the number to be searched 
                                      arr[i] is the ith element in the given sorted array 
    Pseudocode:
        while low<=high and array[low]<=array[high]
            if array[low]==x
                return low
            *calculate probable position(pos) with formula above
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
    |  1  |  3  |  4  |  6  |    arr[low] = 1       arr[high] = 6
    +-----+-----+-----+-----+
    pos = 0+int((3-0)/(6-1))*(3-1) = 0 
  =>It will check at arr[pos]==x or not which is not and arr[pos]<x 
  => low = pos+1 = 1

    Second Iteration :
    +-----+-----+-----+-----+    low = 1            high = 3
    |  1  |  3  |  4  |  6  |    arr[low] = 3       arr[high] = 6
    +-----+-----+-----+-----+
    pos = 1+((3-1)/(6-3))*(3-3) = 1 
  =>It will check at arr[pos]==x which is true 
  => It will return 1

    If no element in the array matched x=3 then it would return -1

    Learn More Here - https://www.geeksforgeeks.org/interpolation-search/
    """
    print_msg_box(message)
