# N과 M (1)

N, M = map(int, input().split())
tmp = [0] * M


def perm(k):
    if k == M:
        print(*tmp)
        return

    for i in range(1, N + 1):
        if i not in tmp:
            tmp[k] = i
            perm(k+1)
            tmp[k] = 0


perm(0)