from collections import deque

N, M = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(N)]

visited = [[[101 * N * M] * 3 for _ in range(M)] for _ in range(N)]
directions = [(1, -1), (1, 0), (1, 1)]

queue = deque()
for i in range(M):
    for d in range(3):
        visited[0][i][d] = fuel[0][i]
    queue.append((0, i, -1))

while queue:
    x, y, prev_dir = queue.popleft()
    for d, (dx, dy) in enumerate(directions):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if d == prev_dir:
                continue

            if visited[nx][ny][d] > visited[x][y][prev_dir] + fuel[nx][ny]:
                visited[nx][ny][d] = visited[x][y][prev_dir] + fuel[nx][ny]
                queue.append((nx, ny, d))

min_fuel = min(visited[N-1][j][d] for j in range(M) for d in range(3))
print(min_fuel)
