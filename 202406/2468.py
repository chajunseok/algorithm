dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, tmp):
    stack = [(x, y)]
    visited[x][y] = 1

    while stack:
        cx, cy = stack.pop()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and field[nx][ny] > tmp:
                stack.append((nx, ny))
                visited[nx][ny] = 1


N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
high_value = max(map(max, field))
max_value = 0

for water in range(high_value + 1):
    safe_area = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if field[i][j] > water and not visited[i][j]:
                dfs(i, j, water)
                safe_area += 1

    max_value = max(max_value, safe_area)

print(max_value)
