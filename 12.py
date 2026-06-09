from bisect import bisect_left

N, X = map(int, input().split())
A = list(map(int, input().split()))

i = bisect_left(A, X)

if i < N and A[i] == X:
    print("Yes")
else:
    print("No")

# O(logN)