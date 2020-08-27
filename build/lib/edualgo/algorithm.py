import time

# 'sort' class contains the following algorithms:
#     1 - Bubble sort
#     2 - Selection sort
#     3 - Insertion sort
#     4 - Merge sort
#     5 - Quick sort
#     6 - Counting sort
#     7 - Radix sort
#     8 - Heap sort
#     9 - Bucket sort

class sort:

    # bubble sort algorithm
    def bubble_sort(self,arr):
        start = time.time()
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1] :
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        end = time.time()
        print("Bubble Sort Runtime = {}".format(end-start))
        return arr

    # selection Sort Algorithm
    def selection_sort(self,arr):
        start = time.time()
        for i in range(len(arr)-1):
            minimum = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j
            arr[minimum],arr[i] = arr[i],arr[minimum]
        end = time.time()
        print("Selection Sort Runtime = {}".format(end-start))
        return arr

class string_algorithms:

    def isUnique(self,input_string):
        mapp = []
        for i in input_string:
            if i not in mapp:
                mapp.append(i)
        return len(mapp) == len(input_string)

    def isPermutation(self,input1,input2):
        mapp1 = []
        mapp2 = []
        for i in input1:
            if i not in mapp1:
                mapp1.append(i)
        for j in input2:
            if j not in mapp2:
                mapp2.append(j)
        mapp1.sort()
        mapp2.sort()
        return mapp1==mapp2

    def URLify(self,input_str,key):
        input2 = ""
        for i in range(len(input_str)):
            if(input_str[i] != ' '):
                input2+=input_str[i]
            elif((input_str[i]==' ') and (input_str[i+1] == ' ')):
                return input2
            elif((input_str[i]==' ') and (input_str[i+1] != ' ')):
                input2 += key
        return input2

    def isPalindromicPermutation(self,input1):
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

    def oneEditAwayInsert(self,input1,input2):
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

    def oneEditAwayReplace(self,input1,input2):
        flag = False
        for i in range(len(input1)):
            if(input2[i]!=input1[i]):
                if(flag):
                    return False
                flag = True
        return True

    def oneEditAway(self,input1,input2):
        if(len(input1)==len(input2)):
            return self.oneEditAwayReplace(input1,input2)
        elif(len(input1)+1==len(input2)):
            return self.oneEditAwayInsert(input1,input2)
        elif(len(input1)-1==len(input2)):
            return self.oneEditAwayInsert(input2,input1)
        return False

    def compressedString(self,input1):
        mapp = {}
        output = ""
        for i in range(len(input1)):
            key = input1[i]
            if(key in mapp.keys()):
                mapp[key]+=1
            else:
                mapp.update({key:1})
        for key in mapp.keys():
            output = output + key + str(mapp[key])
        if(len(output) <= len(input1)):
            return output
        else:
            return input1

    def rotateImage(self,img_arr,n):
        for layer in range(int(n/2)):
            first = layer
            last = n-1-layer
            for i in range(first,last):
                offset = i - first
                top = img_arr[first][i]
                img_arr[first][i] = img_arr[last - offset][first]
                img_arr[last - offset][first] = img_arr[last][last - offset]
                img_arr[last][last - offset] = img_arr[i][last]
                img_arr[i][last] = top
