import heapq

T, C, Ts, Te = map(int, input().split())
graph = [[] for i in range(T+1)]
distance = [float('inf')] * (T+1)

for _ in range(C):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        current_dist, now = heapq.heappop(queue)

        if distance[now] < current_dist:
            continue

        for next_node, cost_value in graph[now]:
            cost = current_dist + cost_value
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))


dijkstra(Ts)
print(distance[Te])
