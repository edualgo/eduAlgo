from edualgo import print_msg_box
from math import gcd

def binary_exponentiation(x, y, hint = False):

    # iterative version
    
    if hint:
        print_binary_exponentiaition_hint()

    result = 1 
    while y>0:

        if y%2 == 1:
            result *= x    

        y //= 2
        x *= x
    
    return result

def binary_modular_exponentiation(x, y, mod, hint=False):

    # iterative version

    if hint:
        print_binary_exponentiaition_hint()

    result = 1
    while y > 0:

        if y%2 == 1:
            result = (result*x) % mod

        y //= 2 
        x = (x*x) % mod
    
    return result

def modular_inverse(x, y, hint=False):

    if hint:
        modular_inverse_hint()

    try:
        assert gcd(x,y)==1
    except AssertionError:
        raise ValueError(f"{x} and {y} are not co-prime")

    return binary_modular_exponentiation(x, y-2, y)


def print_binary_exponentiaition_hint():
    message = """
    The expression X^Y can be evaluated in log(Y) steps.

    let ANS = X^Y

    if Y is even, we can write :
        ANS = (X^2)^(Y ÷ 2)

        that is, we square the base and halve the exponent.

    else if Y is odd :
        ANS = ANS*X

        that is, we multiply our ANS once with base so that Y reduces by 1 and becomes even.

    These two steps are executed repeatedly till exponent (Y) is greater than 0.

    We can extend this algorithm for modular exponentiation by simply appending a mod operation to the multiplications.

    The time complexity for this algorithm is O(Log(Y)). 
    """
    print_msg_box(message)

def modular_inverse_hint():
    message = """
    the modular inverse for A under mod M is defined as X such that 
        (A*X)%M=1

    According to Fermats’s little theorem, 
        X = (A^(M-2))%M , when A and M are co-prime
    """
    print_msg_box(message)