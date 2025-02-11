N, K = map(int, input().split())
line = list(map(str, input()))
cnt = 0

for i in range(N):
    if line[i] == 'H':
       for dx in range(i-K, i+K+1):
           if 0 <= dx < N and line[dx] == 'P':
               cnt += 1
               line[dx] = 'C'
               break

print(cnt)