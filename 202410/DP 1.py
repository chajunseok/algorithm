N = int(input())
food = list(map(int, input().split()))

d = [0] * (N+1)


def DP(x):
    if x == 1 or x == 2 or x == 0:
        return food[x-1]

    if d[x] != 0:
        return d[x]

    d[x] = max(DP(x-2), DP(x-3)) + food[x-1]
    print(d)
    return d[x]

DP(N)
DP(N-1)

print(max(d))