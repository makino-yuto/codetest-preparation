N = int(input())
A = list(map(int, input().split()))

B = set(A)

if len(A) == len(B):
    print("Yes")
else:
    print("No")