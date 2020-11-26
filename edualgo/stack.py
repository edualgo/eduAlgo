from tabulate import tabulate
from .__init__ import print_msg_box


class error(Exception):
    pass

class Stack(object):
    """
    Stack is an abstract data type used to store
    data in Last In First Out method (LIFO).

    We are going to use list(array) to build the stack

    Main feature of this array based stack is

    * Insert
    * deletion of last element
    * Finding the length of the stack
    * Check is the stack is empty
    * get the element at the top of the stack

    Example for application using stack:
       1. browser fetching the previously used URL using back
          and forward button
       2. stack of plates in a restaurant
       3. Validating html file by matching the brackets
       4. etc ...

    Reference:
         https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

    Usage:
    >>> from stack import Stack

    >>> my_stack = Stack(5)

    >>> for value in [10,1,24,200,1000]:
    ...    my_stack.push(value)

    >>> my_stack.pretty_print()
    |-----:|
    | 1000 |
    |  200 |
    |   24 |
    |    1 |
    |   10 |

    >>> my_stack.pop()
    1000

    >>> my_stack.pretty_print()
    |----:|
    | 200 |
    |  24 |
    |   1 |
    |  10 |
    >>> my_stack.top()
    200

    >>> len(my_stack)
    4

    >>> my_stack.push(10)
    >>> my_stack.push(1)
    Traceback (most recent call last):
       ...
    stack.error: Stack size reached maximum

    >>> len(my_stack)
    5
    """


    def __init__(self, size = 0):
        """ Initilise the stack with size 0 and empty data """
        self.data = []
        self.size = size

    def __len__(self):
        """Returns the length of the data"""
        return len(self.data)

    def is_empty(self):
        """Returns boolean False if the data is not empty else True"""
        return len(self.data) == 0

    def push(self, value):
        """Append the value to data """
        if len(self.data) == self.size:
            """print the stack"""
            raise error("Stack size reached maximum")

        self.data.append(value)


    def pop(self):
        """ Return value from data as well as delete the value
        from data after return"""
        if self.is_empty():
            raise error("Stack is empty")
        else:
            return self.data.pop()

    def top(self):
        """Return the last pushed value from data """
        if self.is_empty():
            raise error("Stack is empty")
        else:
            return self.data[-1]

    def print_hint(self):
        """Print the documentation for class stack"""
        print(self.__doc__)

    def pretty_print(self):
        """ Print the stack """
        list_of_list = []
        for value in self.data:
            list_of_list.append([value])
        table_data = list_of_list[::-1]
        print(tabulate(table_data, tablefmt="pipe"))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
