# This program implements Dijkstra algorithm which prints the shortest path

from queue import PriorityQueue
n, s, f = map(int, input().split())
adjacency_matrix = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == -1:
            arr[j] = float('inf')
    adjacency_matrix.append(arr)



def Dijkstra(adj_matrix, start_point, end_point):
    n = len(adj_matrix)
    q = PriorityQueue()
    min_distances = [float('inf')] * n
    min_distances[start_point] = 0
    visited = [False] * n
    visited[start_point] = True
    parent_vertex = [float('inf')] * n
    parent_vertex[start_point] = -1
    for i in range(n):
        if i == start_point:
            continue
        q.put([adj_matrix[start_point][i], i])
        min_distances[i] = adj_matrix[start_point][i]
        if min_distances[i] != float('inf'):
            parent_vertex[i] = start_point
    while not q.empty():
        lowest_dist, idx = q.get()
        if visited[idx]:
            continue
        for i in range(n):
            if i == idx:
                continue
            if min_distances[idx] + adj_matrix[idx][i] < min_distances[i]:
                min_distances[i] = min_distances[idx] + adj_matrix[idx][i]
                parent_vertex[i] = idx
            if not visited[i]:
                q.put([min_distances[i], i])
        visited[idx] = True
    if min_distances[end_point] == float('inf'):
        return -1
    x = end_point
    st = [x]
    while x != start_point:
        st.append(parent_vertex[x])
        x = parent_vertex[x]
    st.reverse()
    for i in range(len(st)):
        st[i] += 1

    return st


res = Dijkstra(adjacency_matrix, s-1, f-1)
if type(res) == int:
    print(res)
else:
    print(*res)
