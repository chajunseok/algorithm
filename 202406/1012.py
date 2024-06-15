dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, visited, bat, N, M): # dfs
    stack = [(x, y)]
    visited[x][y] = 1

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and bat[nx][ny]: # 조건문
                stack.append((nx, ny))
                visited[nx][ny] = 1


for tc in range(int(input())):
    M, N, K = map(int, input().split())
    bat = [[0] * M for _ in range(N)]

    for _ in range(K): # 배추 설정
        ax, ay = map(int, input().split())
        bat[ay][ax] = 1

    visited = [[0] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if bat[i][j] and not visited[i][j]:
                move(i, j, visited, bat, N, M)
                cnt += 1

    print(cnt)
