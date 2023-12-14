# This program prints all permutations of digits from 1 to n (1 <= n < 10)

n = int(input())

s = set()


def permutations(word, l, digit):
    s.add(digit)
    if l == n:
        print(word)
        return
    for i in range(1, n+1):
        if i in s:
            continue
        permutations(word + str(i), l+1, i)
        s.remove(i)


permutations('', 0, -1)

