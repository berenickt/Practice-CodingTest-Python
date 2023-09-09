# 💡 스택 📚 https://www.acmicpc.net/problem/10828
'''
파이썬은 따로 stack 구조를 제공하지 않는다.
기본 클래스 list를 이용하여 stack을 표현할 수 있다.
'''
import sys
input = sys.stdin.readline  # 입력을 빠르게 받기 위해 sys.stdin.readline을 input으로 사용
n = int(input())            # 정수 n을 입력받습니다. 이것은 명령의 개수를 의미
stack = []                  # 스택을 생성, 스택은 나중에 사용될 리스트

for _ in range(n):  # n번 반복
    s = input().split()   # 공백을 기준으로 문자열을 분리
    cmd = s[0]            # 리스트 s의 첫 번째 요소를 명령어로 설정

    if cmd == 'push':
        num = int(s[1])    # 문자열을 정수로 변환하여 숫자를 얻음
        stack.append(num)  # 스택에 숫자를 추가

    elif cmd == 'top':
        # 스택이 있으면, 가장 위에 있는 숫자를 출력
        if stack:
            print(stack[-1])
        # 스택이 비어있으면, -1 출력
        else:
            print(-1)

    # 스택의 크기(길이)를 출력
    elif cmd == 'size':
        print(len(stack))

    # 스택이 비어있으면 1, 아니면 0을 출력
    elif cmd == 'empty':
        print(0 if stack else 1)

    elif cmd == 'pop':
        # 스택이 있으면, 가장 위에 있는 숫자를 꺼내고 출력
        if stack:
            print(stack.pop())
        # 스택이 비어있으면, -1을 출력
        else:
            print(-1)
