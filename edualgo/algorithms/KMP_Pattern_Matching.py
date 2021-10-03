def calculate_longest_prefix_suffix(pattern, lps):
    length = len(pattern)

    lps[0] = 0  #lps of 0th index is always 0

    l = 0
    pos = 1
    while pos < length:
        if pattern[pos] == pattern[l]:
            lps[pos] = l + 1
            l += 1
            pos += 1
        else:
            if l != 0:
                l = lps[l-1]
            else:
                lps[pos] = 0
                pos += 1

def KMP(pattern, input_str):
    '''
        Time Complexity: O(N)
    '''
    flag = 0
    
    input_len = len(input_str)
    pat_len = len(pattern)

    if not pat_len:
        return 0

    lps = [0] * pat_len
    
    # generate lps
    calculate_longest_prefix_suffix(pattern, lps)

    i = 0
    j = 0
    while i < input_len:
        if input_str[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == pat_len:
            print("Match found at index", (i-j))
            flag = 1
            j = lps[j-1]
    if flag == 0:
        print("Match not found!!")


if __name__ == "__main__":
    
    input_str = "ABABDABACDABABCABAB"
    pattern = "ABABC"
    
    print("Input string =", input_str)
    print("Pattern to be searched =", pattern)

    # Function cal
    KMP(pattern, input_str)


