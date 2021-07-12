#find unique element
import sys
def findUnique(arr, n):
    # we take an element one by one and compare with the whole array
    for i in range(n):
        count=0 # to count
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1  #increase the count if same is found
        #after going through the whole array
        #if the element is unique then the count will be 1 right?
        if count==1:
            return arr[i]


n = int(input())
arr =[int(x) for x in input.split()]
    