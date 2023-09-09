# 💡 다리 만들기 📚 https://www.acmicpc.net/problem/2146
from collections import deque

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
g = [[0] * n for _ in range(n)]
d = [[0] * n for _ in range(n)]
cnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and g[i][j] == 0:
            cnt += 1
            g[i][j] = cnt
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny] == 1 and g[nx][ny] == 0:
                            g[nx][ny] = cnt
                            q.append((nx, ny))

q = deque()
for i in range(n):
    for j in range(n):
        d[i][j] = -1
        if a[i][j] == 1:
            q.append((i, j))
            d[i][j] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                g[nx][ny] = g[x][y]
                q.append((nx, ny))

ans = -1

for i in range(n):
    for j in range(n):
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < n and 0 <= y < n:
                if g[i][j] != g[x][y]:
                    if ans == -1 or ans > d[i][j] + d[x][y]:
                        ans = d[i][j] + d[x][y]

print(ans)
