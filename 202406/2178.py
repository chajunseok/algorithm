from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(): # 최소 거리를 구하는 문제 -> bfs
    while queue:
        cx, cy = queue.popleft()
        if cx == N-1 and cy == M-1:
            return visited[cx][cy]

        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1


N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
queue = deque()
visited = [[0] * M for _ in range(N)]
cnt = 0

queue.append((0, 0))
visited[0][0] = 1

print(bfs())