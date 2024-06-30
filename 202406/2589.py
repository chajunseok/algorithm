from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y): # 최소 거리를 구하는 문제 -> bfs
    global max_value

    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 'L' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1
                max_value = max(max_value, visited[nx][ny])  # bfs -> 항상 최단거리로 이동 -> 돌리면서 최장거리 나오면 갱신


N, M = map(int, input().split())
field = [list(map(str, input()))for _ in range(N)]
queue = deque()
max_value = 0

for i in range(N):
    for j in range(M):
        visited = [[0] * M for _ in range(N)]
        if field[i][j] == 'L' and not visited[i][j]:
            bfs(i, j)

print(max_value-1)  # 거리를 구하는거니까 -1 하자