from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
arr = list(map(int, input().split()))

result = bisect_right(arr, x) - bisect_left(arr, x)

print(result)

start = 0
end = N - 1
result1 = 0
result2 = 0

while start <= end:
    mid = (start+end) // 2

    if arr[mid] > x:
        end = mid - 1

    else:
        result1 = mid - 1
        start = mid + 1

start = 0
end = N - 1

while start <= end:
    mid = (start + end) // 2

    if arr[mid] >= x:
        result2 = mid + 1
        end = mid - 1

    else:
        start = mid + 1

print(result2)
print(result1)
print(result1 - result2)