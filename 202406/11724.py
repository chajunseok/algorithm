import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(k):
    visited[k] = 1
    for j in graph[k]:
        if not visited[j]:
            dfs(j)


count = 0
visited = [0] * (N+1)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)