# 💡 요세푸스 문제 @https://www.acmicpc.net/problem/1158
#!/usr/bin/python3
from collections import deque
n, m = map(int,input().split())
q = deque()

for i in range(1, n+1):
  q.append(i)
ans = []

for i in range(n-1):
  for j in range(m-1):
    q.append(q.popleft())
  ans += [q.popleft()]

ans += [q[0]]
print('<' + ', '.join(map(str,ans)) + '>')