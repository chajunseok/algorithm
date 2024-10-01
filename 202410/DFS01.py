def dfs(graph, c, r, visited):
    visited[c][r] = True
    for dy, dx in [(1, 0), (0, 1)]:
        ny, nx = c + dy, r + dx
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and not graph[ny][nx]:
            dfs(graph, ny, nx, visited)


N, M = map(int, input().split())
ice = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if not ice[i][j] and not visited[i][j]:
            dfs(ice, i, j, visited)
            cnt += 1

print(cnt)