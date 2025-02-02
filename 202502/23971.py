# from collections import deque
#
# H, W, N, M = map(int, input().split())
# visited = set()
#
#
# def ZOAC():
#     cnt = 1
#     queue = deque([(0, 0)])
#     visited.add((0, 0))
#
#     while queue:
#         x, y = queue.popleft()
#
#         nx, ny = x + N + 1, y
#         if nx < H and (nx, ny) not in visited:
#             queue.append((nx, ny))
#             visited.add((nx, ny))
#             cnt += 1
#
#         nx, ny = x, y + M + 1
#         if ny < W and (nx, ny) not in visited:
#             queue.append((nx, ny))
#             visited.add((nx, ny))
#             cnt += 1
#
#     return cnt
#
# print(ZOAC())

import math

H, W, N, M = map(int, input().split())

row_num = math.ceil(H / (N + 1))
col_num = math.ceil(W / (M + 1))

print(row_num * col_num)