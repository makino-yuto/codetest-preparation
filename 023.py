N = int(input())
A = list(map(int, input().split()))

count = {}

for i in A:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

ans_key = None
ans_value = -1

for key, value in count.items():
    if ans_value < value:
        ans_value = value
        ans_key = key
    elif ans_value == value and ans_key > key:
        ans_key = key

print(ans_key)