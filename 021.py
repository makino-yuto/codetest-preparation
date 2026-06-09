H, W = map(int, input().split())
ans = 0

grid = []

for _ in range(H):
    grid.append(input())

R, C = map(int, input().split())

R -= 1
C -= 1

if R + 1 < H and grid[R + 1][C] == "#":
    ans += 1

if C + 1 < W and grid[R][C + 1] == "#":
    ans += 1

if C - 1 >= 0 and grid[R][C - 1] == "#":
    ans += 1

if R - 1 >= 0 and grid[R - 1][C] == "#":
    ans += 1

print(ans)