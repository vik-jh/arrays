#Find the triple sum 

from sys import stdin

def tripletArrSum(arr, x):
    tripletSum = 0

    n = len(arr)

    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == x):
                    tripletSum +=1
    return tripletSum



arr = [int(y)for y in input().split()]
x = int(input())

ans = tripletArrSum(arr,x)
print(ans)



