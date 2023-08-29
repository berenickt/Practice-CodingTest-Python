# 💡 단어 뒤집기 @https://www.acmicpc.net/problem/9093
'''
문장이 주어졌을 때 단어를 모두 뒤집는 문제
단어의 순서를 바꿀 수 없고, 단어는 영어 알파벳으로만 이루어져 있다.
단어의 최대 길이: 20, 문장의 최대 길이: 1000

N개의 문자를 스택에 넣었다가 빼면 순서가 역순이 된다.
알파벳을 스택에 넣고, 공백이나 문자열의 끝이면 스택에서 모두 빼내서 역순을 만든다
'''
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  s = input()
  stack = []
  for ch in s:
    # 역순으로 단어를 출력해야 한다면,
    if ch == ' ' or ch == '\n':
      print(''.join(stack[::-1]), end='')
      stack.clear()
      print(ch, end='')
    else:
      stack.append(ch)