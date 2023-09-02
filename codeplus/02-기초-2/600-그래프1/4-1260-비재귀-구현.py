# 💡 DFS와 BFS @https://www.acmicpc.net/problem/1260
from collections import deque

n,m,start = map(int,input().split())
a = [[] for _ in range(n+1)]

for _ in range(m):
  u,v = map(int,input().split())
  a[u].append(v)
  a[v].append(u)

for i in range(1, n+1):
  a[i].sort()

def dfs(node):
  check = [False] * (n+1)
  stack = []
  stack.append((node,0))
  check[node] = True
  print(node, end=' ')
  while stack:
    x,start = stack.pop()
    for i in range(start, len(a[x])):
      y = a[x][i]
      if check[y] == False:
        print(y, end=' ')
        check[y] = True
        stack.append((x,i+1))
        stack.append((y,0))
        break

def bfs(start):
  check = [False] * (n+1)
  q = deque()
  q.append(start)
  check[start] = True
  while q:
    x = q.popleft()
    print(x, end=' ')
    for y in a[x]:
      if check[y] == False:
        check[y] = True
        q.append(y)

dfs(start)
print()
bfs(start)
print()