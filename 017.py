from collections import deque

Q = int(input())
que = deque()

for _ in range(Q):
    command = list(map(int, input().split()))

    if command[0] == 1:
        que.append(command[1])
    else:
        print(que.popleft())

# que.append(x)       末尾に追加
# que.appendleft(x)   先頭に追加
# que.pop()           末尾を返して削除
# que.popleft()       先頭を返して削除