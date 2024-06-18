from collections import deque


def bfs(p):  # 최소 거리 구해야됨 -> bfs
    queue = deque([p])
    visited = [0] * (N + 1)
    visited[p] = 1
    distances = [0] * (N + 1)

    while queue:
        item = queue.popleft()
        for nx in relation[item]:
            if not visited[nx]:
                visited[nx] = 1
                distances[nx] = distances[item] + 1
                queue.append(nx)

    max_distance = max(distances)
    winner[p] = max_distance # 가장 먼 거리가 곧 후보의 점수가됨


N = int(input())
relation = [[] for _ in range(N+1)]

while True:
    sx, sy = map(int, input().split())
    if sx == -1:
        break
    relation[sx].append(sy)
    relation[sy].append(sx)  # 양방향 그래프

winner = [0] * (N + 1)

for idx in range(1, N+1):
    bfs(idx)

min_val = min(winner[1:])
min_idx = []
for idx, i in enumerate(winner):
    if i == min_val:
        min_idx.append(str(idx))

print(min_val, len(min_idx))
print(' '.join(map(str, min_idx)))
