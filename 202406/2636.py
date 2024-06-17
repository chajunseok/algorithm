from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if dish[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                elif dish[nx][ny] == 1:
                    # 치즈 녹이기 아직 녹으면 안돼 2로 표시
                    dish[nx][ny] = 2


def melt_cheese():
    count = 0
    for i in range(N):
        for j in range(M):
            if dish[i][j] == 2:
                dish[i][j] = 0  # 녹은 치즈는 공기가 됨
                count += 1
    return count  # 한바퀴 돌리고 녹이기


N, M = map(int, input().split())
dish = [list(map(int, input().split())) for _ in range(N)]
time = 0
last_cheese = 0

while True:
    bfs()
    new_count = melt_cheese()
    if new_count == 0:
        break
    last_cheese = new_count
    time += 1

print(time)
print(last_cheese)
