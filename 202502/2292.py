N = int(input())
an = [0] * 50000
an[0] = 1

if N == 1:
    print(1)

else:
    for i in range(1, 50000):
        an[i] = 3 * i * (i+1) + 1
        if an[i-1] < N <= an[i]:
            print(i+1)
            break




