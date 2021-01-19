from .__init__ import print_msg_box,file_output
import time
import numpy as np
from itertools import permutations

class matrices:

    def rotateImage(self,img_arr,n,hint=False):
        if(hint==True):
            self.rotateImage_hint()
        for layer in range(int(n/2)):
            first = layer
            last = n-1-layer
            for i in range(first,last):
                offset = i - first
                top = img_arr[first][i]
                img_arr[first][i] = img_arr[last - offset][first]
                img_arr[last - offset][first] = img_arr[last][last - offset]
                img_arr[last][last - offset] = img_arr[i][last]
                img_arr[i][last] = top

    def rotateImage_hint(self):
        message = """
        Rotate The Image
        ------------------------------------

        Purpose :To rotate a N x N 2D array representing an image without
        using any external space
        Method : 2D array, time-space complexity

        Time Complexity : Worst Case - O(n^2), n = number of rows in a matrix
        Space Complexity : O(1)

        Hint :
        Try implementing rotation in layers

        Pseudocode :
        for layer in range(int(n/2)):
            first = layer
            last = n-1-layer
            for i in range(first,last):
                offset = i - first
                top = img_arr[first][i]
                img_arr[first][i] = img_arr[last - offset][first]
                img_arr[last - offset][first] = img_arr[last][last - offset]
                img_arr[last][last - offset] = img_arr[i][last]
                img_arr[i][last] = top

        Visualization:

        Given image :

        1  2  3           1  4  1
        4  8  9    --->   8  8  2
        1  8  9           9  9  3

        Find the pivot (if any) :

            1     2     3

                +---+
            4   | 8 |   9      ---> 8 is the constant position
                +---+

            1     8     9


        Rotate Layer Wise using temp variable :

                 +---+
            1    | 2 |     3
                 +---+
        +---+           +---+
        | 4 |     8     | 9 |   -----> rotate the highlighted layer in 90 degree
        +---+           +---+
                +---+
            1   | 8 |     9
                +---+

        Rotate Next layer :

            +---+       +---+
            | 1 |   4   | 3 |
            +---+       +---+
              8     8     2      -----> rotate the highlighted layer in 90 degree
            +---+       +---+
            | 1 |   9   | 9 |
            +---+       +---+

        Finally you have the desired rotated array.
        """
        print_msg_box(message)

    def setZeros(self,matrix,row,column):
        row_arr = [False] * row
        col_arr = [False] * column
        for i in range(row):
            for j in range(column):
                if(matrix[i][j] == 0):
                    row_arr[i] = True
                    col_arr[j] = True

        for i in range(row):
            if(row_arr[i]):
                for j in range(column):
                    matrix[i][j] = 0

        for i in range(column):
            if(col_arr[i]):
                for j in range(row):
                    matrix[j][i] = 0

class sorting:

    # bubble sort algorithm
    def bubble_sort(self,arr,file_name,hint=False,file=False):
        start = time.time()
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1] :
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                print(arr)
        end = time.time()
        print("Bubble Sort Runtime = {} seconds".format(end-start))
        if(hint == True):
            self.bubble_sort_hint(file_name,file)
        return arr

    def bubble_sort_hint(self,file_name,flag=False):
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
        if(flag == True):
            file_output(message,file_name)
        else:
            print_msg_box(message)

    # selection Sort Algorithm
    def selection_sort(self,arr,hint=False):
        start = time.time()
        for i in range(len(arr)-1):
            minimum = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j
            arr[minimum],arr[i] = arr[i],arr[minimum]
            print(arr)
        end = time.time()
        print("Selection Sort Runtime = {} seconds".format(end-start))
        if(hint==True):
            self.selection_sort_hint()
        return arr

    def selection_sort_hint(self):
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

    def bogo_sort(self,arr, asc=True, hint=False):
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
        print("Bogo Sort Runtime = {} seconds".format(end-start))

        if hint:
            self.bogo_sort_hint()

        return sorted_arr

    def bogo_sort_hint(self):
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
    def insertion_sort(self,arr,hint=False):
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
        print("Insertion Sort Runtime = {} seconds".format(end-start))
        if(hint==True):
            self.insertion_sort_hint()
        return arr

    def insertion_sort_hint(self):
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

    def merge_sorted_lists(self,l1, l2):
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
                continue
            if l1[i] < l2[j]:
                arr.append(l1[i])
                i += 1
            else:
                arr.append(l2[j])
                j += 1
        return arr

    def merge_sort_impl(self,arr):
        if len(arr) <= 1:
            return arr
        else:
            return self.merge_sorted_lists(self.merge_sort_impl(arr[:(len(arr)//2)]), self.merge_sort_impl(arr[(len(arr)//2):]))

    def merge_sort(self,arr, hint=False):
        start = time.time()
        result = self.merge_sort_impl(arr)
        end = time.time()
        print("Merge Sort Runtime = {} seconds".format(end-start))
        if(hint==True):
            self.merge_sort_hint()
        return result

    def merge_sort_hint(self):
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
    def partition(self,arr, low, high):
        # pivot is the element which will be placed at the correct position.
        pivot = arr[high]
        i = low-1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    # Function to perform Quick sort.
    def quick_sort_helper(self,arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            partition_index = self.partition(arr, low, high)

            self.quick_sort_helper(arr, low, partition_index-1) # Before the partition index
            self.quick_sort_helper(arr, partition_index+1, high) # After the partition index

    # Helper function to call the algorithm, and calculate the computation time.
    def quick_sort(self,arr,hint=False):
        if(hint == True):
            self.quick_sort_hint()
        start = time.time()
        self.quick_sort_helper(arr, 0, len(arr)-1)
        end = time.time()
        print("Quick Sort Runtime = {} seconds".format(end-start))

    def quick_sort_hint(self):
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

    def heapify(self,arr, n, i): 
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
            self.heapify(arr, n, largest)

    def heap_sort(self,arr,hint=False):
        start = time.time()
        n = len(arr) 
    
        # Build a maxheap. 
        for i in range(n//2 - 1, -1, -1): 
            self.heapify(arr, n, i) 
    
        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i] # swap 
            self.heapify(arr, i, 0)
        
        print(arr)
        end = time.time()
        print("Heap Sort Runtime = {} seconds".format(end-start))
        if(hint == True):
            self.heap_sort_hint()
        return arr

    def heap_sort_hint(self):
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

class string_algorithms:

    def isUnique(self,input_string,hint=False):
        mapp = []
        for i in input_string:
            if i not in mapp:
                mapp.append(i)
        if(hint == True):
            self.isUnique_hint()
        return len(mapp) == len(input_string)

    def isUnique_hint(self):
        message ="""
        Unique Character Checking
        ------------------------------------

        Purpose : checking if all the characters in a given string are unique
        Method : list comprehension

        Time Complexity: Worst Case - O(n), n = length of the input string

        Hint :
        How about using the inbuilt list data structure ?

        Pseudocode:
        --> create an empty list named mapp
        --> for i in input string
                if i not in mapp
                    add i to the empty list
        --> The string is unique only when the
            length of the map after the total
            iterations is same as that of the
            length of the input string

        Visualization:

        Given String :

        "aabcc"

        Empty List:

        ----------------
        |                |
        ----------------

        after first iteration :

        ----------------
        |       a        |
        ----------------

        after second iteration :

        ----------------
        |       a        |
        ----------------

        [because a was already in the list]

        after third iteration :

        ----------------
        |      a b       |
        ----------------

        Finally :

        ----------------
        |     a b c      |
        ----------------

        size = 3 which is not equal to length of "aabcc"

        Learn More about Lists Below -
        https://docs.python.org/3/tutorial/datastructures.html
        """
        print_msg_box(message)

    def isPermutation(self,input1,input2,hint=False):
        if(hint == True):
            self.isPermutation_hint()
        if(len(input1)!=len(input2)):
            return False
        mapp1 = []
        mapp2 = []
        for i in input1:
            mapp1.append(i)
        for j in input2:
            mapp2.append(j)
        mapp1.sort()
        mapp2.sort()

        return mapp1==mapp2

    def isPermutation_hint(self):
        message = """
        Two String Permutations
        ------------------------------------

        Purpose : checking if one string is consisting of the permutation of
        the characters in the other string
        Method : list comprehension

        Time Complexity: Worst Case - O(n), n = length of the strings

        Hint :
        How about using two inbuilt list data structure ?

        Pseudocode:
        --> check if length(string1) != len(string2)
                return False
        --> create two empty lists named mapp1 & mapp2
        --> for i in input string 1
                add i to mapp1
        --> for i in input string 2
                add i to mapp2
        --> sort mapp1
        --> sort mapp2
        --> return true if mapp1 and mapp2 are equal

        Visualization:

        Given Two String :

        "aabcc"

        "abcac"

        Two Empty List:

            List 1                       List 2
        ----------------            ----------------
        |                |          |                |
        ----------------            ----------------

        After Filling Lists :

            List 1                       List 2
        ----------------            ----------------
        |    a a b c c   |          |    a b c a c   |
        ----------------            ----------------

        Applying sort function :

            List 1                       List 2
        ----------------            ----------------
        |    a a b c c   |          |   a a b c c    |
        ----------------            ----------------

        Final check :

        ------------------            +------+
        | List 1 == List 2 |  -------> | True |
        ------------------            +------+


        Learn More about Lists Below -
        https://docs.python.org/3/tutorial/datastructures.html
        """
        print_msg_box(message)

    def URLify(self,input_str,key,hint=False):
        if(hint==True):
            self.URLify_hint()
        input2 = ""
        for i in range(len(input_str)):
            if(input_str[i] != ' '):
                input2+=input_str[i]
            elif((input_str[i]==' ') and (input_str[i+1] == ' ')):
                return input2
            elif((input_str[i]==' ') and (input_str[i+1] != ' ')):
                input2 += key
        return input2

    def URLify_hint(self):
        message = """
        Making a URL From a String
        ------------------------------------

        Purpose : Making a URL by replacing the spaces with a key value entered
        by the user
        Method : string manipulation

        Time Complexity : Worst Case - O(n), n = length of the string

        Hint :
        Take a blank string, and add data from the input string to the blank
        string to prepare the final URL

        Pseudocode :
        --> Take a blank string s2
        --> for i in [0,length of input string]
                if(not a whitespace)
                    add to s2
                elif(whitespace and next place is also whitespace)
                    return s2
                elif(whitespace and next place not whitespace)
                    add the key value to the blank string

        Visualization:

        Given String To Make URL :

        "Python is love"

        Key : "%20"

        Break The Given String :  /*/ ----> whitespace

        +--------+-------+----+-------+------+
        | Python |  /*/  | is |  /*/  | love |
        +--------+-------+----+-------+------+
            ^              ^             ^
            ^              ^             ^
            ^              ^             ^

            1              2             3

        We will take 1, 2 and 3 sucessively and in place of whitespaces we will
        concatenate the key value.

        Empty String Addition :

        +-+    +--------+   +-------+   +----+   +-------+   +------+
        | |  + | Python | + |  %20  | + | is | + |  %20  | + | love |
        +-+    +--------+   +-------+   +----+   +-------+   +------+

        Learn More about String Concatenation Below -
        https://en.wikipedia.org/wiki/Concatenation
        """
        print_msg_box(message)

    def isPalindromicPermutation(self,input1,hint=False):
        if(hint == True):
            self.isPalindromicPermutation_hint()
        mapp = {}
        for i in range(len(input1)):
            key = input1[i]
            if(key in mapp.keys()):
                mapp[key] += 1
            else:
                mapp.update({key:1})
        flag = 0
        for i in mapp.keys():
            if(mapp[i] %2 == 1):
                flag+=1
        return flag<=1

    def isPalindromicPermutation_hint(self):
        message = """
        Palindromic Permutation
        ------------------------------------

        Purpose :To check if the permutation of the characters in a string can
        make it palindromic
        Method : string manipulation, palindromic behaviour

        Time Complexity : Worst Case - O(n), n = length of the string

        Hint :
        Make a dictionary of characters and their repeatations.

        Pseudocode :
        --> Take a blank dictionary
        --> for i in [0,length of input string]
                key = input[i]
                if(key in dictionary)
                    dictionary[key]+=1
                else
                    push {key:1} inside dictionary
        --> Check if dictioary[i] %2 == 1

        Visualization:

        Given String :

        "abbca"

        Making a table using dictionary :

        Step 1 - create a blank dictionary - {}

        Step 2 - check if the key exists

                yes --> add 1

                no  --> push {key:1} inside the dictionary

        Step 3 - You have the following table

        +----------+----------------+
        |   key    |  repeatations  |
        +----------+----------------+
        |    a     |       2        |   --> rem = 0, flag = 0
        -----------------------------
        |    b     |       2        |   --> rem = 0, flag = 0
        -----------------------------
        |    c     |       1        |   --> rem = 0, flag = 1
        -----------------------------

        Step 4 - check reminder, set flag = 0, initially

        Step 5 - return boolean

        Learn More about Python Dictionaries Below -
        https://www.w3schools.com/python/python_dictionaries.asp
        """
        print_msg_box(message)

    def oneEditAwayInsert(self,input1,input2):
        index1 = 0
        index2 = 0
        while((index2 < len(input2)) and (index1 < len(input1))):
            if(input1[index1] != input2[index2]):
                if(index1 != index2):
                    return False
                index2+=1
            else:
                index1+=1
                index2+=1
        return True

    def oneEditAwayReplace(self,input1,input2):
        flag = False
        for i in range(len(input1)):
            if(input2[i]!=input1[i]):
                if(flag):
                    return False
                flag = True
        return True

    def oneEditAway(self,input1,input2,hint=False):
        if(hint==True):
            self.oneEditAway_hint()
        if(len(input1)==len(input2)):
            return  self.oneEditAwayReplace(input1,input2)
        elif(len(input1)+1==len(input2)):
            return  self.oneEditAwayInsert(input1,input2)
        elif(len(input1)-1==len(input2)):
            return  self.oneEditAwayInsert(input2,input1)
        return False

    def oneEditAway_hint(self):
        message = """
        One Edit Away
        ------------------------------------

        Purpose : Check if two strings are one edit (or zero) away,where edit
        means the following three methods,
            - inserting a character
            - removing a character
            - replacing a character

        Method : string manipulation

        Time Complexity : Worst Case - O(n), n = length of the greater string

        Hint :
        Divide the problem in three cases of insert, remove and replace
        and solve the problem.

        Pseudocode :

        For checking "replace" :

        --> flag = False
        --> for i in range(len(input1)):
                if(input2[i]!=input1[i]):
                    if(flag):
                        return False
                    flag = True

        For checking "insert" & "remove" :

        --> index1 = 0
        --> index2 = 0
        --> while((index2 < len(input2)) and (index1 < len(input1))):
                if(input1[index1] != input2[index2]):
                    if(index1 != index2):
                        return False
                        index2+=1
                    else:
                        index1+=1
                        index2+=1
                return True

        """
        print_msg_box(message)

    def compressedString(self,input1,hint=False):
        if(hint == True):
            self.compressedString_hint()
        mapp = {}
        output = ""
        for i in range(len(input1)):
            key = input1[i]
            if(key in mapp.keys()):
                mapp[key]+=1
            else:
                mapp.update({key:1})
        for key in mapp.keys():
            output = output + key + str(mapp[key])
        if(len(output) <= len(input1)):
            return output
        else:
            return input1

    def compressedString_hint(self):
        message = """
        Compress The String
        ------------------------------------

        Purpose :To compress the size of string by making a summary of the
        repeatation of the characters
        Method : string manipulation, python dictionary

        Time Complexity : Worst Case - O(n), n = length of the string

        Hint :
        Make a dictionary of characters and their repeatations. Finaally forge a
        new string and return it

        Pseudocode :
        --> Take a blank dictionary
        --> Take a blank string output
        --> for i in [0,length of input string]
                key = input[i]
                if(key in dictionary)
                    dictionary[key]+=1
                else
                    push {key:1} inside dictionary
        --> prepare the output string

        Visualization:

        Given String :

        "aabbcccdddeeef"

        Making a table using dictionary :

        Step 1 - create a blank dictionary - {}

        Step 2 - check if the key exists

                yes --> add 1

                no  --> push {key:1} inside the dictionary

        Step 3 - You have the following table

        +----------+----------------+
        |   key    |  repeatations  |
        +----------+----------------+
        |    a     |       2        |
        -----------------------------
        |    b     |       2        |
        -----------------------------
        |    c     |       3        |
        -----------------------------
        |    d     |       3        |
        -----------------------------
        |    e     |       3        |
        -----------------------------
        |    f     |       1        |
        -----------------------------

        Step 4 - prepare the output string as "a2b2c3d3e3f1"

        Learn More about Python Dictionaries Below -
        https://www.w3schools.com/python/python_dictionaries.asp
        """
        print_msg_box(message)

class search_algorithms:

    # linear search algorithm
    def linear_search(self,array, x, hint=False):
        start = time.time()
        flag=-1
        for i in range(len(array)):
            if array[i] == x:
                flag=i
        end = time.time()
        if (hint == True):
            self.linear_search_hint()
        print("Linear Search Runtime = {}".format(end - start))
        return flag


    def linear_search_hint(self):
        message = """
        Linear Search
        ------------------------------------
        Purpose : searching a required number
        Method : Iterating, Comparing
        Time Complexity: Worst Case - O(n)
        Hint :
        Starting from 0th element of array[] and comparing every element to x search one by one.
        Pseudocode:
        --> for i in range[0,length of array]
                    if(array[i]= x)
                        return i
            return "Not found"
        Visualization:
        Number to search => x=3
        Given Array :
        +-----+-----+-----+
        |  5  |  4  |  3  |
        +-----+-----+-----+
        First Iteration (i=0):
        +-----+-----+-----+
        |  5  |  4  |  3  |
        +-----+-----+-----+
        [checking if 5==x, which is not true so going on the next iteration]
        Second Iteration (i=1):
        +-----+-----+-----+
        |  5  |  4  |  3  |
        +-----+-----+-----+
        [checking if 4==x, which is not true so going on the next iteration]
        Third Iteration (i=2):
        +-----+-----+-----+
        |  5  |  4  |  3  |
        +-----+-----+-----+
        [checking if 3==x, which is true so the search returns location of x in the array ]
        If no element in the array matched x=3 then it would return "Not found"
        Learn More Here - https://en.wikipedia.org/wiki/Linear_search
        """
        print_msg_box(message)

    #Define the bsearch method i.e. binary search
    def binary_search(self, list, val,hint=False):

        if(hint == True):
            self.binary_search_hint()
        list_size = len(list) - 1

        low = 0 #lower index
        high = list_size

        # Find the middle most value

        while low <= high:
            mid = (low + high)// 2 #divide

            if list[mid] == val:
                return mid
            # Compare the value the middle most value
            if val > list[mid]:
                low = mid + 1
            else:
                high = mid - 1
        # Value isn't found anywhere in the list, then return none            
        if low > high:
            return None

    def binary_search_hint(self):
        message = """
        Binary Search
        ------------------------------------
        Purpose : searching a required number
        Method : Iterating, divide and conquer
        Time Complexity: 
        Worst-case performance: O(log n)
        Best-case performance: O(1)
        Average performance: O(log n)
        Worst-case space complexity: O(1)
        Hint :
        In binary search we take a sorted list of elements and start looking for an element at the middle of the list.
        If the search value matches with the middle value in the list we complete the search.
        Otherwise we eleminate half of the list of elements by choosing whether to procees with the right or left half
        of the list depending on the value of the item searched. This is possible as the list is sorted and it is
        much quicker than linear search. Here we divide the given list and conquer by choosing the proper half of the
        list. We repeat this approcah till we find the element or conclude about it's absence in the list.
        PSEUDOCODE:
            1. Compare 'x' with the middle element
            2. If x matches with the middle most element, we return the index of the middle element i.e. 'mid'.
            3. Else if x is greater than the middle element, x will lie in the right sub-part of the list from the middle element.Thus, we recur the right part of the list.
            4. Else, the x is smaller than the middle element, so we recur the left sub-part of the list.
        MORE INFO HERE: https://en.wikipedia.org/wiki/Binary_search_algorithm
        """
        print_msg_box(message)

class greedy_algorithms:

    def min_product_subset(self,array, hint=False):
    
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
            self.min_product_subset_hint()
        return prod


    def min_product_subset_hint(self):
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

class recursion:
    def step_problem(self,n,hint=False):
        if(n <0):
            return 0
        if(n==0):
            return 1
        return self.step_problem(n-1) + self.step_problem(n-2) + self.step_problem(n-3)

class dynamic_programming:
    def step_problem(self,n,hint=False):
        arr = [0]*(n+1)
        arr[0] = 1
        arr[1] = 1
        arr[2] = 2
        arr[3] = 4
        for i in range(4,n+1):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
        return arr[n]


# don't forget to add a dot for the init import before publishing the package to the PYPI

# ping1 = recursion()
# ping2 = dynamic_programming()

# print(ping2.step_problem(100))
# print(ping1.step_problem(100))

# img_arr = [[1,0,3],[2,3,4],[5,6,7]]

# ping = matrices()

# ping.setZeros(img_arr,3,3)
# print(img_arr)

# ping1 = sorting()
# arr = [7,53,35,2356,2,3,5,2]

# arr = ping1.bubble_sort(arr,'output.txt',True,True)