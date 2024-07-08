dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y, char):
    if len(char) == 6:
        if char not in num_list:
            num_list.add(char)
    else:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5:
                move(nx, ny, char+numbers[nx][ny])


numbers = [list(map(str, input().split()))for _ in range(5)]
num_list = set()

for r in range(5):
    for c in range(5):
        move(r, c, '')


print(len(num_list))