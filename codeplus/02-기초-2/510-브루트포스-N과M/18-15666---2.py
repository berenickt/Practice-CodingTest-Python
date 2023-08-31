# 💡 N과 M (12) @https://www.acmicpc.net/problem/15666
import sys

n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
c = [False]*n
a = [0]*m
d = []

def go(index, start, n, m):
  if index == m:
    d.append(tuple(a))
    return
  for i in range(start, n):
    c[i] = True
    a[index] = num[i]
    go(index+1, i, n, m)
    c[i] = False

go(0,0,n,m)
d = sorted(list(set(d)))

for v in d:
  sys.stdout.write(' '.join(map(str,v))+'\n')