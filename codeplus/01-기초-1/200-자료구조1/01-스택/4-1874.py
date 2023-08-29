# 💡 스택 수열 @https://www.acmicpc.net/problem/1874
#!/usr/bin/python3
import sys
n = int(input())
a = [int(input()) for _ in range(n)]
stack = []
m = 0
ans = []

for x in a:
  if x > m:
    while x > m:
      m += 1
      stack.append(m)
      ans += ['+']
    stack.pop()
    ans += ['-']
  else:
    if stack[-1] != x:
      print('NO')
      sys.exit(0)
    stack.pop()
    ans += ['-']

print('\n'.join(ans)+'\n')