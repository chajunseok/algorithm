# N과 M (9)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 정렬
sorted_numbers = sorted(numbers)
result = []


def perm(current_perm, used):
    # tuple로 변환하여 리스트에 저장
    if len(current_perm) == M:
        result.append(tuple(current_perm))
        return

    # 이전 숫자를 추적하여 중복된 숫자의 처리를 스킵
    prev = None
    for i in range(N):
        if not used[i] and (prev is None or prev != sorted_numbers[i]):
            used[i] = True
            current_perm.append(sorted_numbers[i])
            perm(current_perm, used)
            current_perm.pop()
            used[i] = False
            # 이전 숫자 업데이트
            prev = sorted_numbers[i]


perm([], [False] * N)

# 중복된 결과 제거를 위해 set 사용 후 정렬된 순서대로 출력
for perm in sorted(set(result)):
    print(' '.join(map(str, perm)))