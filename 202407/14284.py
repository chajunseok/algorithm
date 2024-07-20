import heapq

N, M = map(int, input().split())
graph = [[] for i in range(5001)]
distance = [float('inf')] * 5001

for i in range(5000):
    graph[i].append((i+1, 1))


input_list = []
for _ in range(M):
    u, v, c = map(int, input().split())
    input_list.append((u, v, c))

st, se = map(int, input().split())

check = True
for start, end, cost in input_list:
    if check:
        u, v, c = start, end, cost
        graph[u].append((v, c))
        graph[v].append((u, c))


        def dijkstra(start):
            global check
            queue = []
            heapq.heappush(queue, (0, start))
            distance[start] = 0

            while queue:
                current_dist, now = heapq.heappop(queue)
                if now == se:
                    check = False
                    return

                if distance[now] < current_dist:
                    continue

                for next_node, cost_value in graph[now]:
                    cost = current_dist + cost_value
                    if cost < distance[next_node]:
                        distance[next_node] = cost
                        heapq.heappush(queue, (cost, next_node))

        dijkstra(st)

print(distance[se])