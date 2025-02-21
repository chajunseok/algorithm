N = int(input())
pillars = []

# 기둥 입력
for _ in range(N):
    L, H = map(int, input().split())
    pillars.append((L, H))

# x좌표 기준 정렬
pillars.sort()

# 가장 높은 기둥 찾기
max_height = 0
max_idx = 0
for i in range(N):
    if pillars[i][1] > max_height:
        max_height = pillars[i][1]
        max_idx = i

answer = 0

# 왼쪽에서 오른쪽으로 증가하는 부분
left = pillars[0]
for i in range(max_idx + 1):
    if pillars[i][1] > left[1]:  # 이전 기둥보다 더 높은 기둥을 만나면 넓이 추가
        answer += (pillars[i][0] - left[0]) * left[1]
        left = pillars[i]

# 오른쪽에서 왼쪽으로 감소하는 부분
right = pillars[-1]
for i in range(N - 1, max_idx - 1, -1):
    if pillars[i][1] > right[1]:  # 이전 기둥보다 더 높은 기둥을 만나면 넓이 추가
        answer += (right[0] - pillars[i][0]) * right[1]
        right = pillars[i]

# 가장 높은 기둥들의 면적 추가
answer += max_height * (right[0] - left[0] + 1)

print(answer)
