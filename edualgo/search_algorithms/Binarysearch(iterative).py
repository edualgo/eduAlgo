#divide and conquer: [iterative]
def bin(arr,x):
    low=0
    high=len(arr)-1
    mid=0
    while(low<=high):
        mid=(high+low)//2 
        if(arr[mid]<x):
            low=mid+1 
        elif(arr[mid]>x):
            high=mid-1
        else:
            return mid 
    return -1
arr=[2,3,21]
x=32
res=bin(arr,x)
if res!=-1:
    print("at indes",str(res))
else:
    print("not present")
    

