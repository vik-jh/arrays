from sys import stdin

def pairSum(arr, n, x):

    numPairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j] == x):
                numPairs +=1

    return numPairs


arr = [int(x) for x in input().split()]
n = int(input())
x = int(input()) #sum 


