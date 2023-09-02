# 💡 이분 그래프 @https://www.acmicpc.net/problem/1707
import sys
sys.setrecursionlimit(1000000)
t = int(sys.stdin.readline())

for _ in range(t):
  n,m = map(int,sys.stdin.readline().split())
  a = [[] for _ in range(n)]
  color = [0] * n
  for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    a[u-1].append(v-1)
    a[v-1].append(u-1)

  def dfs(x, c):
    color[x] = c
    for y in a[x]:
      if color[y] == 0:
        dfs(y, 3-c)

  ans = True
  for i in range(n):
    if color[i] == 0:
        dfs(i, 1)
  for i in range(n):
    for j in a[i]:
      if color[i] == color[j]:
        ans = False
  print('YES' if ans else 'NO')