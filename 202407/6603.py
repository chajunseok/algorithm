import sys


def perm(k, num):
    if k == 6:
        result = []
        for idx in tmp:
            result.append(elements[idx])
        print(*result)
        return

    for i in range(num, count):
        tmp[k] = i
        perm(k+1, i+1)
        tmp[k] = 0


for line in sys.stdin:
    if line == '0':
        break
    numbers = list(map(int, line.split()))
    count = numbers[0]
    elements = numbers[1:1 + count]
    tmp = [0] * 6
    perm(0, 0)
    print(' ')

