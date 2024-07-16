import heapq

N, M = map(int, input().split())
invisible = list(map(int, input().split()))
graph = [[] for _ in range(N)]
distance = [float('inf')] * N

invisible.pop()
invisible.append(0)

for _ in range(M):
    u, v, c = map(int, input().split())
    if not invisible[u] and not invisible[v]:
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


dijkstra(0)

if distance[N-1] == float('inf'):
    print(-1)
else:
    print(distance[N-1])