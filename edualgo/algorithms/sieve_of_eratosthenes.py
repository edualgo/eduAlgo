class SieveOfEratosthenes:
    def hint_sieve(self):
        message = """
            Builds Sieve for prime no. less than n
            ------------------------------------
            Purpose : Building Sieve of Eratosthenes
            Method : Simple loops and Sieve building algo

            Time Complexity :   O(nlog(logn))

            Working Hint:
            Initialize the Sieve and Update the values of factor of the initial primes. For example,
            initial the sieve with true values only and starting with 2 if the value at that index is true
            then set the value of its factor index(4,6,8,10,...) to false and repeat the process.

            Pseudocode :
            --> Intialize the sieve(list) with all true values
            --> Set 0 and 1 index as False
            --> while k*k <= n:
            -->     if value at kth index of sieve is true:
            -->         set value at factor index of k as false

            Example:
            --> obj = SieveOfEratosthenes()
            --> obj.build_sieve(10)
            --> obj.get_prime   # get list of prime less than n
            --> obj.get_sieve   # get sieve that was built
        """
        print(message)
    
    def build_sieve(self, n):
        """
        Builds the sieve.

        Args:
            n ([int]): prime numbers less than n 
        """
        self.__sieve = [True for _ in range(n+1)]
        self.__sieve[0:2] = (False, False)

        k = 2
        while k*k <= n:
            if self.__sieve[k]:
                for i in range(k*k, n + 1, k):
                    self.__sieve[i] = False
            
            k += 1

    @property
    def get_prime(self):
        """
        Builds list of prime no. less than n using sieve

        Returns:
            [list]: List of prime no. less than n
        """
        prime = [k for k,i in enumerate(self.__sieve) if i]
        return prime

    @property
    def get_sieve(self):
        """
        Return  the sieve built in build_sieve

        Returns:
            [list]: Sieve
        """
        return self.__sieve