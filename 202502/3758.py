T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    # n = 팀의 갯수, k = 문제의 갯수, t = 팀 id, m = 제출 횟수
    total_score = [[num+1, 0, 0, 0] for num in range(n)] # (팀 번호, 점수, 제출 횟수, 마지막 제출 idx)
    score = [[0] * k for _ in range(n)]
    for index in range(m):
        i, j, s = map(int, input().split()) # i = 팀 id, j = 문제 번호, s = 점수
        tmp = score[i-1][j-1]
        score[i-1][j-1] = max(score[i-1][j-1], s)
        total_score[i-1][1] += score[i-1][j-1] - tmp
        total_score[i-1][2] += 1
        total_score[i-1][3] = index + 1

    total_score.sort(key= lambda x : (-x[1], x[2], x[3]))
    for i in range(n):
        if total_score[i][0] == t:
            print(i+1)