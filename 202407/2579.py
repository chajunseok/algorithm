N = int(input())
stairs = [0]

for _ in range(N):
    stairs.append(int(input()))

dp = [0] * (N + 1)
dp[1] = stairs[1]

for i in range(2, N+1):
    dp[i] = stairs[i] + max(dp[i-3] + stairs[i-1], dp[i-2])

print(dp[N])
