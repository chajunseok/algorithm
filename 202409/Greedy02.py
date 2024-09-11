S = input()
result = 0

for i in range(len(S)):
    if result == 0:
        result += int(S[i])

    else:
        if S[i]:
            result *= int(S[i])

        else:
            result += int(S[i])

print(result)