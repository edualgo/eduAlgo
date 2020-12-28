def bin(arr,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return bin(arr,low,mid-1,x)
        else:
            return bin(arr,mid+1,high,x)
    else:
        return -1
arr=[2,3,21]
x=3
res=bin(arr,0,len(arr)-1,x)
if res!=-1:
    print("at indes",str(res))
else:
    print("not present")
