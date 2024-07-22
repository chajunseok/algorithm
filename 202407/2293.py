# n, goal = map(int, input().split())
#
# coin = []
# for _ in range(n):
#     coin.append(int(input()))
#
# sort_coins = sorted(coin)
# cnt = 0
#
#
# def find(k, current_sum):
#     global cnt
#     if current_sum == goal:
#         cnt += 1
#         return
#     if k == n or current_sum > goal:
#         return
#
#     max_cnt = (goal - current_sum) // sort_coins[k]
#
#     for i in range(max_cnt + 1):
#         find(k + 1, current_sum + sort_coins[k] * i)
#
#
# find(0, 0)
# print(cnt)

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i - coin]
print(dp[k])