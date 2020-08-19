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
    def print_tree(self,root):
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



# root1 = Node(12)
# root1.insert(6)
# root1.insert(14)
# root1.insert(3)
# root1.insert(7)
# root1.insert(15)
# root1.insert(9)
# root1.insert(12)
# root1.insert(2)
# root1.insert(17)
#
# root2 = Node(11)
# root2.insert(5)
# root2.insert(24)
# root2.insert(2)
# root2.insert(8)
# root2.insert(12)
# root2.insert(19)
# root2.insert(1)
# root2.insert(20)
# root2.insert(7)
#
# ping = BinaryTreeAlgorithms()
# # ping.print_tree(root1)
# # print("Second Tree")
# # ping.print_tree(root2)
#
# root3 = ping.mergeTrees(root1,root2)
# ping.print_tree(root3)
