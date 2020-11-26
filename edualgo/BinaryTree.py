from .__init__ import print_msg_box
import collections
class Node:
    def __init__(self, val):

        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

class BinaryTreeAlgorithms:
    def print_tree(self,root,hint=False):
        if(hint==True):
            self.print_tree_hint()
        if root == None:
            return
        print(root.val,end =":")
        if root.left:
            print("L: {} ,".format(root.left.val),end ="")
        if root.right:
            print("R: {} ,".format(root.right.val),end="")
        print("\n")
        self.print_tree(root.left)
        self.print_tree(root.right)

    def print_tree_hint(self):
        message = """
        Printing A Binary Tree
        ------------------------------------

        Purpose : Printing a Binary Tree(Both Left and Right Node)
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

        Given Binary Tree :

                            +------+
                            |  12  |         <-- root
                            +------+
                            /      \\
                           /        \\
                   +------+          +------+
    root.left -->  |  6   |          |  14  |   <-- root.right
                   +------+          +------+
                   /      \\          /      \\
                  /        \\        /        \\
          +------+     +------+   +------+    +------+
          |  3   |     |  7   |   |  12  |    |  15  |
          +------+     +------+   +------+    +------+


           Step 1: print root, root.left and root.right

                12 : L:6, R: 14

           Step 2 : call recursive functions

           f(root.left) :

                           +------+
                           |  6   |    <-- root
                           +------+
                           /      \\
                          /        \\
                  +------+         +------+
   root.left -->  |  3   |         |  7   |  <-- root.right
                  +------+         +------+

          +------------------------+
          | Repeat Step 1 & Step 2 |   <-- recursion calls
          +------------------------+

          f(root.right) :

                          +------+
                          |  14  |    <-- root
                          +------+
                          /      \\
                         /        \\
                 +------+         +------+
  root.left -->  |  12  |         |  15  |  <-- root.right
                 +------+         +------+

         +------------------------+
         | Repeat Step 1 & Step 2 |      <-- recursion calls
         +------------------------+

         Finally The Output :

         -------------------------
        |    12:L: 6 ,R: 14 ,     |
        |                         |
        |    6:L: 3 ,R: 7 ,       |
        |                         |
        |    3:                   |
        |                         |
        |    7:                   |
        |                         |
        |    14:L: 12 ,R: 15 ,    |
        |                         |
        |    12:                  |
        |                         |
        |    15:                  |
         -------------------------

        Learn More:
        - Binary Trees - https://en.wikipedia.org/wiki/Binary_tree
        - Recursion - https://en.wikipedia.org/wiki/Recursion_(computer_science)
        """
        print_msg_box(message)
    
    def Inorder_print(self,root,hint=False):
        if(hint==True):
            self.Inorder_print_hint()
        if root == None:
            return
        self.Inorder_print(root.left)
        print(root.val,end =", ")
        self.Inorder_print(root.right)

    def Inorder_print_hint(self):
        message = """
        Printing A Binary Tree InOrder Traversal
        ------------------------------------

        Purpose : Printing a Binary Tree(InOrder Traversal)
        Method : Recursion, Binary Tree

        Time Complexity : Worst Case - O(n), n = Number of nodes in a Binary Tree

        Hint :
        print order ->  LEFT -- ROOT -- RIGHT
        Call into left recursively till exist,Print the root, use recursion to call into the right

        Pseudocode :
        --> if(root == None) return
        --> print(root.left.value)
        --> print(root.value)
        --> print(root.right.value)

        Visualization:

        Given Binary Tree :

                            +------+
                            |  12  |         <-- root
                            +------+
                            /      \\
                           /        \\
                   +------+          +------+
    root.left -->  |  6   |          |  14  |   <-- root.right
                   +------+          +------+
                   /      \\          /      \\
                  /        \\        /        \\
          +------+     +------+   +------+    +------+
          |  3   |     |  7   |   |  13  |    |  15  |
          +------+     +------+   +------+    +------+


        step : call recursive functions on root.left, print root, call on right

                f(root.left) :

                           +------+
                           |  3   |    <-- root
                           +------+
                           /      \\
                          /        \\
                  +------+         +------+
   root.left -->  | None |         | None |  <-- root.right
                  +------+         +------+

                output : LEFT -- ROOT -- RIGHT 
                         None     3      None
            

                           +------+
                           |  6   |    <-- root
                           +------+
                           /      \\
                          /        \\
                  +------+         +------+
   root.left -->  |  3   |         |  7   |  <-- root.right
                  +------+         +------+

                output : LEFT -- ROOT -- RIGHT 
                          3       6        7

          f(root.right) :

                          +------+
                          |  14  |    <-- root
                          +------+
                          /      \\
                         /        \\
                 +------+         +------+
  root.left -->  |  13  |         |  15  |  <-- root.right
                 +------+         +------+

               output : LEFT -- ROOT -- RIGHT 
                         13      14      15

         Finally The Output :

         ---------------------------------
        |    3, 6, 7, 12, 13, 14, 15,     |
         ---------------------------------

        Learn More:
        - Binary Trees - https://en.wikipedia.org/wiki/Binary_tree
        - Recursion - https://en.wikipedia.org/wiki/Recursion_(computer_science)
        """
        print_msg_box(message)

    def Preorder_print(self,root,hint=False):
        if(hint==True):
            self.Preorder_print_hint()
        if root == None:
            return
        print(root.val,end =", ")
        self.Preorder_print(root.left)
        self.Preorder_print(root.right)

    def Preorder_print_hint(self):
        message = """
        Printing A Binary Tree PreOrder Traversal
        ------------------------------------

        Purpose : Printing a Binary Tree(PreOrder Traversal)
        Method : Recursion, Binary Tree

        Time Complexity : Worst Case - O(n), n = Number of nodes in a Binary Tree

        Hint :
        print order ->  ROOT -- LEFT -- RIGHT
        Print the root, use recursion to call into the left and the right subtree

        Pseudocode :
        --> if(root == None) return
        --> print(root.value)
        --> print(root.left.value)
        --> print(root.right.value)

        Visualization:

        Given Binary Tree :

                                +------+
                                |  12  |   <-- root
                                +------+
                                /      \\
                               /        \\
                        +------+          +------+
         root.left -->  |  6   |          |  14  |   <-- root.right
                        +------+          +------+
                        /      \\          /      \\
                       /        \\        /        \\
                +------+     +------+   +------+    +------+
                |  3   |     |  7   |   |  13  |    |  15  |
                +------+     +------+   +------+    +------+


        step 1 : Print the root value
                    
                                +------+
                                |  6   |    <-- root
                                +------+
                                /      \\
                               /        \\
                        +------+         +------+
         root.left -->  |  3   |         |  7   |  <-- root.right
                        +------+         +------+

                output : 6

                f(root.left) :

                                +------+
                                |  3   |    <-- root
                                +------+
                                /      \\
                               /        \\
                        +------+         +------+
         root.left -->  | None |         | None |  <-- root.right
                        +------+         +------+

                output : ROOT -- LEFT -- RIGHT 
                          3      None     None

          f(root.right) :

                                +------+
                                |  14  |    <-- root
                                +------+
                                /      \\
                               /        \\
                        +------+         +------+
         root.left -->  |  13  |         |  15  |  <-- root.right
                        +------+         +------+

               output : ROOT -- LEFT -- RIGHT 
                         14      13      15

         Finally The Output :

         ---------------------------------
        |    12, 6, 3, 7, 14, 13, 15,     |
         ---------------------------------

        Learn More:
        - Binary Trees - https://en.wikipedia.org/wiki/Binary_tree
        - Recursion - https://en.wikipedia.org/wiki/Recursion_(computer_science)
        """
        print_msg_box(message)

    def Postorder_print(self,root,hint=False):
        if(hint==True):
            self.Postorder_print_hint()
        if root == None:
            return
        self.Postorder_print(root.left)
        self.Postorder_print(root.right)
        print(root.val,end =", ")

    def Postorder_print_hint(self):
        message = """
        Printing A Binary Tree PostOrder Traversal
        ------------------------------------

        Purpose : Printing a Binary Tree(PostOrder Traversal)
        Method : Recursion, Binary Tree

        Time Complexity : Worst Case - O(n), n = Number of nodes in a Binary Tree

        Hint :
        print order ->  LEFT -- RIGHT -- ROOT
        use recursion to call into the left and the right subtree, Print the root

        Pseudocode :
        --> if(root == None) return
        --> print(root.left.value)
        --> print(root.right.value)
        --> print(root.value)

        Visualization:

        Given Binary Tree :

                                +------+
                                |  12  |   <-- root
                                +------+
                                /      \\
                               /        \\
                        +------+          +------+
         root.left -->  |  6   |          |  14  |   <-- root.right
                        +------+          +------+
                        /      \\          /      \\
                       /        \\        /        \\
                +------+     +------+   +------+    +------+
                |  3   |     |  7   |   |  13  |    |  15  |
                +------+     +------+   +------+    +------+


        step 1 : Print the left, print right, print root
                    
                                +------+
                                |  6   |    <-- root
                                +------+
                                /      \\
                               /        \\
                        +------+         +------+
         root.left -->  |  3   |         |  7   |  <-- root.right
                        +------+         +------+


                output : LEFT -- RIGHT -- ROOT 
                          3        7        6


         Finally The Output :

         ---------------------------------
        |    3, 7, 6, 13, 15, 14, 12     |
         ---------------------------------

        Learn More:
        - Binary Trees - https://en.wikipedia.org/wiki/Binary_tree
        - Recursion - https://en.wikipedia.org/wiki/Recursion_(computer_science)
        """
        print_msg_box(message)

    def rangeSumBST(self, root,L,R):
        if(root == None):
            return 0
        sum1 = 0; sum2 = 0
        if(root.left):
            sum1 = self.rangeSumBST(root.left,L,R)
        if(root.right):
            sum2 = self.rangeSumBST(root.right,L,R)
        if((root.val >= L )and (root.val <= R)):
            return root.val + sum1 + sum2
        else:
            return sum1 + sum2

    def mergeTrees(self, t1, t2):
        if(t1 == None and t2 == None):
            return None
        if(t2 == None):
            return t1
        if(t1 == None):
            return t2
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1

    def sumOfLeftLeaves(self, root):
        if(root == None):
            return 0
        sum = 0
        if(root.left != None and (root.left.left == None and root.left.right == None)):
            sum = root.left.val
        return sum + self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)

    def isSameTree(self, p, q):
        if(p == None and q == None):
            return True
        if(p == None or q == None):
            return False
        return (p.val == q.val) and (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))

    def isCousins(self, root, x, y):
        if not root:
            return root
        queue = collections.deque([root])
        level = set()
        last = n_last = root
        while any(queue):
            node = queue.popleft()
            same_father = set()
            if node.left:
                level.add(node.left.val)
                queue.append(node.left)
                n_last = node.left
                same_father.add(node.left.val)
            if node.right:
                level.add(node.right.val)
                queue.append(node.right)
                n_last = node.right
                same_father.add(node.right.val)
            if x in same_father and y in same_father:
                return False
            if node == last:
                last = n_last
                if x in level and y in level:
                    return True
                level = set()
        return False

    def countNode(self,root):
        '''
        countNode will take root node 
        as input and return the number 
        node present in the tree.
        '''
        if (root == None):
            return 0
        return 1 + self.countNode(root.left) + self.countNode(root.right)

    def KthLevel(self,root, k):
        '''
        KthLevel will take root node and level value (k),
        and print the element present at that level 
        Note: level for the root node is 1
        '''
        if (root == None):
            return
        if (k ==1):
            print(root.data,end=', ')
            return
        self.KthLevel(root.left, k-1)
        self.KthLevel(root.right, k-1)
        return


#root1 = Node(12)
#root1.insert(6)
#root1.insert(14)
#root1.insert(3)
#root1.insert(7)
#root1.insert(15)
#root1.insert(13)
# ping = BinaryTreeAlgorithms()
# ping.Inorder_print(root1)
# ping.Preorder_print(root1)
# ping.Postorder_print(root1)


