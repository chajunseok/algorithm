# N과 M (2)

N, M = map(int, input().split())
tmp = [0] * M


def perm(k, num):
    if k == M:
        print(*tmp)
        return

    for i in range(num, N+1):
        if i not in tmp:
            tmp[k] = i
            perm(k+1, i)
            tmp[k] = 0


perm(0, 0)