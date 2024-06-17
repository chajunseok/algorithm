from collections import deque


def bfs():  # 최단거리 구하자 -> 무지성 bfs
    global result
    queue = deque([N])  # 1차원 bfs?
    visited[N] = 0

    while queue:
        sx = queue.popleft()
        if sx == K:  # 도착시 return
            result = visited[sx]
            return
        next_positions = [sx - 1, sx + 1, sx * 2]  # -1 ,+1 ,x2 의 경우 자식노드

        for nx in next_positions: # 노드 순회
            if 0 <= nx <= max_distance and not visited[nx]:  # 최대거리 안에 있고 방문처리가 안되있다면
                visited[nx] = visited[sx] + 1  # 방문처리는 부모노드 거리의 +1
                queue.append(nx)


N, K = map(int, input().split())
max_distance = 100000
visited = [0] * 100001
result = 0

bfs()
print(result)
