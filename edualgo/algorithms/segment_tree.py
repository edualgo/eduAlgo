class SegmentTree:
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
        Get The list of the avaliable functions
        available to create the segment tree of.

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
        """[summary]

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

