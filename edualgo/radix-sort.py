import time

from __init__ import print_msg_box

def counting_sort(array, unit):
    n = len(array)
    output = [0]*n
    count = [0]*10
    
    for i in array:
        pos = (i/unit) 
        count[int(pos%10)] +=1

    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        pos = (array[i]/unit)
        output[count[int(pos%10)]-1] = array[i]
        count[int(pos%10)]-=1

    for i in range(n): 
        array[i] = output[i] 


def radix_sort(array, hint = False):
    start = time.time()
    maxval = max(array)
    unit = 1
    while maxval//unit > 0:
        counting_sort(array, unit)
        unit*=10
    end = time.time()
    if (hint is True):
        radix_sort_hint()
    print("Radix Sort Runtime = {}".format(end - start))
    return array



def radix_sort_hint():
    message = """
    Radix Sort
    ------------------------------------
    Purpose: Sorting a given array
    Method: Distributing, Non Comparing
    Time Complexity: Sorts in O(n+k) time when elements are in the range from 1 to k.
    Hint:
        From the given array, we sort the elements based on the i'th digit by performing counting sort on it until the unit value exceeds the maximum value in the array.
        Radix sort uses counting sort as a sub routine to sort elements.

    Pseudocode:
        Counting-Sort(A, n, unit)
            for j = 1 to d do
                int count[10] = {0};
                for i = 0 to n do
                    count[key of ((A[i]/unit)%10) in pass j]++
                for k = 1 to 10 do
                    count[k] = count[k] + count[k-1]
                for i = n-1 downto 0 do
                    result[count[key of ((A[i]/unit)%10)] ] = A[j]
                    count[key of(((A[i]/unit)%10)]--
                for i= n-1 to 0 do
                    A[i] = result[i]
            end for(j)
        end func 

        Radix-Sort(A)
            unit = 1
            while unit < max(A)
                Counting-Sort(A, unit)
                unit*=10

    
    Visualization:
    
    Given Array :
    +-----+----+----+----+-----+----+---+----+
    | 170 | 45 | 75 | 90 | 802 | 24 | 2 | 66 | 
    +-----+----+----+----+-----+----+---+----+
    
    First Iteration (unit = 1):

    +---+---+---+---+---+---+---+---+
    | 0 | 5 | 5 | 0 | 2 | 4 | 2 | 6 | 
    +---+---+---+---+---+---+---+---+

    Count Array
           +---+---+---+---+---+---+---+---+---+---+
    Count  | 2 | 0 | 2 | 0 | 1 | 2 | 1 | 0 | 0 | 0 |
           +---+---+---+---+---+---+---+---+---+---+
    Index  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |


    Cumilative Count Array
    +---+---+---+---+---+---+---+---+---+---+
    | 2 | 2 | 4 | 4 | 5 | 7 | 8 | 8 | 8 | 8 |
    +---+---+---+---+---+---+---+---+---+---+

    From the first iteration array, we take each value as the index of the cumilative count array and that element provides the position in the result array.
    Once it is placed, the value in the cumilative count array, reduces by one.

    Example - First Iteration Array -> Value : 66
    Pos = (66/1)
    Result[Count[int(Pos%10)]-1] = Result[Count[6]-1] = Result[7] = 66

    Result Array
    +---+---+---+---+---+---+---+---+---+----+
    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 66 |
    +---+---+---+---+---+---+---+---+---+----+

    Updated Cumilative Array 
    +---+---+---+---+---+---+---+---+---+---+
    | 2 | 2 | 4 | 4 | 5 | 7 | 8 | 8 | 8 | 7 |
    +---+---+---+---+---+---+---+---+---+---+

    Final Result Array after First Iteration
    +-----+----+-----+---+----+----+----+----+
    | 170 | 90 | 802 | 2 | 24 | 45 | 75 | 66 |
    +-----+----+-----+---+----+----+----+----+


    Second Iteration (unit = 10):

    +---+---+---+---+---+---+---+---+
    | 7 | 9 | 0 | 0 | 2 | 4 | 7 | 6 | 
    +---+---+---+---+---+---+---+---+

    Count Array
           +---+---+---+---+---+---+---+---+---+---+
    Count  | 2 | 0 | 1 | 0 | 1 | 0 | 1 | 2 | 0 | 1 |
           +---+---+---+---+---+---+---+---+---+---+
    Index  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |


    Cumilative Count Array
    +---+---+---+---+---+---+---+---+---+---+
    | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 7 | 7 | 8 |
    +---+---+---+---+---+---+---+---+---+---+

    Final Result Array after Second Iteration
    +-----+---+----+----+----+-----+----+----+
    | 802 | 2 | 24 | 45 | 66 | 170 | 75 | 90 |
    +-----+---+----+----+----+-----+----+----+

    Third Iteration (unit = 100):

    +---+---+---+---+---+---+---+---+
    | 8 | 0 | 0 | 0 | 0 | 1 | 0 | 6 | 
    +---+---+---+---+---+---+---+---+

    Count Array
           +---+---+---+---+---+---+---+---+---+---+
    Count  | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
           +---+---+---+---+---+---+---+---+---+---+
    Index  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |


    Cumilative Count Array
    +---+---+---+---+---+---+---+---+---+---+
    | 6 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 8 | 8 |
    +---+---+---+---+---+---+---+---+---+---+

    Final Result Array after Third (And Final) Iteration
    +---+----+----+----+----+----+-----+-----+
    | 2 | 24 | 45 | 66 | 75 | 90 | 170 | 802 |
    +---+----+----+----+----+----+-----+-----+


    Learn More Here - https://en.wikipedia.org/wiki/Radix_sort
    """
    
    print_msg_box(message)

