from __init__ import print_msg_box
import time 

def maxSubArraySum(a,size): 
	
	max_so_far =a[0] 
	curr_max = a[0] 
	
	for i in range(1,size): 
		curr_max = max(a[i], curr_max + a[i]) 
		max_so_far = max(max_so_far,curr_max) 
		
	return max_so_far 

def kadanes_algorithm(arr,hint=False):
    start = time.time()
    if hint:
        kadanes_algorithm_hint()

    ans = maxSubArraySum(arr,len(arr))
    end = time.time()
    print("Time Taken: ",end-start)
    return ans

def kadanes_algorithm_hint():
    message="""
                                Kadane’s Algorithm
    ------------------------------------------------------------------------------------------
    Purpose : In this problem, we are given an array. Our task is to find out the maximum subarray sum.
    Method : Dynamic Programming

    Time Complexity : O(n)
    Space Complexity : O(1)

    Hint :
    Apply Dynamic Programming on contiguous array to find max contiguous sum.

    Pseudocode: 
        Initialize:
            max_so_far = a[0]
            curr_max = a[0]

        Loop(i=1,size)
        (a) curr_max = max(a[i],curr_max + a[i])
        (b) max_so_far = max(max_so_far,curr_max)

        return max_so_far

    Visualization:
        Input: [-2,1,2,-1]
        max_so_far = -2
        curr_max = -2
        
        for i=1,  a[0] =  -2
        curr_max = max(1,-2+1) = 1
        max_so_far = max(-2,1) = 1 

        for i=2,  
        curr_max = max(2,1+2) = 3
        max_so_far = max(1,3) = 3

        for i=3,  
        curr_max = max(-1,3-1) = 2
        max_so_far = max(3,2) = 3 

        FINAL RESULT = max_so_far = 3

    Learn More:
    - Maximum Subarray Problem - https://en.wikipedia.org/wiki/Maximum_subarray_problem
       
    """
    print_msg_box(message)

# print(kadanes_algorithm([-2,1,2,-1],True))
