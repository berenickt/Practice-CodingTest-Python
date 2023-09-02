# 💡 BFS 스페셜 저지 @https://www.acmicpc.net/problem/16940
from collections import deque

n = int(input())
a = [[] for _ in range(n)]

for _ in range(n-1):
  u, v = map(int,input().split())
  u -= 1
  v -= 1
  a[u].append(v)
  a[v].append(u)

b = list(map(int,input().split()))
b = [x-1 for x in b]
order = [0]*n

for i in range(n):
  order[b[i]] = i

for i in range(n):
  a[i].sort(key=lambda x: order[x])

bfs_order = []
q = deque()
check = [False]*n
q.append(0)
check[0] = True

while q:
  x = q.popleft()
  bfs_order.append(x)
  for y in a[x]:
    if check[y] == False:
      check[y] = True
      q.append(y)

ok = True

for i in range(n):
  if bfs_order[i] != b[i]: ok = False

print(1 if ok else 0)