import heapq

N, K = map(int, input().split())
graph = [[] for _ in range(100001)]
distance = [float('inf')] * 100001

graph[0].append((1, 1))
graph[100000].append((99999, 1))
for i in range(1, 100000):
    graph[i].append((i+1, 1))
    graph[i].append((i-1, 1))
    if i <= 50000:
        graph[i].append((2*i, 0))


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


dijkstra(N)
print(distance[K])