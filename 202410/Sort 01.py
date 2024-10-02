N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

while K > 0:
    min_val = min(A)
    max_val = max(B)

    if min_val < max_val:
        A[A.index(min_val)], B[B.index(max_val)] = B[B.index(max_val)], A[A.index(min_val)]
        K -= 1

    else:
        break

print(sum(A))