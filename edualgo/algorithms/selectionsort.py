arr=[1,3,1321,33,0]
for i in range(len(arr)):
    min=i 
    for j in range(i+1,len(arr)):
        if(arr[min]>arr[j]):
            min=j 
    arr[i],arr[min]=arr[min],arr[i]
print("after sorting")
for i in range(len(arr)):
    print(arr[i])
