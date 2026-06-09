N, X = map(int, input().split())
A = list(map(int, input().split()))

seen = set()
ans = "No"

for i in A:
    a = X - i
    
    if a in seen:
        ans = "Yes"
        break

    seen.add(i)

print(ans)