from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(): # 최소 거리를 구하는 문제 -> bfs
    while queue:
        cx, cy, cz = queue.popleft()
        for k in range(6):
            nx = cx + dx[k]
            ny = cy + dy[k]
            nz = cz + dz[k]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and not box[nz][nx][ny] and not visited[nz][nx][ny]:
            # 토마토가 있다면 and 방문한적 없다면
                queue.append((nx, ny, nz))
                visited[nz][nx][ny] = visited[cz][cx][cy] + 1 # 방문 표시를 부모노드의 거리로


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
queue = deque()

for u in range(H):
    for i in range(N):
        for j in range(M):
            if box[u][i][j] == 1:
                queue.append((i, j, u)) # 토마토 위치를 미리 구하고 시작
                visited[u][i][j] = 1

bfs()

max_days = 0
is_all_ripe = True
for u in range(H):
    for i in range(N):
        for j in range(M):
            if box[u][i][j] == 0:
                if visited[u][i][j] == 0: # 안익은 토마토가 있는데 방문한적도 없다면
                    is_all_ripe = False
                else:
                    max_days = max(max_days, visited[u][i][j] - 1) # 가장 긴 거리를 선택

if is_all_ripe:
    print(max_days)
else:
    print(-1)