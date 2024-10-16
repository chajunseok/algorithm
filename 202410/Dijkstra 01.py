import heapq

N, M, C = map(int, input().split())
INF = int(1e9)

graph = [[] for i in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(C)
cnt = 0
max_val = 0

for i in range(N+1):
    if distance[i] != 0 and distance[i] != INF:
        cnt += 1
        if max_val < distance[i]:
            max_val = distance[i]

print(cnt, max_val)