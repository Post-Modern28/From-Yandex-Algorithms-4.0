# This program creates Z-function for a given string s

modulo = 10**9 + 7

s = input()
n = len(s)
x = 257
h = [0] * (n + 1)
x_powers = [1] * (n + 1)
s = ' ' + s
for i in range(1, n+1):
    h[i] = (h[i-1] * x + ord(s[i]) - ord('a') + 1) % modulo
    x_powers[i] = (x_powers[i-1] * x) % modulo


def are_same(pos1, pos2, l):
    if pos1 + l > n + 1 or pos2 + l > n + 1:
        return False
    f1 = (h[pos1+l-1] + h[pos2-1] * x_powers[l]) % modulo
    f2 = (h[pos2+l-1] + h[pos1-1] * x_powers[l]) % modulo

    return f1 == f2


def bin_search(pos):
    global n
    rb = n+1
    lb = pos
    while lb <= rb:
        middle = (lb+rb) // 2
        l = middle - pos + 1
        if are_same(1, pos, l):
            lb = middle + 1
        else:
            rb = middle - 1
    return lb-pos


for i in range(n+1):
    if i == 1:
        continue
    print(bin_search(i), end=' ')
