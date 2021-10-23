'''
Python implementation to rotate a string 

For manual testing :
python rotate_string.py

'''

def rotate_string (sentence, rotation_point) :

    '''
        The function rotates the given string clockwise by a certain number of times.
        For example :
            Suppose the string be 'what's up'. 
            Let the number of rotations be 3.
            The final string will be rotated by 3 times clockwise.
            Hence the output becomes ' upwhat's'
            
    '''

    new_string = ""
    if (rotation_point%len(sentence) == 0) :
        return sentence
    new_string = sentence[len(sentence) - (rotation_point%len(sentence)):] + sentence [:-(rotation_point%len(sentence))]
    return (new_string)

if __name__ == '__main__' :

    print(rotate_string('paranjoy', 10)) # prints oyparanj
    print(rotate_string('abcdef', 3)) # prints defabc
    print(rotate_string('sometimes', 9)) # prints sometimes

