# This program reads the string and finds the number of substrings which are palindromes

modulo = 10**9 + 7

s = input()
n = len(s)
x = 257
h = [0] * (n + 1)
h_rev = [0] * (n + 1)
x_powers = [1] * (n + 1)
s = s
s_rev = s[::-1]
for i in range(1, n+1):
    h[i] = (h[i-1] * x + ord(s[i-1]) - ord('a') + 1) % modulo
    h_rev[i] = (h_rev[i-1] * x + ord(s_rev[i-1]) - ord('a') + 1) % modulo
    x_powers[i] = (x_powers[i-1] * x) % modulo


def are_same(pos1, pos2, l):
    if pos1 + l > n + 1 or pos2 + l > n + 1:
        return False
    f1 = (h[pos1+l-1] + h[pos2-1] * x_powers[l]) % modulo
    f2 = (h[pos2+l-1] + h[pos1-1] * x_powers[l]) % modulo

    return f1 == f2


def are_same2(pos1, pos2, l):
    if pos1 + l > n + 1 or pos2 + l > n + 1:
        return False
    f1 = (h[pos1+l-1] - h[pos1-1] * x_powers[l]) % modulo
    f2 = (h_rev[pos2+l-1] - h_rev[pos2-1] * x_powers[l]) % modulo
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


def binary_search_odd(center):
    left = 1
    right = min(center, n-center+1)
    while left <= right:
        string_len = (left + right) // 2
        lpos = center - string_len + 1  # center - lpos = strlen - 1 => lpos = center - strlen + 1
        rpos_orig = center + string_len - 1
        # rpos = n - center + string_len  # rpos = n - center - string_len - 2
        rpos = n - rpos_orig + 1

        if are_same2(lpos, rpos, string_len):
            left = string_len + 1
        else:
            right = string_len - 1
    return left - 1


def binary_search_even(center):
    left = 1
    right = min(center, n-center)
    while left <= right:
        string_len = (left + right) // 2
        lpos = center - string_len + 1  # center - lpos = strlen - 1 => lpos = center - strlen + 1
        rpos_orig = center + string_len
        # rpos = n - center + string_len  # rpos = n - center - string_len - 2
        rpos = n - rpos_orig + 1

        if are_same2(lpos, rpos, string_len):
            left = string_len + 1
        else:
            right = string_len - 1
    return left - 1


def count_palindromes():
    res = 0

    for i in range(1, n+1):
        # print(i, end=': ')
        r1 = binary_search_odd(i)
        r2 = binary_search_even(i)
        # print(r1, r2, sep=' ')
        res += r1 + r2

    return res


print(count_palindromes())
