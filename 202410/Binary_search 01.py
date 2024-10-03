N, M = map(int, input().split())
rice_cake = list(map(int, input().split()))

start = 0
end = max(rice_cake)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in rice_cake:
        if x > mid:
            total += x - mid

    if total < M:
        end = mid + 1

    else:
        result = mid
        start = mid + 1

print(result)

# 이진탐색은 꼭 배열의 절반씩 탐색할 필요가 없다.
