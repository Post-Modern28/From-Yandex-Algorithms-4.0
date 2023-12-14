n = int(input())
buckets = [[] for _ in range(10)]
buckets2 = [[] for _ in range(10)]
print("Initial array:")
num = None
for i in range(n):
    num = input()
    print(f'{num}{", " if i != n-1 else ""}', end='\n' if i == n-1 else '')

    last_digit = int(num[-1])
    buckets[last_digit].append(num)

print('**********')
k = len(num)
for i in range(1, k+1):
    for j in range(10):
        for elem in buckets[j]:
            buckets2[int(elem[k-i])].append(elem)
    buckets, buckets2 = buckets2, [[] for _ in range(10)]
    print(f"Phase {i}")
    for j in range(10):
        print(f'Bucket {j}:', end=' ')
        if not buckets[j]:
            print('empty')
        else:
            print(*buckets[j], sep=', ')
    print('**********')
print("Sorted array:")
arr = []
for i in range(10):
    for elem in buckets[i]:
        arr.append(elem)
print(*arr, sep=', ')


