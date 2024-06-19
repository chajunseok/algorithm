from collections import deque


def bfs():
    queue = deque()
    queue.append((0, 0, 0))  # (x, y, 벽을 부순 횟수)
    visited = [[[0] * 2 for _ in range(M)] for __ in range(N)]
    visited[0][0][0] = 1  # 시작 지점 초기화

    while queue:
        x, y, crush = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][crush]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if jido[nx][ny] == 0 and visited[nx][ny][crush] == 0:  # 평범한 경우 (벽 부순 횟수 0, 1)
                    visited[nx][ny][crush] = visited[x][y][crush] + 1
                    queue.append((nx, ny, crush))
                # 벽을 부수는 경우 (새로 부숴야하기 때문에, 벽 부순횟수가 0회 + 부순적 없는 벽)
                elif jido[nx][ny] == 1 and crush == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))

    return -1  # 목표 위치에 도달하지 못한 경우


N, M = map(int, input().split())
jido = [list(map(int, input().strip())) for _ in range(N)]

print(bfs())
