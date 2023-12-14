# This program implements partitioning of an array

n = int(input())
arr = list(map(int, input().split()))
x = int(input())


def partition(arr, pivot):
    less = 0
    other = 0
    for i in arr:
        if i < pivot:
            less += 1
        else:
            other += 1
    print(less)
    print(other)


partition(arr, x)
