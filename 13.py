from bisect import bisect_left

N, X = map(int, input().split())
A = list(map(int, input().split()))

i = bisect_left(A, X)

if i < N:
    print(A[i])
else:
    print(-1)