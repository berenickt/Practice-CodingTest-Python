# 💡 큐 @https://www.acmicpc.net/problem/10845
#!/usr/bin/python3
import sys
input = sys.stdin.readline
n = int(input())

queue = [0]*n
begin = 0
end = 0

for _ in range(n):
  cmd, *val = input().split()
  if cmd == 'push':
    num = int(val[0])
    queue[end] = num
    end += 1
  elif cmd == 'front':
    if begin == end:
      print(-1)
    else:
      print(queue[begin])
  elif cmd == 'size':
    print(end-begin)
  elif cmd == 'empty':
    if begin == end:
      print(1)
    else:
      print(0)
  elif cmd == 'pop':
    if begin == end:
      print(-1)
    else:
      print(queue[begin])
      begin += 1
  elif cmd == 'back':
    if begin == end:
      print(-1)
    else:
      print(queue[end-1])