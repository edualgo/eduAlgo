def fibonacci_numbers(SEQ_LEN, N1=0, N2=1, _=0):
    """
    SEQ_LEN :   NUMBER OF ELEMENT IN YOUR FIBONACCI SEQUENCE
    N1, N2  :   THE FIRST TWO NUMBER OF THE SEQUENCE (0,1 DEFAULT)
    _       :   PLACEHOLDER FOR COUNTER INSIDE THE FUNCTION
    """
    while _ <= SEQ_LEN:
        print(N1)           # PRINT THE ACTUAL NUMBER OF THE SEQUENCE
        NN = N1 + N2        # FIND NEXT NUMBER OF THE SEQUENCE
        N1, N2 = N2, NN     # UPDATE N1, N2 >> EXAMPLE: [N1: 1, N2: 2, NN: 3] >> [N1: 2, N2: 3, NN: 5]
        _ += 1
