N, K = map(int, input().split())
A = list(map(int, input().split()))

B = sorted(A, reverse=True)

print(sum(B[:K]))
# NlogN
# 2 7
# 3 6 3 5 7 4 6 7 4 5 6 1 7 9 4 5
# 48