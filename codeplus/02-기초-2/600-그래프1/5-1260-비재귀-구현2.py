# 💡 DFS와 BFS @https://www.acmicpc.net/problem/1260
from collections import deque

def dfs(n, a, node):
  check = [False] * (n+1)
  start = [0] * (n+1)
  stack = []
  stack.append(node)
  check[node] = True
  print(node, end=' ')
  while stack:
    node = stack.pop()
    while start[node] < len(a[node]):
      nxt = a[node][start[node]]
      if check[nxt] == False:
        print(nxt, end=' ')
        check[nxt] = True
        stack.append(node)
        stack.append(nxt)
        break
      start[node] += 1

def bfs(n, a, start):
  q = deque()
  check = [False] * (n+1)
  q.append(start)
  check[start] = True
  while q:
    x = q.popleft()
    print(x, end=' ')
    for y in a[x]:
      if check[y] == False:
        check[y] = True
        q.append(y)


n, m, start = map(int,input().split())
a = [[] for _ in range(n+1)]

for _ in range(m):
  u, v = map(int,input().split())
  a[u].append(v)
  a[v].append(u)
for i in range(1, n+1):
  a[i].sort()

dfs(n, a, start)
print()
bfs(n, a, start)
print()