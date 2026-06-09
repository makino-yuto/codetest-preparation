N, K = map(int, input().split())
A = list(map(int, input().split()))

B = sorted(set(A), reverse=True)

print(sum(B[:K]))