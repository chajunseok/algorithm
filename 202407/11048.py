from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
cost = [[-1] * M for _ in range(N)]
queue.append((0, 0))
cost[0][0] = miro[0][0]

while queue:
    cx, cy = queue.popleft()

    if cx == M - 1 and cy == N - 1:
        break

    for dx, dy in [[1, 0], [0, 1], [1, 1]]:
        nx = cx + dx
        ny = cy + dy

        if 0 <= nx < M and 0 <= ny < N and cost[cy][cx] + miro[ny][nx] > cost[ny][nx]:
            queue.append((nx, ny))
            cost[ny][nx] = cost[cy][cx] + miro[ny][nx]

print(cost[N-1][M-1])
