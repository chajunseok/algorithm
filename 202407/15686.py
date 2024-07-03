import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 최소 거리 찾는 함수
def found_distance(x, y, val_list):
    min_distance = 10000000
    # 치킨 집 순열 순회
    for (cx, cy) in val_list:
        distance = abs(x - cx) + abs(y - cy)
        # 같은 집에서 더 작은 거리가 있을 경우 바꾸기
        if distance < min_distance:
            min_distance = distance
    return min_distance


# 순열 구하는 함수
def perm(k, num):
    global min_val
    if k == M:
        val_list = [chicken[idx] for idx in chicken_list[:M]]

        chicken_len = 0
        # 집 좌표를 순회
        for (si, sj) in house:
            # 더해주기
            chicken_len += found_distance(si, sj, val_list)

        # 각각 순열마다 최소값 갱신해주기
        min_val = min(min_val, chicken_len)
        return

    for i in range(num, len(chicken)):
        chicken_list[k] = i
        perm(k + 1, i + 1)
        chicken_list[k] = -1


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
for r in range(N):
    for c in range(N):
        if city[r][c] == 2:
            chicken.append((r, c))
        elif city[r][c] == 1:
            house.append((r, c))

chicken_list = [-1] * M
min_val = 1000000
perm(0, 0)

print(min_val)
