import heapq

N, D = map(int, input().split())
graph = [[] for i in range(10001)]
distance = [float('inf')] * 10001

for i in range(10000):
    graph[i].append((i+1, 1))

for _ in range(N):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))


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


dijkstra(0)
print(distance[D])
