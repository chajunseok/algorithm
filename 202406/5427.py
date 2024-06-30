from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    # 불의 확산 queue
    while fire_queue:
        x, y = fire_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and building[nx][ny] == '.' and not fire_visited[nx][ny]:
                fire_visited[nx][ny] = fire_visited[x][y] + 1
                fire_queue.append((nx, ny))

    # 상근이 queue
    while sg_queue:
        x, y = sg_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if building[nx][ny] == '.' and not visited[nx][ny]:
                    # 불이 도달하지 않은 지역
                    if not fire_visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        sg_queue.append((nx, ny))

            # 구멍이 난 벽에 도착하면  return
            else:
                return visited[x][y] + 1
    return 'IMPOSSIBLE'


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    building = [list(input().strip()) for _ in range(h)]

    fire_queue = deque()
    sg_queue = deque()
    visited = [[0] * w for _ in range(h)]
    fire_visited = [[0] * w for _ in range(h)]

    for r in range(h):
        for c in range(w):
            if building[r][c] == '*':
                fire_queue.append((r, c))
                fire_visited[r][c] = 0
            elif building[r][c] == '@':
                sg_queue.append((r, c))
                visited[r][c] = 0

    print(bfs())
