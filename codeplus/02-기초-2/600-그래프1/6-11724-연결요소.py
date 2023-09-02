# 💡 연결 요소 @https://www.acmicpc.net/problem/11724
import sys

sys.setrecursionlimit(100000)
n,m = map(int,input().split())
a = [[] for _ in range(n)]
check = [False] * (n)

for _ in range(m):
  u,v = map(int,input().split())
  a[u-1].append(v-1)
  a[v-1].append(u-1)

def dfs(x):
  check[x] = True
  for y in a[x]:
    if check[y] == False:
      dfs(y)

ans = 0
for i in range(n):
  if not check[i]:
    dfs(i)
    ans += 1
print(ans)