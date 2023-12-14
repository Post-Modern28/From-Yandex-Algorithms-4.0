# This program solves simple salesman problem

n = int(input())

adj_matrix = []
min_edge = float('inf')
min_dist = float('inf')
for i in range(n):
    row = list(map(int, input().split()))
    for j, val in enumerate(row):
        if not val:
            row[j] = float('inf')
    min_edge = min(min_edge, min(row))
    adj_matrix.append(row)


visited_vertices = [0] * n


def backtrack_traversal(vert=0, cur_dist=0, vert_visited=0):
    global min_dist
    if vert_visited == n-1:
        if not vert:
            min_dist = 0
            return
        min_dist = min(cur_dist+adj_matrix[vert][0], min_dist)
        return
    if cur_dist + min_edge*(n-vert_visited) >= min_dist:
        return
    for neigh in range(1, n):
        if not visited_vertices[neigh]:
            visited_vertices[neigh] = 1
            backtrack_traversal(neigh, cur_dist+adj_matrix[vert][neigh], vert_visited+1)
            visited_vertices[neigh] = 0
    return


backtrack_traversal()
if min_dist == float('inf'):
    min_dist = -1
print(min_dist)
