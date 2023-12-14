# This program generates all regular bracket sequences of parentheses and square brackets of length n in lexicographical order.

n = int(input())

s = set()

opening = '(['
closing = ')]'


def generate_parentheses(word='', l=0, st='', opening_count=0):
    if l == n:
        print(word)
    if opening_count < n//2:
        for par in opening:
            generate_parentheses(word+par, l+1, st+par, opening_count+1)
    for i, par in enumerate(closing):
        if st and opening[i] == st[-1]:
            generate_parentheses(word+par, l+1, st[:-1], opening_count)


generate_parentheses()

