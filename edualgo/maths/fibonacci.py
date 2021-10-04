from __init__ import print_msg_box

class fib_class:

    def __init__(self, num, hint=False):
        if hint is True: 
            self.fib_hint()
        print([self.fib_cal(i) for i in range(num)])

    def fib_cal(self, num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return self.fib_cal(num-1) + self.fib_cal(num-2)

    def fib_hint(self):
        message='''
        Conditions to calculate the Fibonacci series:
        1. If num == 0 then Fibonacci should return 0
        2. If num == 1 then Fibonacci should return 1
        3. If num > 0 then add the previous number with current number        
        
        Time Complexity  : O(2^n)
        Space Complexity : O(1) 
        Where n is number of number of Fibonacci series
        '''
        print_msg_box(message)

def fibonacci(num, hint=False):
    obj_fib_class = fib_class(num, hint)
