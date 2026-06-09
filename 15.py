from bisect import bisect_right
from bisect import bisect_left

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

left = bisect_left(A, L)
right = bisect_right(A, R)

print(right - left)