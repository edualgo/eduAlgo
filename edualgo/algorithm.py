import time

# 'sort' class contains the following algorithms:
#     1 - Bubble sort
#     2 - Selection sort
#     3 - Insertion sort
#     4 - Merge sort
#     5 - Quick sort
#     6 - Counting sort
#     7 - Radix sort
#     8 - Heap sort
#     9 - Bucket sort

class sort:

    # bubble sort algorithm
    def bubble_sort(self,arr):
        start = time.time()
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1] :
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        end = time.time()
        print("Bubble Sort Runtime = {}".format(end-start))
        return arr

    # selection Sort Algorithm
    def selection_sort(self,arr):
        start = time.time()
        for i in range(len(arr)-1):
            minimum = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j
            arr[minimum],arr[i] = arr[i],arr[minimum]
        end = time.time()
        print("Selection Sort Runtime = {}".format(end-start))
        return arr
