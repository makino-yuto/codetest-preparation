from bisect import bisect_left
from bisect import bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
    X = int(input())
    i = bisect_right(A, X)
    if i >= len(A):
        print(-1)
    else:
        print(A[i])