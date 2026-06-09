from bisect import bisect_right

N, X = map(int, input().split())
A = list(map(int, input().split()))

i = bisect_right(A, X)
print(i)