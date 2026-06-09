N, L, R = map(int, input().split())

A = list(map(int, input().split()))

B = A[L-1:R]

ans = 0

for i in B:
    ans += i

print(ans)