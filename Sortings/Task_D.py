# This program implements Merge Sort

def merge(arr1, arr2):
    p1 = p2 = 0
    l1 = len(arr1)
    l2 = len(arr2)
    new_arr = []
    while p1 < l1 and p2 < l2:
        if arr1[p1] < arr2[p2]:
            new_arr.append(arr1[p1])
            p1 += 1
        else:
            new_arr.append(arr2[p2])
            p2 += 1
    while p1 < l1:
        new_arr.append(arr1[p1])
        p1 += 1
    while p2 < l2:
        new_arr.append(arr2[p2])
        p2 += 1
    return new_arr


def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    return merge(MergeSort(left), MergeSort(right))


def run():
    n1 = int(input())
    if n1 == 0:
        return 
    a1 = list(map(int, input().split()))
    print(*MergeSort(a1))


run()
