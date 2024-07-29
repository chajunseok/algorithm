n = int(input())
tmp1, tmp2 = 0, 1
for i in range(n):
    tmp1, tmp2 = tmp2 % 15746, (tmp1 + tmp2) % 15746
print(tmp2)