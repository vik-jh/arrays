#Find the intersection of Arrays
import sys

def intersections(arr1, n, arr2, m):

    for i in range(n):
        for j in range(m):
            if arr1[i] == arr2[j]:
                print(arr1[i], end=" ")
                arr2[j] = sys.maxsize
                break



n = int(input())
arr1 = [int(x) for x in input().split]
m = int(input())
arr2 = [int(u) for u in input().split]
