dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y):
    global cnt, visited

    stack = [(x, y)]
    visited[x][y] = 1

    while stack:
        cx, cy = stack.pop()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and section[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1


N = int(input())
section = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt_list = []

for i in range(N):
    for j in range(N):
        if section[i][j] and not visited[i][j]:
            cnt = 1
            move(i, j)
            cnt_list.append(cnt)


print(len(cnt_list))
for home in sorted(cnt_list):
    print(home)

