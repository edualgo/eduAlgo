def stack_sequence(pushes : list , pops : list):
    '''
 Function to check whether the given sequence of pop can be 
 achieved from the given push sequences 
 in a stack. eg- push -> 1 2 3 4 5 , pop -> 3 2 1 5 4 is a valid sequence 
    '''
    stack = []
    sequence = []
    i = 0
    j = 0
    for n in pushes:
        stack.append(n)
        sequence.append(f"Push[{n}]")
        j += 1
        while l and stack[-1] == pops[i]:
            sequence.append(f"Pop[{stack.pop()}]")
            i += 1
            j -= 1
    return sequence


if __name__ == "__main__":
    '''
Input format -> 1st line : integers with space
2nd line : integers with space
length(pushes)==length(pops)
    '''
    pushesin = list(map(int , input().split()))
    popsin = list(map(int , input().split()))
    output = stack_sequence(pushesin , popsin)
    if len(output) == 2*len(pushes):
        print("")
        for sequnce in output:
            print(sequnce , end=" ")
    else:
        print("The sequences isn't valid\n")
