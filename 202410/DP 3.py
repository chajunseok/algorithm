N, M = map(int, input().split())
currencies = [int(input()) for _ in range(N)]
d = [10000] * (M + 1)
d[0] = 0

for i in range(1, M + 1):
    for currency in currencies:
        if i >= currency:
            d[i] = min(d[i], d[i - currency] + 1)

if d[M] == 10000:
    print(-1)
else:
    print(d[M])
