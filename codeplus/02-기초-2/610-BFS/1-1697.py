# 💡 숨바꼭질 @https://www.acmicpc.net/problem/1697
from collections import deque

MAX = 200000
check = [False]*(MAX+1)
dist = [-1]*(MAX+1)
n,m = map(int,input().split())
check[n] = True
dist[n] = 0
q = deque()
q.append(n)

while q:
  now = q.popleft()
  for nxt in [now-1, now+1, now*2]:
    if 0 <= nxt <= MAX and check[nxt] == False:
      check[nxt] = True
      dist[nxt] = dist[now] + 1
      q.append(nxt)

print(dist[m])