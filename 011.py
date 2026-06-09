N, X  = map(int, input().split())
A = list(map(int, input().split()))

ans = "No"

for i in A:
    if i == X:
        ans = "Yes"
        break

print(ans)

# O(N)
# 12.pyでO(logN)に改善