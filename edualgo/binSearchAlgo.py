from .__init__ import print_msg_box

class BinarySearyAlgorithm:

    #Define the bsearch method i.e. binary search
    def bsearch(self, list, val):

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

    def print_bsearch_hint(self):
        message = """
        FIND AN ELEMENT FROM A GIVEN SORTED LIST USING BINARY SEARCH ALGORITHM AND PRINT THE ELEMENT'S POSITION
        -+-+-+-
        In binary search we take a sorted list of elements and start looking for an element at the middle of the list.
        If the search value matches with the middle value in the list we complete the search.
        Otherwise we eleminate half of the list of elements by choosing whether to procees with the right or left half
        of the list depending on the value of the item searched. This is possible as the list is sorted and it is
        much quicker than linear search. Here we divide the given list and conquer by choosing the proper half of the
        list. We repeat this approcah till we find the element or conclude about it's absence in the list.
        -+-+-+-
        PSEUDOCODE:
            1. Compare 'x' with the middle element
            2. If x matches with the middle most element, we return the index of the middle element i.e. 'mid'.
            3. Else if x is greater than the middle element, x will lie in the right sub-part of the list from the middle element.Thus, we recur the right part of the list.
            4. Else, the x is smaller than the middle element, so we recur the left sub-part of the list.
        -+-+-+-
        TIME COMPLEXITY OF BINARY SEARCH ALGORITHM:

            Worst-case performance: O(log n)
            Best-case performance: O(1)
            Average performance: O(log n)
            Worst-case space complexity: O(1)
        -+-+-+-
        MORE INFO HERE: https://en.wikipedia.org/wiki/Binary_search_algorithm
        """
        print_msg_box(message)

# Initialize the sorted list

#list = [2,7,19,34,53,72] #samplelist

# Print the search result
#obj1 = BinarySearyAlgorithm()
#print(obj1.bsearch(list,72))
#print(bsearch(list,100))
#print(obj1.print_bsearch_hint())
