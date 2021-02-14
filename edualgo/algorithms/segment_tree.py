class SegmentTree:
    def build_tree_hint(self):
        message = """
            Build Segment Tree
            ------------------------------------
            Purpose : Building a Segment tree for the given array and query
            Method : Recursion

            Time Complexity : Worst Case - O(n)

            Working Hint:
            Initialize relevant leaf nodes with array elements, and assign result of the query to the parent node.

            Pseudocode :
            --> if array_start_index == array_end_index:
            -->     Assign the corresponding leaf node the value of array element at array_start_index 
            -->     return leaf node value
            --> Find middle element of the array range [array_start_index, array_end_index]
            --> Perform query on leaf nodes values and assign result to parent node
            --> Return Parent Node Value

            Example:
            --> obj = SegmentTree([1,2,3,4,5,6,7], 2, 5)  # (2,5) is the range of query to be performed on.
            --> obj.build_tree(0,6)  # 0 and 6 are starting and ending index of array
        """
        print(message)

    def get_result_hint(self):
        message = """
            Get Result of Range Query from Segment Tree
            ------------------------------------
            Purpose : Building a Segment tree for the given array and query
            Method : Recursion

            Time Complexity : Worst Case - O(logn)

            Working Hint:
            Reach child nodes for the corresponding range, and return result of the query to the parent node.

            Pseudocode :
            --> if array_start_index and array_ending_index are inside query range:
            -->     return leaf node value
            --> if array_start_index or array_ending_index is outside query range:
            -->     return constant for corresponding function
            --> Find middle element of the array range [array_start_index, array_end_index]
            --> Perform query on leaf nodes values and return the result

            Example:
            --> obj = SegmentTree([1,2,3,4,5,6,7], 2, 5)  # (2,5) is the range of query to be performed on.
            --> obj.build_tree(0,6)  # 0 and 6 are starting and ending index of array
            --> obj.get_result(0,6)  # 0 and 6 are starting and ending index of array
        """
        print(message)

    def __init__(self,arr,l,r,function = 'add'):
        self.tree = [None for _ in range(3*len(arr))]
        self.arr = arr
        self.l = l
        self.r = r
        self._function = ('add', 'min', 'max', 'xor', 'product')
        self.func = function

    @property
    def get_function_list(self):
        """
        Get The list of the avaliable functions available to create the segment tree of.

        Returns:
            tuple: Tuple of functions
        """
        return self._function
    
    def build_tree(self, ss, se, idx = 0):
        """
        Build the segment tree of the corresponding function.

        Args:
            ss ([int]): Starting Index
            se ([int]): Ending Index
            idx (int, optional): Index of segment tree node. Defaults to 0.
        """
        if ss==se:
            self.tree[idx] = self.arr[ss]
            return self.tree[idx]
        
        mid = (ss + se) // 2

        if self.func == 'add':
            self.tree[idx] = self.build_tree(ss, mid, 2*idx+1) + self.build_tree(mid+1, se, 2*idx+2)
        elif self.func == 'min':
            self.tree[idx] = min(self.build_tree(ss, mid, 2*idx+1), self.build_tree(mid+1, se, 2*idx+2))
        elif self.func == 'max':
            self.tree[idx] = max(self.build_tree(ss, mid, 2*idx+1), self.build_tree(mid+1, se, 2*idx+2))
        elif self.func == 'xor':
            self.tree[idx] = self.build_tree(ss, mid, 2*idx+1) ^ self.build_tree(mid+1, se, 2*idx+2)
        elif self.func == 'product':
            self.tree[idx] = self.build_tree(ss, mid, 2*idx+1) * self.build_tree(mid+1, se, 2*idx+2)
        return self.tree[idx]

    def get_result(self, ss, se, idx = 0):
        """[
        Args:
            ss ([int]): Starting Index
            se ([int]): Ending Index
            idx (int, optional): Index of segment tree node. Defaults to 0.

        Returns:
            int/float: Result for the given range
        """
        if ss >= self.l and  se <= self.r:
            return self.tree[idx]
        
        if se < self.l or ss > self.r:
            if self.func == 'add':
                return 0
            elif self.func == 'min':
                return 10**9
            elif self.func == 'max':
                return -10**9
            elif self.func == 'xor':
                return 0
            elif self.func == 'product':
                return 1
        
        mid = (ss + se) // 2
        if self.func == 'add':
            return self.get_result(ss,mid,2*idx+1) + self.get_result(mid+1,se,2*idx+2)
        elif self.func == 'min':
            return min(self.get_result(ss,mid,2*idx+1), self.get_result(mid+1,se,2*idx+2))
        elif self.func == 'max':
            return max(self.get_result(ss,mid,2*idx+1), self.get_result(mid+1,se,2*idx+2))
        elif self.func == 'xor':
            return self.get_result(ss,mid,2*idx+1) ^ self.get_result(mid+1,se,2*idx+2)
        elif self.func == 'product':
            return self.get_result(ss,mid,2*idx+1) * self.get_result(mid+1,se,2*idx+2)
