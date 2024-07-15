from math import inf

INF = inf
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [INF] * (N+1)

for _ in range(M):
    bus_start, bus_end, c = map(int, input().split())
    graph[bus_start].append((bus_end, c))

start_point, end_point = map(int, input().split())


def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i

    return idx


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i, j in graph[start]:
        if distance[i] >= j:
            distance[i] = j

    for _ in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        for next_node, weight in graph[now]:
            cost = distance[now] + weight
            if cost < distance[next_node]:
                distance[next_node] = cost


dijkstra(start_point)

print(distance[end_point])

