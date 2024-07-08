import sys


def perm(player, current_sum, used):
    if player == 11:
        return current_sum
    max_sum = 0
    for position in range(11):
        if not used[position] and abilities[player][position] > 0:
            used[position] = 1
            max_sum = max(max_sum, perm(player + 1, current_sum + abilities[player][position], used))
            used[position] = 0
    return max_sum


input = sys.stdin.read
data = input().split()

index = 0
C = int(data[index])
index += 1

results = []

for _ in range(C):
    abilities = []
    for _ in range(11):
        abilities.append(list(map(int, data[index:index + 11])))
        index += 11
    used = [0] * 11
    max_sum = perm(0, 0, used)
    results.append(max_sum)

for result in results:
    print(result)