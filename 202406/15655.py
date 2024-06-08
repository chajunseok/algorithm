# N과 M (6)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# 정렬
sort_numbers = sorted(numbers)
tmp = [0] * M


def perm(k, num):
    if k == M:
        print(*tmp)
        return

    # 다시 이전 idx 가 나오므로 num 값 저장한 곳 부터 시작함
    for i in range(num, N):
        # sort_numbers[i]가 없을 때 -> 중복 제거
        if sort_numbers[i] not in tmp:
            # 순열 생성
            tmp[k] = sort_numbers[i]
            perm(k + 1, i)
            tmp[k] = 0


perm(0, 0)