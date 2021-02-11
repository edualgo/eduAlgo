import numpy as np
from random import choice

def sublinear(inplist, x):
    randlist = np.array(inplist)
    np.random.shuffle(randlist)
    s = randlist[:int(len(inplist)**0.5)]
    presence = False
    p = s[0]
    q = s[0]
    minp = p - x
    maxq = x - q
    for i in range(len(s)):
        if s[i] <= x and x-s[i] < minp:
            p = s[i]
            minp = p - x
        if s[i] > x and s[i]-x < maxq:
            q = s[i]
            maxq = x - q

    for i in range(inplist.index(p),inplist.index(q)):
        if inplist[i] == x:
            presence = True
            break
    return presence
  
arr = [i for i in range(0,10000,3)]
iterations = 10000

listoutputs = []

for i in range(iterations):
    n = choice(arr)
    pre = sublinear(arr, n)
    listoutputs.append(pre)
    
print('Number of Trials:', len(listoutputs))
print('Number of Trues:',listoutputs.count(True))
print('Numer of False:',listoutputs.count(False))

# Output: Number of Trials:10000  Number of Trues:9320  Numer of False:680
