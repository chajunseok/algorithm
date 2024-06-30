from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# DFS를 사용하여 섬을 라벨링
def dfs(x, y, land_id):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and jido[nx][ny] == 1:
                visited[nx][ny] = True
                new_jido[nx][ny] = land_id
                stack.append((nx, ny))


# BFS를 사용하여 최단 다리 길이 찾기
def bfs(z):
    global min_val
    queue = deque()
    dist = [[-1] * N for _ in range(N)]

    # 섬 1개씩 최단 거리 찾기
    for r in range(N):
        for c in range(N):
            if new_jido[r][c] == z:
                queue.append((r, c))
                dist[r][c] = 0

    # BFS 탐색
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
                # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if new_jido[nx][ny] > 0 and new_jido[nx][ny] != z:
                min_val = min(min_val, dist[cx][cy])
                return
                # 바다를 만나면 dist를 1씩 늘린다.
            if new_jido[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[cx][cy] + 1
                queue.append((nx, ny))


N = int(input())
jido = [list(map(int, input().split())) for _ in range(N)]
new_jido = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
land_id = 0

# 각 섬에 고유 번호 부여
for r in range(N):
    for c in range(N):
        if jido[r][c] == 1 and not visited[r][c]:
            land_id += 1
            visited[r][c] = True
            new_jido[r][c] = land_id
            dfs(r, c, land_id)

min_val = 10000
# 섬 1개씩 bfs
for i in range(1, land_id):
    bfs(i)

print(min_val)
