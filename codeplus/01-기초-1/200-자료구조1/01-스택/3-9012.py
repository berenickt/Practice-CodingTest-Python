# 💡 괄호 @https://www.acmicpc.net/problem/9012
#!/usr/bin/python3
def valid(s):
  cnt = 0
  for ch in s:
    if ch == '(':
      cnt += 1
    else:
      cnt -= 1
    if cnt < 0:
      return 'NO'
  if cnt == 0:
    return 'YES'
  else:
    return 'NO'

t = int(input())
for _ in range(t):
  print(valid(input()))