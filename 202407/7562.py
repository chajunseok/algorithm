from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]


def bfs(x, y):
    global end_position_x, end_position_y
    queue = deque()
    queue.append((x, y))
    visited = [[-1] * N for _ in range(N)]
    visited[x][y] = 0

    while queue:
        sx, sy = queue.popleft()

        if sx == end_position_x and sy == end_position_y:
            return visited[sx][sy]

        for k in range(8):
            nx, ny = sx + dx[k], sy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[sx][sy] + 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    start_position_x, start_position_y = map(int, input().split())
    end_position_x, end_position_y = map(int, input().split())

    if start_position_x == end_position_x and start_position_y == end_position_y:
        print(0)
        continue

    print(bfs(start_position_x, start_position_y))
