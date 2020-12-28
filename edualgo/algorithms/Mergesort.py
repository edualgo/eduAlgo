def mergesort(list1):
    
 if len(list1)>1:
    mid=len(list1)//2
    llist=list1[:mid]
    rlist=list1[mid:]
    mergesort(llist)
    mergesort(rlist)
    i=0 #left 
    j=0  #right
    k=0  #list1
    while len(llist)>i and len(rlist)>j:
        if llist[i]<rlist[j]:
            list1[k]=llist[i]
            i=i+1 
            k=k+1 
        else:
            list1[k]=rlist[j]
            j=j+1
            k=k+1
    while len(llist)>i:
        list1[k]=llist[i]
        i=i+1 
        k=k+1 
    while len(rlist)>j:
        list1[k]=rlist[j]
        j=j+1 
        k=k+1 
           
n=int(input("enter the elem"))
list1=[int(input()) for x in range(n)]
mergesort(list1)
print("soted ",list1)
