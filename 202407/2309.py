noye = [int(input()) for _ in range(9)]


def find_dwarfs(noye):
    total_sum = sum(noye)
    found = False

    for i in range(9):
        for j in range(i + 1, 9):
            if total_sum - noye[i] - noye[j] == 100:
                dwarfs = [noye[k] for k in range(9) if k != i and k != j]
                dwarfs.sort()
                for dwarf in dwarfs:
                    print(dwarf)
                found = True
                break
        if found:
            break


find_dwarfs(noye)
