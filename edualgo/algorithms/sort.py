import time
import numpy as np
from itertools import permutations

from . import print_msg_box


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
        return self.merge_sorted_lists(self.merge_sort_impl(arr[:(len(arr)//2)]), self.merge_sort_impl(arr[(len(arr)//2):]))

def merge_sort(arr, hint=False):
    start = time.time()
    result = self.merge_sort_impl(arr)
    end = time.time()
    print("Merge Sort Runtime = {}".format(end-start))
    if(hint==True):
        self.merge_sort_hint()
    return result

def merge_sort_hint():
    message ="""
    merge Sort
    ------------------------------------

    Purpose : sorting in increasing order
    Method : Break into two halves and get these lists sorted, then merge these sorted halves into one sorted list.

    Time Complexity: Worst Case - O(n*log(n))

    Hint :
    We break the list into halfs until we have single element lists(since there is only one elemnt they are sorted.)
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
