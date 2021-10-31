'''
Python implementation to find subsequences of a string 

For manual testing :
python subsequences_string.py

'''

'''
Python implementation to find subsequences of a string 

For manual testing :
python subsequences_string.py

'''

def subsequences_string_main (word, output) :
    
    '''
        The function prints all the subsequences of a string obtained by deleting zero or more characters of the string without changing the original order.
        For example :
            Suppose the string be 'this'. 
            Then the substrings will be this thi ths th tis ti ts t his hi hs h is i s  
    '''

    if len(word) == 0:
        print(output, end=' ')
        return
    
    subsequences_string_main(word[1:], output+word[0])
    subsequences_string_main(word[1:], output)
  
def subsequences_string (word) :
  subsequences_string_main(word, "")

if __name__ == '__main__' :
  
    subsequences_string('abcd') # prints abcd abc abd ab acd ac ad a bcd bc bd b cd c d
