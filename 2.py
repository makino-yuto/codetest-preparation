N, X = map(int, input().split())

A = list(map(int, input().split()))

count = 0

for i in A:
    if i == X:
        count += 1

print(count)