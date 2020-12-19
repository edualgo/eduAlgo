from edualgo import print_msg_box

class combinationsDict(dict):

    def __missing__(self, k):
        n,r = k
        if r==0 or r==n: 
            self[k] = 1 
            return 1
        K = self[n-1,r-1] + self[n-1,r]
        self[k]= K
        return K

    @property
    def hint(self):
        message = """

        ------formal definition------
        number of combinations is defined as:
        The number of selections of a given number of elements from a larger number without regard to their arrangement.

        for r elements to be selected from n elements, number of combinations is denoted by nCr 

        nCr = (n!)/((r!)*(n-r)!)

        ------recursive definition------
        C(n, r) = C(n-1, r-1) + C(n-1, r)
        base case: C(n, 0) = C(n, n) = 1

        ------usage------
        obj = combinationsDict()
        print("3C2 =",obj[3,2]) 

        """
        print_msg_box(message)
    