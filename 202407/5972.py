import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(50001)]
distance = [float('inf')] * 50001

for _ in range(M):
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

        for next_node, cost_val in graph[now]:
            cost = current_dist + cost_val
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))


dijkstra(1)
print((distance[N]))