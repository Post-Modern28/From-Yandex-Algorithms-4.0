# Task description: given weighthened unoriented graph, divide its vertices in 2 groups in such way that the sum of weighs of edges
# connecting vertices from different groups is maximized.

from itertools import combinations, permutations

n = int(input())
adj_matrix = []
max_dist = 0
for i in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)


left_side = set()
right_side = {*range(n)}
best_option = None


def backtrack(vertex=0, l=0, cur_dist=0):
    global max_dist, best_option
    if vertex == n:
        return
    if cur_dist > max_dist:
        max_dist = cur_dist
        best_option = left_side.copy()

    right_side.remove(vertex)
    for i in left_side:
        cur_dist -= adj_matrix[i][vertex]
    left_side.add(vertex)
    for i in right_side:
        cur_dist += adj_matrix[i][vertex]
    backtrack(vertex+1, l+1, cur_dist)
    left_side.remove(vertex)
    for i in right_side:
        cur_dist -= adj_matrix[i][vertex]
    right_side.add(vertex)
    for i in left_side:
        cur_dist += adj_matrix[i][vertex]
    backtrack(vertex + 1, l + 1, cur_dist)


backtrack()
print(max_dist)
for i in range(n):
    if i in best_option:
        print(1, end=' ')
    else:
        print(2, end=' ')
