from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not box[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 1

bfs()

max_days = 0
is_all_ripe = True
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            if visited[i][j] == 0:
                is_all_ripe = False
            else:
                max_days = max(max_days, visited[i][j] - 1)

if is_all_ripe:
    print(max_days)
else:
    print(-1)