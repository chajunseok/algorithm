dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):  # 늘 먹던 맛
    stack = [(x, y)]
    visited[x][y] = 1
    section = 1

    while stack:
        cx, cy = stack.pop()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and not jido[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = 1
                section += 1

    section_lst.append(section)


M, N, K = map(int, input().split())
jido = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
cnt = 0
section_lst = []


# 입력 좌표를 기준으로 영역이 겹치는 부분을 jido에 표기
for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            if 0 <= i < M and 0 <= j < N: # runtime error 방지
                jido[i][j] = 1

for i in range(M):
    for j in range(N):
        if jido[i][j] == 0 and not visited[i][j]:  # dfs 의 시작점 설정
            dfs(i, j)
            cnt += 1  # 찾았을 경우, cnt += 1

print(cnt)
print(' '.join(map(str, sorted(section_lst))))
