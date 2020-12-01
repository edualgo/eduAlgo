from .__init__ import print_msg_box

class Queue(object):
    """
    Queue is an abstract data type used to store
    data in  first-in-first-out (FIFO) data structure.

    We are going to use list(array) to build the queue

    Main feature of this array based queue is

    * enqueue(Addition of an element at the last index of array)
    * dequeue(Popping the element from the first index of the array)
    * Finding the length of the queue
    * Check is the queue is empty
    * get the element at the front of the queue

    Example for application using queue:
       1. Priority queue usages
       2. Any line on reservation counters
       3. etc ...

    Reference:
         https://en.wikipedia.org/wiki/Queue_(abstract_data_type)

    Usage:
    >>> from queue import Queue

    >>> sample_queue = Queue(5)

    >>> for value in [7,17,367,27,777]:
    ...     sample_queue.enqueue(value)

    >>> sample_queue.print_queue()
    | 7 |
    | 17 |
    | 367 |
    | 27 |
    | 777 |

    >>> sample_queue.dequeue()
    7

    >>> sample_queue.print_queue()
    | 17 |
    | 367 |
    | 27 |
    | 777 |

    >>> sample_queue.front()
    17

    >>> len(sample_queue)
    4

    >>> sample_queue.enqueue(77)

    >>> sample_queue.print_queue()
    | 17 |
    | 367 |
    | 27 |
    | 777 |
    | 77 |
    >>> sample_queue.enqueue(77777)
    Traceback (most recent call last):
    ...
    Exception: Queue size limit reached maximum

    >>> len(sample_queue)
    5
    """
    def __init__(self, size = 0):
        """ Initilise the queue with size 0 and empty data """
        self.data = []
        self.size = size

    def __len__(self):
        """Returns the length of the queue"""
        return len(self.data)

    def is_empty(self):
        """Returns boolean True if queue is empty and False if we have some data present"""
        return len(self.data) == 0

    def enqueue(self, value):
        """Enqueue (append) the value to queue """
        if len(self.data) == self.size:
            """Current queue list:"""
            self.print_queue()
            raise Exception("Queue size limit reached maximum")

        self.data.append(value)

    def dequeue(self):
        """ The front element is popped from the Queue and value of the element is returned"""
        if self.is_empty():
            raise Exception("Queue is empty !!! Please add data to the Queue :) ")
        else:
            return self.data.pop(0)

    def front(self):
        """Return the first element present in the queue """
        if self.is_empty():
            raise Exception("Queue is empty !!! Please add data to the Queue :) ")
        else:
            return self.data[0]

    def print_hint(self):
        """Print the details related to Queue and its implementation"""
        print(self.__doc__)

    def print_queue(self):
        """ Print the current queue"""
        for value in self.data:
            element = f'| {value} |'
            print(element)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
