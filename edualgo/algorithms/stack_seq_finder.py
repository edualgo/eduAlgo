def stack_sequence(pushes , pops):
    """Stack Sequence Finder using python"""
    stack = []
    sequence = []
    i = 0
    j = 0
    for n in pushes:
        stack.append(n)
        sequence.append(f"Push[{n}]")
        j += 1
        while j and stack[-1] == pops[i]:
            sequence.append(f"Pop[{stack.pop()}]")
            i += 1
            j -= 1
    return sequence


if __name__ == "__main__":
    pushesin = list(map(int , input().split()))
    popsin = list(map(int , input().split()))
    output = stack_sequence(pushesin , popsin)
    if len(output) == 2*len(pushesin):
        print("")
        for sequnce in output:
            print(sequnce , end=" ")
    else:
        print("The sequences isn't valid\n")
