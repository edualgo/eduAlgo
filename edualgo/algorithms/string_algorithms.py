import time

from .__init__ import print_msg_box


def isUnique(input_string,hint=False):
    mapp = []
    for i in input_string:
        if i not in mapp:
            mapp.append(i)
    if(hint is True):
         isUnique_hint()
    return len(mapp) == len(input_string)

def isUnique_hint():
    message ="""
    Unique Character Checking
    ------------------------------------

    Purpose : checking if all the characters in a given string are unique
    Method : list comprehension

    Time Complexity: Worst Case - O(n), n = length of the input string

    Hint :
    How about using the inbuilt list data structure ?

    Pseudocode:
    --> create an empty list named mapp
    --> for i in input string
            if i not in mapp
                add i to the empty list
    --> The string is unique only when the
        length of the map after the total
        iterations is same as that of the
        length of the input string

    Visualization:

    Given String :

    "aabcc"

    Empty List:

     ----------------
    |                |
     ----------------

    after first iteration :

     ----------------
    |       a        |
     ----------------

    after second iteration :

     ----------------
    |       a        |
     ----------------

    [because a was already in the list]

    after third iteration :

     ----------------
    |      a b       |
     ----------------

    Finally :

     ----------------
    |     a b c      |
     ----------------

    size = 3 which is not equal to length of "aabcc"

    Learn More about Lists Below -
    https://docs.python.org/3/tutorial/datastructures.html
    """
    print_msg_box(message)

def isPermutation(input1,input2,hint=False):
    if(hint is True):
         isPermutation_hint()
    if(len(input1)!=len(input2)):
        return False
    mapp1 = []
    mapp2 = []
    for i in input1:
        mapp1.append(i)
    for j in input2:
        mapp2.append(j)
    mapp1.sort()
    mapp2.sort()

    return mapp1==mapp2

def isPermutation_hint():
    message = """
    Two String Permutations
    ------------------------------------

    Purpose : checking if one string is consisting of the permutation of
    the characters in the other string
    Method : list comprehension

    Time Complexity: Worst Case - O(n), n = length of the strings

    Hint :
    How about using two inbuilt list data structure ?

    Pseudocode:
    --> check if length(string1) != len(string2)
            return False
    --> create two empty lists named mapp1 & mapp2
    --> for i in input string 1
            add i to mapp1
    --> for i in input string 2
            add i to mapp2
    --> sort mapp1
    --> sort mapp2
    --> return true if mapp1 and mapp2 are equal

    Visualization:

    Given Two String :

    "aabcc"

    "abcac"

    Two Empty List:

         List 1                       List 2
     ----------------            ----------------
    |                |          |                |
     ----------------            ----------------

    After Filling Lists :

         List 1                       List 2
     ----------------            ----------------
    |    a a b c c   |          |    a b c a c   |
     ----------------            ----------------

    Applying sort function :

         List 1                       List 2
     ----------------            ----------------
    |    a a b c c   |          |   a a b c c    |
     ----------------            ----------------

    Final check :

     ------------------            +------+
    | List 1 == List 2 |  -------> | True |
     ------------------            +------+


    Learn More about Lists Below -
    https://docs.python.org/3/tutorial/datastructures.html
    """
    print_msg_box(message)

def URLify(input_str,key,hint=False):
    if(hint is True):
         URLify_hint()
    input2 = ""
    for i in range(len(input_str)):
        if(input_str[i] != ' '):
            input2+=input_str[i]
        elif((input_str[i]==' ') and (input_str[i+1] == ' ')):
            return input2
        elif((input_str[i]==' ') and (input_str[i+1] != ' ')):
            input2 += key
    return input2

def URLify_hint():
    message = """
    Making a URL From a String
    ------------------------------------

    Purpose : Making a URL by replacing the spaces with a key value entered
    by the user
    Method : string manipulation

    Time Complexity : Worst Case - O(n), n = length of the string

    Hint :
    Take a blank string, and add data from the input string to the blank
    string to prepare the final URL

    Pseudocode :
    --> Take a blank string s2
    --> for i in [0,length of input string]
            if(not a whitespace)
                add to s2
            elif(whitespace and next place is also whitespace)
                return s2
            elif(whitespace and next place not whitespace)
                add the key value to the blank string

    Visualization:

    Given String To Make URL :

    "Python is love"

    Key : "%20"

    Break The Given String :  /*/ ----> whitespace

    +--------+-------+----+-------+------+
    | Python |  /*/  | is |  /*/  | love |
    +--------+-------+----+-------+------+
        ^              ^             ^
        ^              ^             ^
        ^              ^             ^

        1              2             3

    We will take 1, 2 and 3 sucessively and in place of whitespaces we will
    concatenate the key value.

    Empty String Addition :

    +-+    +--------+   +-------+   +----+   +-------+   +------+
    | |  + | Python | + |  %20  | + | is | + |  %20  | + | love |
    +-+    +--------+   +-------+   +----+   +-------+   +------+

    Learn More about String Concatenation Below -
    https://en.wikipedia.org/wiki/Concatenation
    """
    print_msg_box(message)

def isPalindromicPermutation(input1,hint=False):
    if(hint is True):
         isPalindromicPermutation_hint()
    mapp = {}
    for i in range(len(input1)):
        key = input1[i]
        if(key in mapp.keys()):
            mapp[key] += 1
        else:
            mapp.update({key:1})
    flag = 0
    for i in mapp.keys():
        if(mapp[i] %2 == 1):
            flag+=1
    return flag<=1

def isPalindromicPermutation_hint():
    message = """
    Palindromic Permutation
    ------------------------------------

    Purpose :To check if the permutation of the characters in a string can
    make it palindromic
    Method : string manipulation, palindromic behaviour

    Time Complexity : Worst Case - O(n), n = length of the string

    Hint :
    Make a dictionary of characters and their repeatations.

    Pseudocode :
    --> Take a blank dictionary
    --> for i in [0,length of input string]
            key = input[i]
            if(key in dictionary)
                dictionary[key]+=1
            else
                push {key:1} inside dictionary
    --> Check if dictioary[i] %2 == 1

    Visualization:

    Given String :

    "abbca"

    Making a table using dictionary :

    Step 1 - create a blank dictionary - {}

    Step 2 - check if the key exists

            yes --> add 1

            no  --> push {key:1} inside the dictionary

    Step 3 - You have the following table

    +----------+----------------+
    |   key    |  repeatations  |
    +----------+----------------+
    |    a     |       2        |   --> rem = 0, flag = 0
    -----------------------------
    |    b     |       2        |   --> rem = 0, flag = 0
    -----------------------------
    |    c     |       1        |   --> rem = 0, flag = 1
    -----------------------------

    Step 4 - check reminder, set flag = 0, initially

    Step 5 - return boolean

    Learn More about Python Dictionaries Below -
    https://www.w3schools.com/python/python_dictionaries.asp
    """
    print_msg_box(message)

def oneEditAwayInsert(input1,input2):
    index1 = 0
    index2 = 0
    while((index2 < len(input2)) and (index1 < len(input1))):
        if(input1[index1] != input2[index2]):
            if(index1 != index2):
                return False
            index2+=1
        else:
            index1+=1
            index2+=1
    return True

def oneEditAwayReplace(input1,input2):
    flag = False
    for i in range(len(input1)):
        if(input2[i]!=input1[i]):
            if(flag):
                return False
            flag = True
    return True

def oneEditAway(input1,input2,hint=False):
    if(hint is True):
         oneEditAway_hint()
    if(len(input1)==len(input2)):
        return  oneEditAwayReplace(input1,input2)
    elif(len(input1)+1==len(input2)):
        return  oneEditAwayInsert(input1,input2)
    elif(len(input1)-1==len(input2)):
        return  oneEditAwayInsert(input2,input1)
    return False

def oneEditAway_hint():
    message = """
    One Edit Away
    ------------------------------------

    Purpose : Check if two strings are one edit (or zero) away,where edit
    means the following three methods,
        - inserting a character
        - removing a character
        - replacing a character

    Method : string manipulation

    Time Complexity : Worst Case - O(n), n = length of the greater string

    Hint :
    Divide the problem in three cases of insert, remove and replace
    and solve the problem.

    Pseudocode :

    For checking "replace" :

    --> flag = False
    --> for i in range(len(input1)):
            if(input2[i]!=input1[i]):
                if(flag):
                    return False
                flag = True

    For checking "insert" & "remove" :

    --> index1 = 0
    --> index2 = 0
    --> while((index2 < len(input2)) and (index1 < len(input1))):
            if(input1[index1] != input2[index2]):
                if(index1 != index2):
                    return False
                    index2+=1
                else:
                    index1+=1
                    index2+=1
            return True

    """
    print_msg_box(message)

def compressedString(input1,hint=False):
    if(hint is True):
         compressedString_hint()
    mapp = {}
    output = ""
    for i in range(len(input1)):
        key = input1[i]
        if(key in mapp.keys()):
            mapp[key]+=1
        else:
            mapp.update({key:1})
    for key,value in mapp.items():
        output = output + key + str(value)
    if(len(output) <= len(input1)):
        return output
    else:
        return input1

def compressedString_hint():
    message = """
    Compress The String
    ------------------------------------

    Purpose :To compress the size of string by making a summary of the
    repeatation of the characters
    Method : string manipulation, python dictionary

    Time Complexity : Worst Case - O(n), n = length of the string

    Hint :
    Make a dictionary of characters and their repeatations. Finaally forge a
    new string and return it

    Pseudocode :
    --> Take a blank dictionary
    --> Take a blank string output
    --> for i in [0,length of input string]
            key = input[i]
            if(key in dictionary)
                dictionary[key]+=1
            else
                push {key:1} inside dictionary
    --> prepare the output string

    Visualization:

    Given String :

    "aabbcccdddeeef"

    Making a table using dictionary :

    Step 1 - create a blank dictionary - {}

    Step 2 - check if the key exists

            yes --> add 1

            no  --> push {key:1} inside the dictionary

    Step 3 - You have the following table

    +----------+----------------+
    |   key    |  repeatations  |
    +----------+----------------+
    |    a     |       2        |
    -----------------------------
    |    b     |       2        |
    -----------------------------
    |    c     |       3        |
    -----------------------------
    |    d     |       3        |
    -----------------------------
    |    e     |       3        |
    -----------------------------
    |    f     |       1        |
    -----------------------------

    Step 4 - prepare the output string as "a2b2c3d3e3f1"

    Learn More about Python Dictionaries Below -
    https://www.w3schools.com/python/python_dictionaries.asp
    """
    print_msg_box(message)

# boyer moore algorithm 
NO_OF_CHARACTERS = 256

def badCharHeuristic(string, size): 
    badChar = [-1] * NO_OF_CHARACTERS 
    for i in range(size): 
        badChar[ord(string[i])] = i; 
    return badChar 

def boyer_moore(text, pattern, hint = False): 
    m = len(pattern) 
    n = len(text) 
    badChar = badCharHeuristic(pattern, m)  
    s = 0
    while(s <= n - m): 
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]: 
            j -= 1 
        if j < 0: 
            print("Pattern occurs at shift = {}".format(s)) 
            s += (m - badChar[ord(text[s + m])] if s + m < n else 1) 
        else: 
            s += max(1, j - badChar[ord(text[s + j])]) 
    if(hint is True):
        boyer_moore_hint()

def boyer_moore_hint():
    message ="""
    Boyer Moore Algorithm
    ------------------------------------
    Boyer Moore algorithm is considered as the most efficient string searching algorithm. 
    This algorithm takes a 'backward' approach. A simplified version of it or the entire 
    algorithm is used in text editors for search and substitute commands.

    Purpose : Efficient string searching

    Method : The pattern string (P) is aligned with the start of the text string (T), and 
             then compares the characters of the pattern from right to left, beginning with 
             the rightmost character.

    Time Complexity : Best Case - O(m) preprocessing + O(n/m) matching 
                      {n = length of pattern, m = length of text}

                      Worst Case - O(m) preprocessing + O(m*n) matching 
                      {n = length of pattern, m = length of text}

    Hint : 
        - The algorithm scans the characters of the pattern from right to left beginning with 
          the rightmost one. In case of a mismatch (or a complete match of the whole pattern) 
          it uses two pre-computed functions to shift the window to the right.

        - If a character is compared that is not within the pattern, no match can be found by
          analyzing any further aspects at this position so the pattern can be changed 
          entirely past the mismatching character.

    Pseoducode :
        -- fullSuffixMatch(shiftArray, borderArray, pattern)
        
        Begin
        n := pattern length
        j := n
        j := n+1
        borderArray[i] := j
        while i > 0, do
            while j <= n AND pattern[i - 1] ≠ pattern[j - 1], do
                if shiftArray[j] = 0, then
                shiftArray[j] := j - i;
            j := borderArray[j];
            done
            decrease i and j by 1
            borderArray[i] := j
        done
        End
 
        -- partialSuffixMatch(shiftArray, borderArray, pattern)

        Begin
        n := pattern length
        j := borderArray[0]
        for index of all characters ‘i’ of pattern, do
            if shiftArray[i] = 0, then
                shiftArray[i] := j
            if i = j then
                j := borderArray[j]
        done
        End

        -- boyer_moore(text, pattern)
        
        Begin
        patLen := pattern length
        strLen := text size

        for all entries of shiftArray, do
            set all entries to 0
        done

        call fullSuffixMatch(shiftArray, borderArray, pattern)
        call partialSuffixMatch(shiftArray, borderArray, pattern)
        shift := 0

        while shift <= (strLen - patLen), do
            j := patLen -1
            while j >= 0 and pattern[j] = text[shift + j], do
            decrease j by 1
        done

        if j < 0, then
            print the shift as, there is a match
            shift := shift + shiftArray[0]
        else
            shift := shift + shiftArray[j + 1]
        done
        End

    Visualization :

        Given Text - ABAAABCD
        Given Pattern - ABC

        +-----+-----+-----+-----+-----+-----+-----+-----+
        |  A  |  B  |  A  |  A  |  A  |  B  |  C  |  D  |
        +-----+-----+-----+-----+-----+-----+-----+-----+
                       |
                       X
                       |
        +-----+-----+-----+
        |  A  |  B  |  C  |
        +-----+-----+-----+   

        -------------------------------------------------

        +-----+-----+-----+-----+-----+-----+-----+-----+
        |  A  |  B  |  A  |  A  |  A  |  B  |  C  |  D  |
        +-----+-----+-----+-----+-----+-----+-----+-----+
                                   |
                                   X
                                   |
                    +-----+-----+-----+
                    |  A  |  B  |  C  |
                    +-----+-----+-----+   
      
        -------------------------------------------------

        +-----+-----+-----+-----+-----+-----+-----+-----+
        |  A  |  B  |  A  |  A  |  A  |  B  |  C  |  D  |
        +-----+-----+-----+-----+-----+-----+-----+-----+
                                   |     |     |
                                   |     |     |
                                   |     |     |
                                +-----+-----+-----+
                                |  A  |  B  |  C  |
                                +-----+-----+-----+ 

        Hence, the pattern occurs at shift 4.

    Learn more here - https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm
    """
    print_msg_box(message)
