N = int(input())
A = list(map(int, input().split()))

B = sorted(A, reverse=True)

print(*B)
# 出力
# 6
# 3 5 4 2 4 6
# 6 5 4 4 3 2