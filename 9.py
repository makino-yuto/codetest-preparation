N, Q = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
    L, R = map(int, input().split())
    B = A[L-1:R]
    print(sum(B))

# 遅い
# 10.pyにて高速化