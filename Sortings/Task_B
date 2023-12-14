# This program implements Quick Sort
from random import randint


def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    less = []
    equal = []
    bigger = []
    piv_idx = randint(0, len(arr)-1)
    pivot = arr[piv_idx]
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            bigger.append(i)
    return QuickSort(less) + equal + QuickSort(bigger)


def run():
    n = int(input())
    if n == 0:
        return
    a = list(map(int, input().split()))
    print(*QuickSort(a))


run()
