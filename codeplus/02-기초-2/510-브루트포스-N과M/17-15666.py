# 💡 N과 M (12) @https://www.acmicpc.net/problem/15666
import sys
n,m = map(int,input().split())
c = [False] * (n+1)
num = list(map(int,input().split()))
num = sorted(list(set(num)))
n = len(num)
a = [0]*m

def go(index, start, n, m):
  if index == m:
    for i in range(m):
      sys.stdout.write(str(num[a[i]])+' ')
    sys.stdout.write('\n')
    return
  for i in range(start, n):
    c[i] = True
    a[index] = i
    go(index+1, i, n, m)
    c[i] = False

go(0,0,n,m)