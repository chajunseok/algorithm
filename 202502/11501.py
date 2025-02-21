T = int(input())
for _ in range(T):
    N = int(input())
    stock_list = list(map(int, input().split()))

    max_price = 0
    profit = 0
    for i in range(N - 1, -1, -1):
        if stock_list[i] > max_price:
            max_price = stock_list[i]
        else:
            profit += max_price - stock_list[i]

    print(profit)
