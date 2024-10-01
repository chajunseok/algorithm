from collections import deque


def bfs(graph, r, c, visited):
    global cnt

    queue = deque([(r, c)])
    visited[r][c] = 1

    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and graph[ny][nx] == 1:
                queue.append((ny, nx))
                visited[ny][nx] = visited[cy][cx] + 1


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
bfs(maze, 0, 0, visited)

print(visited[N-1][M-1])