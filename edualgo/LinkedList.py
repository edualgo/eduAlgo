from .__init__ import print_msg_box

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,val):
        if self.tail is None:
            self.head = Node(val)
            self.tail = self.head

        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.val, end =" ")
            temp = temp.next

class list_algorithms:

    def length(self,head):
        temp = head
        count = 0
        while(temp):
            temp = temp.next
            count += 1
        return count

    def reverse_linked_recursive(self,head):
        if(head == None or head.next == None):
            return head
        small_head = self.reverse_linked_recursive(head.next)
        head.next = None
        temp = small_head
        while(temp.next != None):
            temp = temp.next
        temp.next = head
        head = small_head
        return head

    def reverse_linked_iterative(self,head):
        if(head == None or head.next == None):
            return head
        prev = None
        curr = head
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def is_palindrome(self,head):
        stack = []
        temp = head
        while(temp):
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while(temp):
            if(stack[-1] != temp.val):
                return False
            else:
                stack.pop()
                temp = temp.next
        return True

    def is_palindrome_optimized(self,head):
        len = self.length(head)
        if(len <= 1):
            return True
        count = 0
        head2 = head
        prev = None
        while(count < int(len/2)):
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
            count+=1
        head = head2
        head2 = prev
        if(len % 2 == 1):
            head = head.next
        while((head2 != None) and (head != None)):
            if(head2.val != head.val):
                return False
            head = head.next
            head2 = head2.next
        return True

    def delete_sorted_duplicate(self,head):
        if(head == None or head.next == None):
            return head
        small_head = self.delete_sorted_duplicate(head.next)
        while((small_head != None) and (head.val == small_head.val)):
            temp = small_head
            small_head = small_head.next
            temp.next = None

        head.next = small_head
        return head

    def delete_node(self,node):
        node.val = node.next.val
        node.next = node.next.next

    def middleNode(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeTwoLists(self, l1, l2):
        if(l1==None):
            return l2
        if((l2 != None) and (l2.val < l1.val)):
            l1,l2 = l2,l1
        l1.next = self.mergeTwoLists(l1.next,l2)
        return l1

    def removeElements(self,head,val):
        if(head == None):
            return head
        small_head = self.removeElements(head.next,val)
        if(head.val == val):
            head = small_head
        else:
            head.next = small_head
        return head

    def getIntersectionNode(self,headA,headB):
        tempA = headA
        tempB = headB

        lengthA = 0
        lengthB = 0

        while(tempA):
            lengthA += 1
            tempA = tempA.next
        while(tempB):
            lengthB += 1
            tempB = tempB.next

        tempA = headA
        tempB = headB

        while(lengthA > lengthB):
            tempA = tempA.next
            lengthA -= 1
        while(lengthB > lengthA):
            tempB = tempB.next
            lengthB -= 1

        while((tempA != tempB) and (tempA != None)):
            tempA = tempA.next
            tempB = tempB.next

        if((tempA == tempB) and (tempA != None)):
            return tempA
        else:
            return None

    def getDecimalValue(self,head):
        temp = head
        length = 0
        while(temp):
            length += 1
            temp = temp.next

        num = 0
        temp = head

        while(temp):
            num += temp.val * (2**(length-1))
            length -= 1
            temp = temp.next

        return num

    def nextLargerNodes(self,head):
        result = []
        temp = head
        while(temp):
            result.append(temp.val)
            temp = temp.next

        stack = []
        n = len(result)
        i = n-1
        while(i >= 0):
            next = 0
            while(len(stack)!=0 and stack[-1] <= result[i]):
                stack.pop()
            if(len(stack)!=0 and stack[-1] > result[i]):
                next = stack[-1]
            stack.append(result[i])
            result[i] = next
            i-=1
        return result
    def removeNthNodeFromEnd(self,head,n):
        first = head 
        second = head 
        for i in range(n): 
            if(second.next == None): 
                if(i == n - 1): 
                    self.head = self.head.next
                return self.head 
            second = second.next
        while(second.next != None): 
            second = second.next
            first = first.next
          
        first.next = first.next.next

    def removeNthNodeFromEnd_hint(self):
        message=""" 
        Remove Nth Node from end of a linked list
        ------------------------------------
         Purpose : to remove the Nth node from end of the linked list
         Approach: We use a two pointer approach. The first and second pointer both start by refering to head.
         We then move the second pointer by N steps without moving the first pointer. 
         Now both the pointers have a distance of N nodes between them.
         Now, we move both the pointer by a step each until the second pointer reaches the end of linked list.
         Since both the pointers will still be at a distacne of N nodes , when the second pointer reaches the end of linked list , 
         the first pointer will be at a distance of N nodes from the end i.e at the Nth node from the end.
         So we delete the node pointed by the first pointer.

         Edge Case: There are 2 possible edge cases in the above mentioned approach
         ---------------------------------------------------
         While moving the second pointer by N nodes , we keep checking if the "next" of the second pointer is null
         If it is null then 2 cases may arise:
         1) The length of linked list is exactly N and in that case the value of the loop variable i would be N-1 
         and the Nth node from end would be the head. So in that case we update the head by setting the head to head.next
         2) The length of list is < n :
         In this case, since we can't delete the Nth node from the end, we simply return head .
         


         Time Complexity:
         --------------------
         O(L): where L is the length of the Linked List
        """
        print(message)
        
        
            


# ping = linkedlist()
# ping.append(1)
# ping.append(2)
# ping.printLL()
