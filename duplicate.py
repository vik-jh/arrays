#find duplicate

import sys

def duplicateNumber(arr, n) :
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i]==arr[j]:
                return arr[i]
                

x = input()
n = int(x)
arr = [int(y) for y in input.split]
