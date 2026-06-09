N, Q = map(int, input().split())
A = list(map(int, input().split()))

preans = [0] * (N + 1)

for i in range(N):
    preans[i + 1] = preans[i] + A[i]
    
for _ in range(Q):
    L, R = map(int, input().split())
    print(preans[R] - preans[L - 1])