import time
import numpy as np
from itertools import permutations

from .__init__ import print_msg_box


# bubble sort algorithm
def bubble_sort(arr,hint=False):
    start = time.time()
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
            print(arr)
    end = time.time()
    print("Bubble Sort Runtime = {}".format(end-start))
    if(hint == True):
        bubble_sort_hint()
    return arr

def bubble_sort_hint():
    message ="""
    Bubble Sort
    ------------------------------------

    Purpose : sorting in increasing order
    Method : Bubble Making, Swapping

    Time Complexity: Worst Case - O(n^2)

    Hint :
    Try to kick out the greater value to the rightmost position by using loops
    and value swapping.

    Pseudocode:
    --> for i in [0,length of array]
            for j in [0,length of array - 1]
                if(array[j] > array[i])
                    swap array[j] & array[i]

    Visualization:

    Given Array :

    +-----+-----+-----+
    |  5  |  4  |  3  |
    +-----+-----+-----+

    First Iteration :

    +-----+-----+-----+
    |  4  |  5  |  3  |
    +-----+-----+-----+

    Second Iteration :

    +-----+-----+-----+
    |  4  |  3  |  5  |
    +-----+-----+-----+

    Third Iteration :

    +-----+-----+-----+
    |  3  |  4  |  5  |
    +-----+-----+-----+

    Learn More Here - https://en.wikipedia.org/wiki/Bubble_sort
    """
    print_msg_box(message)

# selection Sort Algorithm
def selection_sort(arr,hint=False):
    start = time.time()
    for i in range(len(arr)-1):
        minimum = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum],arr[i] = arr[i],arr[minimum]
        print(arr)
    end = time.time()
    print("Selection Sort Runtime = {}".format(end-start))
    if(hint==True):
        selection_sort_hint()
    return arr

def selection_sort_hint():
    message ="""
    selection Sort
    ------------------------------------

    Purpose : sorting in increasing order
    Method : Pick Up minimum, swap with minimum

    Time Complexity: Worst Case - O(n^2)

    Hint :
    In every iteration the minimum element from the unsorted subarray is picked and
    moved to the sorted subarray.

    Pseudocode:
    --> for i in [0,length of array]
            minimum = i
            for j in [i+1,length of array]
                if arr[j] < arr[minimum]
                    minimum = j
            swap arr[i] & arr[minimum]

    Visualization:

    Given Array :

    +-----+-----+-----+
    |  5  |  4  |  3  |
    +-----+-----+-----+

    We have two buckets,

    |              |        |              |
    |   Unsorted   |        |    sorted    |
    |              |        |              |
    |    5,4,3     |        |     empty    |
     --------------          --------------

    Select the minimum from the unsorted bucket and put that in sorted bucket

    |              |        |              |
    |   Unsorted   |        |    sorted    |
    |              |        |              |
    |     5,4      |        |      3       |
     --------------          --------------

    Again select the minimum from the unsorted bucket and put that in
    sorted bucket

    |              |        |              |
    |   Unsorted   |        |    sorted    |
    |              |        |              |
    |      5       |        |     3,4      |
     --------------          --------------

    Repeat the same till the unsorted bucket is empty

    |              |        |              |
    |   Unsorted   |        |    sorted    |
    |              |        |              |
    |              |        |     3,4,5    |
     --------------          --------------

    Finally you have the sorted array.

    Learn More Here - https://en.wikipedia.org/wiki/Selection_sort
    """
    print_msg_box(message)

def bogo_sort( arr, asc=True, hint=False):
    n = len(arr)

    def is_sorted(n, array, ascend=asc):
        if ascend:
            for i in range(n-1):
                if array[i] > array[i+1]:
                    return False
        else:
            for i in range(n-1):
                if array[i] < array[i+1]:
                    return False
        return True

    permut = permutations([i for i in range(n)], n)

    start = time.time()
    for seq in permut:
        tmp = np.array(arr)

        if is_sorted(n, tmp[list(seq)], asc):
            sorted_arr = tmp[list(seq)]
    end = time.time()
    print("Bogo Sort Runtime = {}".format(end-start))

    if hint:
        bogo_sort_hint()

    return sorted_arr

def bogo_sort_hint():
    message ="""
    Bogo Sort
    ------------------------------------

    Purpose : Sorting in increasing/decreasing order as specified by asc argument
    Method : Choose the sorted one among all the permutations

    Time Complexity: Worst Case - O(n!)

    Hint :
    Generate all the possible permutations of the elements in the array
    and check which is sorted.

    Pseudocode:
    --> for sequence in all_permutations
            if is_sorted(array[sequence])
                return array[sequence]

    Visualization:

    Given Array :

    +-----+-----+-----+
    |  5  |  4  |  3  |
    +-----+-----+-----+

    First Permutation :

    +-----+-----+-----+
    |  5  |  4  |  3  |
    +-----+-----+-----+
    Is it sorted? NO

    Second Permutation :

    +-----+-----+-----+
    |  5  |  3  |  4  |
    +-----+-----+-----+
    Is it sorted? NO

    Third Permutation :

    +-----+-----+-----+
    |  4  |  5  |  3  |
    +-----+-----+-----+
    Is it sorted? NO

    Third Permutation :

    +-----+-----+-----+
    |  4  |  3  |  5  |
    +-----+-----+-----+
    Is it sorted? NO

    Third Permutation :

    +-----+-----+-----+
    |  3  |  4  |  5  |
    +-----+-----+-----+
    Is it sorted? YES

    Learn More Here - https://en.wikipedia.org/wiki/Bogosort
    """

    print_msg_box(message)

# insertion Sort Algorithm
def insertion_sort(arr,hint=False):
    start = time.time()
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)
    end = time.time()
    print("Insertion Sort Runtime = {}".format(end-start))
    if(hint==True):
        insertion_sort_hint()
    return arr

def insertion_sort_hint():
    message ="""
    Insertion Sort
    ------------------------------------

    Purpose : sorting in increasing order
    Method : insert element in correct position, pushing greater elements ahead

    Time Complexity: Worst Case - O(n^2)

    Hint :
    In every iteration the ith element is inserted into the correct place
    and the elements greater than ith element are moved one position ahead of
    current position.

    Pseudocode:
    --> for i in [1,length of array]
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

    Visualization:

    Given Array :

    +-----+-----+-----+
    |  5  |  4  |  3  |
    +-----+-----+-----+

    First Iteration :

    +-----+-----+-----+
    |  4  |  5  |  3  |
    +-----+-----+-----+

    Second Iteration :

    +-----+-----+-----+
    |  3  |  4  |  5  |
    +-----+-----+-----+

    Finally you have the sorted array.

    Learn More Here - https://en.wikipedia.org/wiki/Insertion_sort
    """
    print_msg_box(message)

def merge_sorted_lists(l1, l2):
    arr=list()
    i=j=0
    while i < len(l1) or j < len(l2):
        if j >= len(l2):
            arr.append(l1[i])
            i += 1
            continue
        if i >= len(l1):
            arr.append(l2[j])
            j += 1
            continue;
        if l1[i] < l2[j]:
            arr.append(l1[i])
            i += 1
        else:
            arr.append(l2[j])
            j += 1
    return arr

def merge_sort_impl(arr):
    if len(arr) <= 1:
        return arr
    else:
        return merge_sorted_lists(merge_sort_impl(arr[:(len(arr)//2)]), merge_sort_impl(arr[(len(arr)//2):]))

def merge_sort(arr, hint=False):
    start = time.time()
    result = merge_sort_impl(arr)
    end = time.time()
    print("Merge Sort Runtime = {}".format(end-start))
    if(hint==True):
        merge_sort_hint()
    return result

def merge_sort_hint():
    message ="""
    merge Sort
    ------------------------------------

    Purpose : sorting in increasing order
    Method : Break into two halves and get these lists sorted, then merge these sorted halves into one sorted list.

    Time Complexity: Worst Case - O(n*log(n))

    Hint :
    We break the list into halves until we have single element lists(since there is only one element they are sorted.)
    then we merge these lists pair by pair such that the merged list is sorted.

    Pseudocode:
    --> if len(arr) <= 1:
            return arr
        else:
            return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

    Visualization:

    Given Array :

    +-----+-----+-----+-----+-----+
    |  5  |  4  |  3  |  7  |  2  |
    +-----+-----+-----+-----+-----+

    Break list into halves until you have one list for each array

    +-----+-----+    +-----+-----+-----+
    |  5  |  4  |    |  3  |  7  |  2  |
    +-----+-----+    +-----+-----+-----+

    +-----+    +-----+    +-----+    +-----+-----+
    |  5  |    |  4  |    |  3  |    |  7  |  2  |
    +-----+    +-----+    +-----+    +-----+-----+

    +-----+    +-----+    +-----+    +-----+    +-----+
    |  5  |    |  4  |    |  3  |    |  7  |    |  2  |
    +-----+    +-----+    +-----+    +-----+    +-----+

    Now we merge pair and maintain the sorted order:

    +-----+    +-----+    +-----+    +-----+-----+
    |  5  |    |  4  |    |  3  |    |  2  |  7  |
    +-----+    +-----+    +-----+    +-----+-----+

    +-----+-----+    +-----+    +-----+-----+
    |  4  |  5  |    |  3  |    |  2  |  7  |
    +-----+-----+    +-----+    +-----+-----+

    +-----+-----+    +-----+-----+-----+
    |  4  |  5  |    |  2  |  3  |  7  |
    +-----+-----+    +-----+-----+-----+

    +-----+-----+-----+-----+-----+
    |  2  |  3  |  4  |  5  |  7  |
    +-----+-----+-----+-----+-----+

    Finally you have the sorted array.

    Learn More Here - https://en.wikipedia.org/wiki/Merge_sort
    """
    print_msg_box(message)
  
# Quick Sort Partitioning Logic.
def partition(arr, low, high):
    # pivot is the element which will be placed at the correct position.
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] < pivot:
           i += 1
           arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# Function to perform Quick sort.
def quick_sort(arr, low, high, hint=False):
    if len(arr) == 1:
        return arr
    if low < high:
        partition_index = partition(arr, low, high)

        quick_sort(arr, low, partition_index-1) # Before the partition index
        quick_sort(arr, partition_index+1, high) # After the partition index

    if hint:
        quick_sort_hint()

# Helper function to call the algorithm, and calculate the computation time.
def quick_sort_helper():
    arr = [10, 7, 8, 9, 1, 5]
    start = time.time()
    quick_sort(arr, 0, len(arr)-1)
    end = time.time()
    print("Quick Sort Runtime = {}".format(end-start))

def quick_sort_hint():
    message = """
    Quick Sort
    ------------------------------------

    Purpose : sorting in increasing order
    Method : Given an array and an element x of array as pivot, put x at its correct position in sorted array and put
    all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x.

    Time Complexity: Worst Case - O(n^2): The worst case occurs when the partition process always picks greatest or
    smallest element as pivot.

    Time Complexity: Average Case - O(n*log(n))

    Hint :
    Take the last element as pivot, place the pivot element at its correct position in sorted array, and place all
    smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot

    Pseudo Code:
    --> partition_index = partition(arr, low, high)

        quick_sort(arr, low, pi-1) # Before the partition index
        quick_sort(arr, pi+1, high) # After the partition index

    --> Partitioning Hint:
        for j in range(low, high):
            if arr[j] < pivot:
               i += 1
               swap (arr[i], arr[j])
               arr[i], arr[j] = arr[j], arr[i]

        swap (arr[i+1], arr[high])
        return i+1

    Visualization: (Illustrating the partition logic)

    Given Array :

    +-----+-----+-----+-----+-----+
    |  5  |  3  |  2  |  7  |  4  |
    +-----+-----+-----+-----+-----+

    Initializing i = -1, j = 0, pivot = arr[high] = 4. Traverse the array from low to high - 1 (ie 0 to 3).

    j = 0. i = -1. Since arr[j] > pivot, do nothing. No change in arr and i.
    +-----+-----+-----+-----+-----+
    |  5  |  3  |  2  |  7  |  4  |
    +-----+-----+-----+-----+-----+

    j = 1. i = -1. Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j]) ie swap (5, 3).
    +-----+-----+-----+-----+-----+
    |  3  |  5  |  2  |  7  |  4  |
    +-----+-----+-----+-----+-----+

    j = 2. i = 0. Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j]) ie swap (5, 2).
    +-----+-----+-----+-----+-----+
    |  3  |  2  |  5  |  7  |  4  |
    +-----+-----+-----+-----+-----+

    j = 3. i = 1. Since arr[j] > pivot, do nothing. No change in arr and i.
    +-----+-----+-----+-----+-----+
    |  3  |  2  |  5  |  7  |  4  |
    +-----+-----+-----+-----+-----+

    We come out of loop because j is now equal to high-1. Now we place pivot at correct position by swapping arr[i+1]
    and arr[high] (or pivot).
    +-----+-----+-----+-----+-----+
    |  3  |  2  |  4  |  7  |  5  |
    +-----+-----+-----+-----+-----+

    Now 4 is at its correct place. All elements smaller than 4 are before it and all elements greater than 4 are after
    it. Repeat this process for left and right side of partition index.

    Learn More Here - https://en.wikipedia.org/wiki/Quicksort
    """
    print_msg_box(message)

# Heap Sort

def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest)

def heap_sort(arr,hint=False):
    start = time.time()
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0)
    
    print(arr)
    end = time.time()
    print("Heap Sort Runtime = {}".format(end-start))
    if(hint == True):
        heap_sort_hint()
    return arr

def heap_sort_hint():
    message ="""
    Heap Sort
    ------------------------------------

    Purpose : sorting in increasing order
    Method : Create Max Heap, Remove max root element and swap with last element, Repeat process

    Time Complexity: Time complexity of heapify is O(Logn). 
                     Time complexity of createAndBuildHeap() is O(n) 
                     and overall time complexity of Heap Sort is O(nLogn).

    Hint :
    1. Build a max heap from the input data.
    2. At this point, the largest item is stored at the root of the heap. 
       Replace it with the last item of the heap followed by reducing the size of heap by 1. 
       Finally, heapify the root of the tree.
    3. Repeat step 2 while size of heap is greater than 1.  


    Visualization:

    Given Array :   +-----+-----+-----+-----+-----+
                    |  4  | 10  |  3  |  5  |  1  |
                    +-----+-----+-----+-----+-----+

                             ( 0 )
                            +------+
                            |  4   |         
                            +------+
                            /      \\
                    ( 1 )  /        \\ ( 2 )
                   +------+          +------+
                   |  10  |          |  3   |   
                   +------+          +------+
                   /      \\      
                  /        \\     
             +------+     +------+   
     ( 3 )   |  5   |     |  1   |  ( 4 ) 
             +------+     +------+                   

    -> The numbers in bracket represent the indices in the array 
       representation of data.

    Applying heapify procedure to index 1 :

                             ( 0 )
                            +------+
                            |  4   |         
                            +------+
                            /      \\
                    ( 1 )  /        \\ ( 2 )
                   +------+          +------+
                   |  10  |          |  3   |   
                   +------+          +------+
                   /      \\      
                  /        \\     
             +------+     +------+   
     ( 3 )   |  5   |     |  1   |  ( 4 ) 
             +------+     +------+                   

    Applying heapify procedure to index 0 :

                             ( 0 )
                            +------+
                            |  10  |         
                            +------+
                            /      \\
                    ( 1 )  /        \\ ( 2 )
                   +------+          +------+
                   |  5   |          |  3   |   
                   +------+          +------+
                   /      \\      
                  /        \\     
             +------+     +------+   
     ( 3 )   |  4   |     |  1   |  ( 4 ) 
             +------+     +------+                   

    -> The heapify procedure calls itself recursively to build heap
       in top down manner.
    
    Learn More Here - https://en.wikipedia.org/wiki/Heapsort
    """
    print_msg_box(message)
