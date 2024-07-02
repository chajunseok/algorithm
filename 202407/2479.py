from collections import deque


def hamming_distance(code1, code2):
    # 두 이진 코드를 각각 비교하여 더해서 1이되면 출력
    return sum(c1 != c2 for c1, c2 in zip(code1, code2))


def find_hamming_path(codes, start, end):
    N = len(codes)

    # 해밍 거리가 1인 코드들 사이의 인접 리스트를 생성
    adj_list = {i: [] for i in range(N)}
    for i in range(N):
        for j in range(i + 1, N):
            if hamming_distance(codes[i], codes[j]) == 1:
                adj_list[i].append(j)
                adj_list[j].append(i)

    # BFS를 사용하여 최단 경로를 찾음
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == end:
            # 다시 1을 더해서 출력해줌(0부터 시작한 배열이였으니깐)
            return [p + 1 for p in path]

        for neighbor in adj_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return -1


# 입력 받기
N, K = map(int, input().split())
codes = [input().strip() for _ in range(N)]
start, end = map(int, input().split())

# 배열 0부터 시작
start -= 1
end -= 1

# 해밍 경로 찾기
result = find_hamming_path(codes, start, end)

# 결과 출력
if result == -1:
    print(result)
else:
    print(' '.join(map(str, result)))
