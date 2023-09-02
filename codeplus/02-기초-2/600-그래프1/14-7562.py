# 💡 나이트의 이동 @https://www.acmicpc.net/problem/7562
from collections import deque

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]
t = int(input())

for _ in range(t):
  n = int(input())
  sx,sy = map(int,input().split())
  ex,ey = map(int,input().split())
  d = [[-1]*n for _ in range(n)]
  q = deque()
  q.append((sx,sy))
  d[sx][sy] = 0
  while q:
    x,y = q.popleft()
    for k in range(8):
      nx,ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0 <= ny < n:
        if d[nx][ny] == -1:
          d[nx][ny] = d[x][y] + 1
          q.append((nx,ny))
  print(d[ex][ey])