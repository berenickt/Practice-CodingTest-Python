# 💡 N과 M (7) @https://www.acmicpc.net/problem/15656
import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
c = [False]*n
a = [0]*m

def go(index, n, m):
  if index == m:
    sys.stdout.write(' '.join(map(str,a))+'\n')
    return
  for i in range(n):
    c[i] = True
    a[index] = num[i]
    go(index+1, n, m)
    c[i] = False

go(0,n,m)