# Task description: you are given N points. Each point has 2 numbers affiliated with it: speed of a vehicle that stands on this point (in km/h) 
# and the time required to get into this vehicle. Then you are given N-1 roads between the points. The graph is guaranteed to be connected (actually, it's a tree)
# From each point 1 person moves to point 1. Find minimum time it will take the last person to arrive.
import sys
sys.setrecursionlimit(10000000)
n = int(input())
stations = [[-1, -1]]
edges = []
for _ in range(n):
    stations.append(list(map(int, input().split())))
for _ in range(n - 1):
    edges.append(list(map(int, input().split())))

distances = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
    distances[i][i] = 0
adj_list = [[] for i in range(n + 1)]
adj_matrix = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
for v1, v2, dist in edges:
    distances[v1][v2] = dist
    distances[v2][v1] = dist
    adj_list[v1].append([v2, dist])
    adj_list[v2].append([v1, dist])
    adj_matrix[v1][v2] = dist
    adj_matrix[v2][v1] = dist


def Dijkstra(S, matrix):
    N = len(matrix)
    valid = [True] * N
    weight = [float('inf')] * N
    weight[S] = 0
    parent = [float('inf')] * N
    for i in range(N):
        min_weight = float('inf')
        ID_min_weight = -1
        for j in range(N):
            if valid[j] and weight[j] < min_weight:
                min_weight = weight[j]
                ID_min_weight = j
        for z in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][z] < weight[z]:
                weight[z] = weight[ID_min_weight] + matrix[ID_min_weight][z]
                parent[z] = ID_min_weight
        valid[ID_min_weight] = False
    max_time = max(weight[1:])
    idx = weight.index(max_time)
    st = [idx]
    while idx != S:
        st.append(parent[idx])
        idx = parent[idx]
    return max_time, st


vistited = [0] * (n + 1)


def calculate_distances(main_vertex, cur_vertex, cur_dist=0):
    vistited[cur_vertex] = 1
    for v, d in adj_list[cur_vertex]:
        distances[main_vertex][v] = min(distances[main_vertex][v], cur_dist + d)
        if not vistited[v]:
            calculate_distances(main_vertex, v, cur_dist + d)
    vistited[cur_vertex] = 0


for i in range(1, n + 1):
    calculate_distances(i, i)

times = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
    times[i][i] = 0


for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        change_time, speed = stations[i]
        times[i][j] = change_time + distances[i][j] / speed


def transpose_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


transpose_matrix(times)
res = Dijkstra(1, times)
print(res[0])
print(*res[1])
