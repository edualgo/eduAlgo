def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)

if __name__ == '__main__':
    
    arr = list(map(int,input("\nEnter the numbers: ").strip().split()))
    n = len(arr) #length of the array
    print(arr)
    #intial count of no.of zeroes  positive numbers and negative numbers
    int_neg = 0 # intializing the negative numbers count to zero
    int_pos = 0 # intializing the postive numbers count to zero
    int_zero = 0 # intializing no.of zeroes in the array to zero
    max_neg = float('-inf')
    min_pos = float('inf')
    prod = 1


    for i in range(0,n):
    # counting number of zero
        if (arr[i] == 0):]
            count_zero = count_zero + 1
            continue

    #counting number of negative numbers
        if (arr[i] < 0):
            int_neg = int_neg + 1
            max_neg = max(max_neg, arr[i])


    #counting number of positive numbers
        if (arr[i] > 0):
            int_pos = int_pos + 1
            min_pos = min(min_pos,arr[i])

        prod = prod*arr[i]

    if n == 1:
        print("arr[0]") #if the array contains only one value

    if int_zero == n or int_zero > 0 :
        print(0) #if the array contains all the values as zeroes or have atleast one zero

    if int_neg == 0:
        print(min_pos) #if the array contains no negative numbers

    if (int_neg % 2 == 0) :
        prod = int(prod / max_neg) #if the array contains even number of negative numbers
    print(prod)
