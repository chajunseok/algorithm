import heapq

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [float('inf')] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        current_dist, now = heapq.heappop(queue)

        if distance[now] < current_dist:
            continue

        for next_node in graph[now]:
            cost = current_dist + 1
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))


dijkstra(X)
result = [i for i in range(1, N + 1) if distance[i] == K]

if result:
    for node in result:
        print(node)
else:
    print(-1)
