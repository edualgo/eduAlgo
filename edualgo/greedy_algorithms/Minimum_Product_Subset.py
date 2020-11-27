from __init__ import print_msg_box

#Minimun product subset of an array

def min_product_subset(array, hint=False):
   
    n = len(array)  # length of the array
    print(array)

    int_neg = 0
    int_pos = 0
    int_zero = 0
    max_neg = float('-inf')
    min_pos = float('inf')
    prod = 1

    if n == 1:
        print(array[0])

    for i in range(0, n):
        # counting number of zero
        if array[i] == 0:
            int_zero = int_zero + 1
            continue

        # counting number of negative numbers
        if array[i] < 0:
            int_neg = int_neg + 1
            max_neg = max(max_neg, array[i])

        # counting number of positive numbers
        if array[i] > 0:
            int_pos = int_pos + 1
            min_pos = min(min_pos, array[i])

        prod = prod * array[i]

    if int_zero == n or (int_neg == 0 and int_zero > 0):
        print(0)

    if int_neg == 0:
        print(min_pos)

    if int_neg % 2 == 0:
        prod = int(prod / max_neg)
    print(prod)
          
    if(hint == True):
        min_product_subset_hint()
    return prod


def min_product_subset_hint():
    message = """
    Minimum Product Subset of an Array 
    ----------------------------------------------

    Purpose : Finding the minimum product of the subset ,from the following 
    subsets of an array
    Method : 
    Time Complexity : Worst Case - 0(n)

    Hint : Finding the least product obtained among all the subsets of the given array
    Given an array a, we have to find minimum product possible with the subset 
    of elements present in the array. The minimum product can be single element
    also.

    Pseudocode:
    -->Input: Set[], set_size
              1. Get the size of power set
                    power_set_size = pow(2, set_size)
                    min_product = INT
              2  Loop for counter from 0 to pow_set_size
                    (a) Loop for i = 0 to set_size
                        (i) Initialize product_temp to 1
                        (ii) If ith bit in counter is set
                                Print ith element from set for this subset
                                Update product_temp by multiplying with  ith element
                        (iii) Set max_product to min(min_product, product_temp)
                    (b) Print separator for subsets i.e., newline

    Visualization:
    
    Input Array : 
    
    +----+----+----+----+----+
    | -1 | -1 | -2 |  4 |  3 |
    +----+----+----+----+----+
    
    Step-1: Check if the length of the array = 1
        Yes --> Minimum sum product = arr[0]
        No --> Push to Step-2
        
    Step-2: Initializing 
            int_neg = 0(No.of negative numbers in array)  
            int_pos = 0(No.of positive numbers in array)
            int_zero = 0(No.of zeroes in array),  max_neg = float('-inf'),min_pos = float('inf'),
            prod = 1(initial product of subset)
            
        Initializing i = 0 :
            int_neg = 1, max_neg = -1,product = 1*(-1) = -1
        Initializing i = 1 :
            int_neg = 2, max_neg = -1,product = (-1)*(-1) = 1
        Initializing i = 2 :
            int_neg = 3, max_neg = -2,product = 1*(-2) = -2
        Initializing i = 3 :
            int_pos = 1, min_pos = 4,product = (-2)*4 = -8
        Initializing i = 4 :
            int_pos = 2, min_pos = 3,product = (-8)*4 = -24
            
    Step-3:
       a)  Check If there are all zeros or no negative number present :
                Yes --> Minimum sum product = 0
                No --> Go to (b)
       b)  Check If there are all positive :
                Yes --> Minimum sum product = min_pos
                No --> Go to (c)
       c) Check If there are even number of negative numbers :
                Yes --> Minimum sum product = Product/max_neg 
                No --> Minimum sum product = product
                
    Step-4:
        Prepare the output as "-24"      
       
    """
    print_msg_box(message)
