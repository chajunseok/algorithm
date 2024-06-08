# N과 M (7)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# 정렬
sort_numbers = sorted(numbers)
tmp = [0] * M
result = []


def perm(k, num):
    if k == M:
        result.append(tuple(tmp))
        return

    # 중복 가능, 이전 idx 가능
    for i in range(num, N):
        # 순열 생성
        tmp[k] = sort_numbers[i]
        perm(k + 1, i+1)
        tmp[k] = 0


perm(0, 0)

for perm in sorted(set(result)):
    print(' '.join(map(str, perm)))