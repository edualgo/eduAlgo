from .__init__ import print_msg_box

class Heap:
    """
    A heap is a specialized tree-based data structure which is essentially 
        an almost complete tree that satisfies the heap property: the key of P 
        is less than or equal to the key of C.[2] The node at the "top" of the 
        heap (with no parents) is called the root node. 

    Main feature of this list based Heap is
    * is_empty: Check if the heap is empty
    * add: Addition of an element in the heap
    * pop: Popping the root element of the heap
    * update: Update an element with a new value in the heap
    * root: get the root element of the heap
    * print: print the heap elements.

    Usage:
    >>> from heap import Heap

    >>> sample_heap = Heap([2,6,4,8,5,9,2,10])ter
    >>> sample_heap.isEmpty()
    False
    >>> sample_heap.root()
    2
    >>> sample_heap.add(15)
    >>> sample_heap.add(7)
    >>> sample_heap.root()
    2
    >>> sample_heap.pop()
    2
    >>> sample_heap.add(19)
    >>> sample_heap.update(2, 1)
    >>> sample_heap.root()
    1
    >>> sample_heap.print()
    1, 5, 4, 8, 6, 9, 7, 10, 15, 19
    >>> sample_heap.update(8, 11)
    >>> sample_heap.add(20)
    >>> sample_heap.pop()
    1
    >>> sample_heap.update(3, 2)
    Traceback (most recent call last):
    ...
    Exception: The Element 3 is not present in the heap
    >>> sample_heap.pop()
    4
    >>> sample_heap.add(1)
    >>> sample_heap.pop()
    1
    >>> for i in range(sample_heap.__len__()):
    ...     sample_heap.pop()
    5
    6
    7
    9
    10
    11
    15
    19
    20
    >>> sample_heap.isEmpty()
    True
    >>> sample_heap.root()
    Traceback (most recent call last):
    ...
    Exception: Heap is empty !!! Please add elements to the heap
    >>> sample_heap.pop()
    Traceback (most recent call last):
    ...
    Exception: Heap is empty !!! Please add elements to the heap
    """
    
    def __init__(self, items=[]):
        """Initilise the heap with elements in list items"""
        self.heap = [None]
        self.rank = {}

        for x in items:
            self.add(x)

    def __len__(self):
        """Returns the length of the heap"""
        return len(self.heap)-1

    def isEmpty(self):
        """Returns True if heap is empty and False otherwise"""
        return len(self.heap) == 1

    def add(self, x):
        """Add element in the heap"""
        i = len(self.heap)
        self.heap.append(x)
        self.rank[x] = i
        self.up(i)

    def pop(self):
        """Remove the root element of the heap and return its value"""
        if self.isEmpty():
            raise Exception("Heap is empty !!! Please add elements to the heap")

        root = self.heap[1]
        del self.rank[root]
        x = self.heap.pop()

        if self:
            self.heap[1] = x
            self.rank[x] = 1
            self.down(1)
        return root   

    def up(self, i):
        """Move the element at index i up to its correct position"""
        x = self.heap[i]
        while i>1 and x<self.heap[i//2]:
            self.heap[i] = self.heap[i//2]
            self.rank[self.heap[i//2]] = i
            i //= 2

        self.heap[i] = x
        self.rank[x] = i


    def down(self, i):
        """Move the element at index i down to its correct position"""
        x = self.heap[i]
        n = len(self.heap)
        while True:
            left = 2*i
            right = left+1
            if right<n and self.heap[right]<x and self.heap[right] < self.heap[left]:
                self.heap[i] = self.heap[right]
                self.rank[self.heap[right]] = i
                i = right
            elif left<n and self.heap[left]<x:
                self.heap[i] = self.heap[left]
                self.rank[self.heap[left]] = i
                i = left
            else:
                self.heap[i] = x
                self.rank[x] = i
                break
                
    def update(self, old, new):
        """Update the element old with a new element"""
        if self.rank.get(old, -1) == -1:
            raise Exception(f"The Element {old} is not present in the heap")

        i = self.rank[old]
        del self.rank[old]

        self.heap[i] = new
        self.rank[new] = i
        
        if old<new:
            self.down(i)
        else:
            self.up(i)

    def root(self):
        """Returns the root element present in the heap"""
        if self.isEmpty():
            raise Exception("Heap is empty !!! Please add elements to the heap")
        else:
            return self.heap[1]

    def print_hint(self):        
        message = """
        Printing A Heap
        ------------------------------------
        Purpose : Printing a Heap(Both Left and Right Node)
        Method : Recursion, Binary Tree
        Time Complexity : Worst Case - O(n), n = Number of nodes in a Binary Tree
        Hint :
        Print the root, use recursion and call into the left and right
        Pseudocode :
        --> if(root == None) return
        --> print(root.value)
        --> print(root.left.value)
        --> print(root.right.value)
        --> make recursion calls,
            print_tree(root.left)
            print.tree(root.right)

        Visualization:

        Given Heap : [3, 6, 4, 10, 7, 12, 15]

                            +-----+
                            |  3  |   <-- root
                            +-----+
                           /      \\
                          /        \\
                   +-----+          +-----+
    root.left -->  |  6  |          |  4  |   <-- root.right
                   +-----+          +-----+
                  /      \\          /     \\
                 /        \\        /       \\
           +----+       +-----+  +----+      +----+
           | 10 |       |  7  |  | 12 |      | 15 |
           +----+       +-----+  +----+      +----+
        
        Step 1: print root, root.left and root.right
        Step 2 : call recursive functions

        Finally The Output :
         -------------------------
        |    3: L: 6, R: 4,      |
        |                        |
        |    6: L: 10, R: 7,     |
        |                        |
        |    4: L: 12 ,R: 15,    |
         -------------------------
        
        Learn More:
        - Heap - https://en.wikipedia.org/wiki/Heap_(data_structure)
        """
        print_msg_box(message)

    def print(self):
        """Print the current heap"""
        print(*self.heap[1:], sep=', ')        

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    