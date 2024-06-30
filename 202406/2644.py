from collections import deque


def bfs():
    queue = deque([p1])
    visited[p1] = 0

    while queue:
        now = queue.popleft()
        # 관계들을 순회
        for next in relation[now]:
            # 일치하는 관계 발견시 촌수 + 1해서 출력
            if next == p2:
                return visited[now] + 1

            # 일치하지 않으면 que에 저장
            elif visited[next] == -1:
                visited[next] = visited[now] + 1
                queue.append(next)

    # 다 순회했는데 관계가 성립이 되지 않으면 -1
    return -1


N = int(input())
p1, p2 = map(int, input().split())
M = int(input())
relation = [[] for _ in range(N + 1)]

# 양방향 트리
for k in range(M):
    parent, child = map(int, input().split())
    relation[parent].append(child)
    relation[child].append(parent)

# 촌수 거리를 계산 해야하므로 방문처리 리스트 생성
visited = [-1] * (N + 1)
print(bfs())



