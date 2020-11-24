from .__init__ import print_msg_box

def rotateImage(img_arr,n,hint=False):
    if(hint==True):
         rotateImage_hint()
    for layer in range(int(n/2)):
        first = layer
        last = n-1-layer
        for i in range(first,last):
            offset = i - first
            top = img_arr[first][i]
            img_arr[first][i] = img_arr[last - offset][first]
            img_arr[last - offset][first] = img_arr[last][last - offset]
            img_arr[last][last - offset] = img_arr[i][last]
            img_arr[i][last] = top

def rotateImage_hint():
    message = """
    Rotate The Image
    ------------------------------------

    Purpose :To rotate a N x N 2D array representing an image without
    using any external space
    Method : 2D array, time-space complexity

    Time Complexity : Worst Case - O(n^2), n = number of rows in a matrix
    Space Complexity : O(1)

    Hint :
    Try implementing rotation in layers

    Pseudocode :
    for layer in range(int(n/2)):
        first = layer
        last = n-1-layer
        for i in range(first,last):
            offset = i - first
            top = img_arr[first][i]
            img_arr[first][i] = img_arr[last - offset][first]
            img_arr[last - offset][first] = img_arr[last][last - offset]
            img_arr[last][last - offset] = img_arr[i][last]
            img_arr[i][last] = top

    Visualization:

    Given image :

    1  2  3           1  4  1
    4  8  9    --->   8  8  2
    1  8  9           9  9  3

    Find the pivot (if any) :

        1     2     3

            +---+
        4   | 8 |   9      ---> 8 is the constant position
            +---+

        1     8     9


    Rotate Layer Wise using temp variable :

            +---+
        1   | 2 |   3
            +---+
      +---+       +---+
      | 4 |   8   | 9 |   -----> rotate the highlighted layer in 90 degree
      +---+       +---+
            +---+
        1   | 8 |   9
            +---+

    Rotate Next layer :

        +---+       +---+
        | 1 |   4   | 3 |
        +---+       +---+
          8     8     2      -----> rotate the highlighted layer in 90 degree
        +---+       +---+
        | 1 |   9   | 9 |
        +---+       +---+

    Finally you have the desired rotated array.
    """
    print_msg_box(message)

def setZeros(matrix,row,column):
    row_arr = [False] * row
    col_arr = [False] * column
    for i in range(row):
        for j in range(column):
            if(matrix[i][j] == 0):
                row_arr[i] = True
                col_arr[j] = True

    for i in range(row):
        if(row_arr[i]):
            for j in range(column):
                matrix[i][j] = 0

    for i in range(column):
        if(row_arr[i]):
            for j in range(row):
                matrix[j][i] = 0
