from __init__ import print_msg_box
class Node:

    def __init__(self, dataValue=None):
        self.dataValue = dataValue
        self.next = None

class singleLinkedList:

    def __init__(self):
        self.headValue = None
        self.temp = None

    def insertLast(self, *elements):

        for data in elements:

            if self.headValue == None:
                self.headValue = Node(data)
                self.temp  = self.headValue
            else:
                self.temp.next = Node(data)
                self.temp = self.temp.next
        self.temp.next = self.headValue
        pass

    def insertFirst(self, *elements):

        if self.headValue != None:
            prevheadValue = self.headValue
            self.headValue = None
        else:
            prevheadValue = None

        for data in elements:

            if self.headValue == None:
                self.headValue = Node(data)
                self.temp  = self.headValue
            else:
                self.temp.next = Node(data)
                self.temp = self.temp.next

        if prevheadValue != None:
            self.temp.next = prevheadValue
            self.temp = self.temp.next
        while self.temp.next != prevheadValue:
            self.temp = self.temp.next
        self.temp.next = self.headValue


    def insertMiddle(self, arg1: "data", arg2: "position"):
        node = self.headValue
        for i in range(1,arg2-1):
            if node.next is None:
                return
            node = node.next
            prev = node.next
        node.next = Node(arg1)
        node = node.next
        node.next = prev
        while node.next != self.headValue:
            node = node.next
        node.next = self.headValue       
            
    def delete(self, position: "Position to be deleted"):
        #[data|next] --> [data|next] --> [data|next] --> [data|next]
        #                        ^_______________^
        node = self.headValue
        for i in range(position-2):
            node = node.next 
        node.next = node.next.next
        while node.next != self.headValue:
            node = node.next
        node.next = self.headValue

    def display(self):

        printValue = self.headValue
        
        if printValue is None:
            print("list is empty")

        while printValue is not None:
            print (printValue.dataValue)
            printValue = printValue.next
        pass
    def hint(self):
        message=""""
        Create a node class to have two variables
        1. Store data (datavalue)
        2. Next data address in last it is usually null in circular (next)
        linked list 
        Create another class to perform manipulation in list
        
        Insert First:
        *To insert first element we need to have the data to whether any
        data exist before if so then we have to store it safely
        * Storing the data in headval
        * Taking previous value to set next value of another node
        * It repeats until it reaches the previous head value
        * Setting the last value to head node

        Insert last:
        *To insert last element we need to have the data to whether any
        data exist before if so then we have to store it safely
        * It repeats until it reaches the head value is occurred
        * Setting the last node next value to head node
        
        Insert Middle:
        *To insert middle element we need to have the data to whether any
        data exist before if so then we have to store it safely
        * Taking previous value to set next value of another node
        * It repeats until it reaches the previous head value
        * Setting the last next value to head node
        
        Display:
            Display will take next value of node repeatedly so the list is 
            infinite loop        

        """
#creating object 
#list = singleLinkedList()

#list.insertLast(50, 60,70)
#list.display()

'''
It shows the entered things at last

output:
=======

50
60
70
50...
'''

#list.insertFirst(10,20,30)
#list.display()

'''
It shows the entered things at first then remaining 

output:
=======

10
20
30
50
60
70
10...
'''

#print(list.insertMiddle.__annotations__)
#list.insertMiddle(40,4)
#list.display()
'''
It shows the inserted element at nth position 

output:
=======

10
20
30
40
50
60
70
10...
'''

#list.delete(6)
#list.display()
'''
It shows the list after deleting it 

output:
=======

10
20
30
40
50
60
10...
'''
