# This program uses optimized bruteforce to find the number of ways to place N queens on NxN board

n = int(input())


count = 0
matrix = [[0 for _ in range(n)] for __ in range(n)]


def add_numbers(x, y):
    matrix[x][y] -= 1
    for i in range(n):
        matrix[x][i] += 1
        matrix[i][y] += 1
    for i in range(1, n):
        x_coord1 = x + i
        y_coord1 = y + i
        x_coord2 = x - i
        y_coord2 = y - i
        if 0 <= x_coord1 < n and 0 <= y_coord1 < n:
            matrix[x_coord1][y_coord1] += 1
        if 0 <= x_coord1 < n and 0 <= y_coord2 < n:
            matrix[x_coord1][y_coord2] += 1
        if 0 <= x_coord2 < n and 0 <= y_coord2 < n:
            matrix[x_coord2][y_coord2] += 1
        if 0 <= x_coord2 < n and 0 <= y_coord1 < n:
            matrix[x_coord2][y_coord1] += 1


def subtract_numbers(x, y):
    matrix[x][y] += 1
    for i in range(n):
        matrix[x][i] -= 1
        matrix[i][y] -= 1
    for i in range(1, n):
        x_coord1 = x + i
        y_coord1 = y + i
        x_coord2 = x - i
        y_coord2 = y - i
        if 0 <= x_coord1 < n and 0 <= y_coord1 < n:
            matrix[x_coord1][y_coord1] -= 1
        if 0 <= x_coord1 < n and 0 <= y_coord2 < n:
            matrix[x_coord1][y_coord2] -= 1
        if 0 <= x_coord2 < n and 0 <= y_coord2 < n:
            matrix[x_coord2][y_coord2] -= 1
        if 0 <= x_coord2 < n and 0 <= y_coord1 < n:
            matrix[x_coord2][y_coord1] -= 1


taken_row = [0] * n
taken_column = [0] * n


def place_dinosaurs(cur_col=0):
    global count
    if cur_col == n:
        count += 1
        return
    for i in range(n):
        if taken_row[i]:
            continue
        if not matrix[i][cur_col]:
            add_numbers(i, cur_col)
            taken_row[i] = 1
            taken_column[cur_col] = 1
            place_dinosaurs(cur_col=cur_col + 1)
            subtract_numbers(i, cur_col)
            taken_row[i] = 0
            taken_column[cur_col] = 0


place_dinosaurs()
print(count)
