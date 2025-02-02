while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    num_list = sorted([a, b, c])
    if num_list[0] + num_list[1] <= num_list[2]:
        print("Invalid")
        continue

    elif len(set(num_list)) == 3:
        print("Scalene")

    elif len(set(num_list)) == 2:
        print("Isosceles")

    else:
        print("Equilateral")

