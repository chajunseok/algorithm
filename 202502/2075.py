import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    values = list(map(int, sys.stdin.readline().split()))
    for value in values:
        if len(heap) < N:
            heapq.heappush(heap, value)
        else:
            if heap[0] < value:
                heapq.heappushpop(heap, value)

print(heap[0])
