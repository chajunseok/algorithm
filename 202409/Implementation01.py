dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
da = ["L", "R", "U", "D"]


N = int(input())
move = list(map(str, input().split()))
s, e = 1, 1
idx = 0

for char in move:
    idx = da.index(char)
    nx, ny = s + dx[idx], e + dy[idx]
    if 0 < nx <= N and 0 < ny <= N:
        s = nx
        e = ny

print(e, s)