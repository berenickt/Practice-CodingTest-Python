# 💡 1, 2, 3 더하기 3 @https://www.acmicpc.net/problem/15988
d = [0]*1000001
mod = 1000000009
d[0] = 1
for i in range(1, 1000000+1):
  if i-1 >= 0:
    d[i] += d[i-1]
  if i-2 >= 0:
    d[i] += d[i-2]
  if i-3 >= 0:
    d[i] += d[i-3]
  d[i] %= mod

t = int(input())
for _ in range(t):
  n = int(input())
  print(d[n])