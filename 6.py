N, K = map(int, input().split())
A = list(map(int, input().split()))

A = set(A)

B = sorted(A, reverse=True)

print(*B[:K])

# * でlistを展開可能
# print(*B[:K])なら
# [9, 7, 6, 5, 4, 3, 1]
# print(B[:K]) なら
# 9 7 6 5 4 3 1