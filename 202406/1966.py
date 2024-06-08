dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y, mapSection, visited, color):
    stack = [(x, y)]
    visited[x][y] = 1

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and mapSection[nx][ny] == color:
                stack.append((nx, ny))
                visited[nx][ny] = 1


def cnt_section(N, section_a):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                move(i, j, section_a, visited, section_a[i][j])
                cnt += 1
    return cnt


N = int(input())
section = [input() for _ in range(N)]
section_RG = [[''] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if section[i][j] == 'G':
            section_RG[i][j] = 'R'
        else:
            section_RG[i][j] = section[i][j]

print(cnt_section(N, section), cnt_section(N, section_RG))
