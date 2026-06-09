N = int(input())
A = list(map(int, input().split()))

ans = set()
seen = set()


for i in A:
    if i in seen:
        ans.add(i)
    else:
        seen.add(i)

print(*sorted(ans))
