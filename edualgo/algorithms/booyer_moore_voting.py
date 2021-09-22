'''

The following file contains the code for Moore majority voting algorithm.
It returns the majority element in an array(i.e element occuring more than n/2 times in the array). It is
also capable of returning the frequency of the majority element.
Incase of no such element, it returns -1

'''

class BoyerMooreMajority:

    def __init__(self, array=None):
        self.arr = array
        self.majority_element = None
        self.votes_count = 0

    def get_majority_element(self):
        '''
        This function returns the majority element present in the array. Incase no such element exists
        it returns -1
        '''
        try:
            if self.arr is None:
                ve = ValueError()
                ve.strerror = "Passed array cannot be None"
                raise ve
            elif type(self.arr) != list:
                ve = ValueError()
                ve.strerror = "Please pass an array of elements"
                raise ve
            elif len(self.arr) == 0:
                ve = ValueError()
                ve.strerror = "Passed array cannot be empty"
                raise ve

        except ValueError as v:
            print(f'Value Error : {v.strerror}')

        else:
            candidate = None
            votes = 0
            length = len(self.arr)
            for i in range(length):
                if votes == 0:
                    candidate = self.arr[i]
                    votes = 1
                elif self.arr[i] == candidate:
                    votes += 1
                else:
                    votes -= 1

            for i in range(length):
                if self.arr[i] == candidate:
                    self.votes_count += 1

            if self.votes_count > length // 2:
                self.majority_element = candidate
            else:
                self.majority_element = -1

            return self.majority_element

    def get_vote_count(self):
        '''
        This function returns the frequency or votes of the majority element. Incase of no majority element
        it returns -1
        '''
        try:
            if self.majority_element is None:
                raise ValueError
        except ValueError as v:
            print('Value Error : Please run get_majority_element function properly first.')

        else:
            if self.majority_element == -1:
                self.votes_count = -1

            return self.votes_count


# CALLING CODE EXAMPLE
#arr = [1,2,3,1,1,4,5,1,1,7,1]
#mva = BoyerMooreMajority(arr) # create an object
#mva.get_majority_element() # This returns 1 as output
#mva.get_vote_count() # This returns 6 as output