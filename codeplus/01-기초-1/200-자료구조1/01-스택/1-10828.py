# 💡 스택 @https://www.acmicpc.net/problem/10828
'''
파이썬은 따로 stack 구조를 제공하지 않는다.
기본 클래스 list를 이용하여 stack을 표현할 수 있다.
이때, input() 함수를 사용할 경우, 
시간초과 에러가 뜨므로 시간단축을 위해 sys.stdin.readline()을 사용한다.
'''
import sys
input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
  s = input().split()
  cmd = s[0]
  if cmd == 'push':
    num = int(s[1])
    stack.append(num)
  elif cmd == 'top': 
    if stack:
      print(stack[-1])
    else:
      print(-1)
  elif cmd == 'size': 
    print(len(stack))
  elif cmd == 'empty': 
    print(0 if stack else 1)
  elif cmd == 'pop': 
    if stack:
      print(stack.pop())
    else:
      print(-1)