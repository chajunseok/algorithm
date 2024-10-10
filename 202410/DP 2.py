X = int(input())
d = [0] * (X+1)


def DP(x):
    if x == 1:
        return 0

    if d[x] != 0:
        return d[x]

    d[x] = DP(x - 1) + 1

    if x % 5 == 0:
        d[x] = min(d[x], DP(x // 5) + 1)

    if x % 3 == 0:
        d[x] = min(d[x], DP(x // 3) + 1)

    if x % 2 == 0:
        d[x] = min(d[x], DP(x // 2) + 1)

    return d[x]

print(DP(X))
