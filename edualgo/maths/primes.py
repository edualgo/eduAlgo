from edualgo import print_msg_box
from math import sqrt
from edualgo.maths.modular_arithmetic import *
from random import randint
from collections import defaultdict

def is_prime(x, hint=False):
    
    if hint: is_prime_hint()

    if x<2: return False
    if x==2: return True
    if x%2==0: return False

    return all([x%i!=0 for i in range(3, int(sqrt(x))+1, 2)])

def is_prime_hint():
    message = """
    conditions for any number X to be prime:
        1. X >= 2
        2. 2 is the only even prime
        3. X must not be divisible by any number in [2, X)
            we can optimise this check as follows:
                i. we need to check for only odd divisors.
                ii. divisors and corresponding quotients are only possible divisors left and they are unique upto sqrt(X).
                    so we need to check for only odd divisors upto sqrt(X) i.e., from 3 to sqrt(X). 
    """
    print_msg_box(message)

class prime_factorisation:

    def __init__(self, use_sieve=True, sieve_range = int(1e6)):
        self.use_sieve = use_sieve
        self.sieve_range = sieve_range
        if use_sieve:
            spf = list(range(self.sieve_range + 1))
            for i in range(4, self.sieve_range+1,2):
                spf[i] = 2
            for i in range(3, int(sqrt(self.sieve_range))+1):
                if spf[i] == i:
                    for j in range(i*i, self.sieve_range+1, i):
                        if spf[j] == j:
                            spf[j] = i 
            self.spf = spf

    def factorise(self, x):
        if self.use_sieve and x<=self.sieve_range:
            return self.__factorise_fast(x)
        else:
            factors = defaultdict(int) 
            while x%2==0:
                factors[2] += 1
                x >>= 2

            for i in range(3, int(sqrt(x))+1, 2):
                while x%i == 0:
                     factors[i] += 1 
                     x //= i

            if x>2: factors[x] += 1

            return dict(factors) 

    def __factorise_fast(self, x):
        factors = defaultdict(int) 
        while x != 1: 
            factors[self.spf[x]] += 1
            x //= self.spf[x] 
        return dict(factors) 

    @property
    def hint(self):
        message = """

        finding prime factorisation of N

        ----simple factorisation----
            1. while N is even keep dividing N by 2 and keep adding 2 to the answer list.
            2. Now that N is odd, do the following:
                i. run loop for i from 3 to sqrt(N) with step size 2 (taking all odd numbers).
                    i. while i divides N, add i to asnwer list and divide N by i.
            3. if N is still not 1 then its a prime, add it to the answer list.

            The time complexity is O(sqrt(N).log(N))

        ----factorisation using sieve----
            simple method is very slow if we have to process multiple factorisation queries.
            the idea is to store the smallest prime divisor of every number then use this value to find the factorisation using recursive division.

            1. creating the smallest prime divisor array:

                pseudo code:
                    divisor_array = [ 0, 1, 2, 3, 4, 5, ....., N ] 
    
                    loop for i from 4 to N with step size of 2: 
                        divisor_array[i] = 2

                    loop for i from 3 to sqrt(N):
                        if divisor_array[i] is i (means i is Prime):
                            loop for j from i*i to N with step size of i:
                                if divisor_array[j] == j:
                                    divisor_array[j] = i

                the time complexity is O(N.log(log(N))) 
                needs O(N) extra space 

            2. finding the factorisation of X

                pseudo code:
                    factors = []
                    while X != 1: 
                        factors.append(divisor_array[X])
                        X = X / divisor_array[X] 

                the time complexity is O(log(N)) 

        """
        print_msg_box(message)

class sieve_of_eratosthenes:

    def __init__(self, n=int(1e6)):

        mark = [True]*(n+1) 
        mark[0] = mark[1] = False
        for i in range(2, int(sqrt(n)) +1):
            if mark[i]:
                for j in range(i*i, n+1, i):
                    mark[j] = False

        self.range = n
        self.mark = mark

    def is_prime(self, arg):
        try:
            assert arg<=self.range
        except AssertionError:
            raise ValueError(f"{arg} > {self.range}")

        return self.mark[arg]

    def filter_primes(self, array):
        try:
            assert all([x<=self.range for x in array])
        except AssertionError:
            raise ValueError(f"please make sure the numbers are <= {self.range}")

        return list(filter(lambda x: self.mark[x], array))

    @property
    def hint():
        message = """
        it is used to find primes in range 2 to N

        sieve of eratosthenes algorithm generates an array in which the value at each index i is a boolean value which tells whether i is a prime number or not.

        we take a boolean array of size N with default True except for index 0 and 1

        the idea is to mark multiples of all primes from 2 to sqrt(N) as False.

        pseudo code:
            sieve_array = [ True, True, ..... ] 
            sieve_array[0] = sieve_array[1] = False

            loop for i from 2 to sqrt(N):
                if sieve_array[i] is True (means i is Prime):
                    loop for j from i*i to N with step size of i:
                        sieve_array[j] = False

        Now, if any index i in sieve_array is true then it means i is a prime.

        the time complexity is O(N.log(log(N))) 
        needs O(N) extra space 
        """
        print_msg_box(message)

def is_prime_big(x, hint = False):

    if hint: is_prime_big_hint()

    def miller(d,n):
    
        a  = 2+randint(1,n-4)

        x=  binary_modular_exponentiation(a,d,n)
        if x in [1,n-1]: return True

        while d!=n-1:
            x=binary_modular_exponentiation(x,2,n)
            d<<=1 
            if x==1: return False
            if x==n-1: return True

        return False

    def checkprime(n, k = 4):
        if n<=1 or n==4:
            return False
        if n<=3: return True
 
        d=n-1
        while d%2==0:
            d//=2 
    
        for _ in range(k):       
            if not miller(d,n):
                return False 
        return True

    return checkprime(x)

def is_prime_big_hint():
    message = """
    to check primality of very large numbers (order 10^10)

    ------Miller Rabin test--------
        checks if a number n is prime 
        k is a input parameter which measures accuracy of the test 
        generally k = 4   

        compute d & r such that d*(2^r) = n-1  
    
    ------test logic------
        randomly choose 'a' in range(2,n-1)
        compute x = (a^d)%n 
        if x in [1, n-1]:
            return true 
        else:
            keep squaring (with mod n) x while d!=n-1
                d*=2
                if (x^2)%n == 1: return False 
                else if (x^2)%n ==n-1 :return True 

    the test logic runs k times to ensure accurate results. 

    overall time complexity is O(k.(Log(n))^3)
    """
    print_msg_box(message)
