
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


def run():
    n1 = int(input())
    a1 = list(map(int, input().split()))
    n2 = int(input())
    a2 = list(map(int, input().split()))
    print(*merge(a1, a2))


run()
