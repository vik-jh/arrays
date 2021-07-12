from sys import stdin

def sortZeroesAndOne(arr):

    n =len(arr)
    nextZero = 0
    for i in range(n):
        if arr[i] == 0:
            arr[i], arr[nextZero] = arr[nextZero], arr[i]
            nextZero +=1



arr = [int(y)for y in input().split()]

print(sortZeroesAndOne(arr))


