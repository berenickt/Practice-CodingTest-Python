# 💡 덱 📚 https://www.acmicpc.net/problem/10866
# 덱의 앞과 뒤에서 원소를 추가하거나 삭제하고, 덱의 길이나 비어있는지 여부를 출력하는 기능을 수행
import sys
from collections import deque

input = sys.stdin.readline  # 입력을 빠르게 받기 위해 sys.stdin.readline을 사용
n = int(input())  # 명령어의 개수 n을 입력받습니다.
dequeList = deque()  # 덱을 생성

for _ in range(n):
    line = input().split()  # 입력을 공백으로 나누어 명령어와 값(숫자)을 분리
    command = line[0]  # 명령어 부분을 추출

    # 👉 (1) push_front X: 정수 X를 덱의 앞에 넣는다
    if command == "push_front":
        num = int(line[1])
        dequeList.appendleft(num)
    # 👉 (2) push_back X: 정수 X를 덱의 뒤에 넣는다.
    elif command == "push_back":
        num = int(line[1])
        dequeList.append(num)
    # 👉 (3) pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다.
    # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif command == "pop_front":
        if dequeList:
            print(dequeList.popleft())
        else:
            print(-1)
    # 👉 (4) pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.
    # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif command == "pop_back":
        if dequeList:
            print(dequeList.pop())
        else:
            print(-1)
    # 👉 (5) size: 덱에 들어있는 정수의 개수를 출력
    elif command == "size":
        print(len(dequeList))
    # 👉 (6) empty: 덱이 비어있으면 1을, 아니면 0을 출력
    elif command == "empty":
        print(0 if dequeList else 1)
    # 👉 (7) front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif command == "front":
        if dequeList:
            print(dequeList[0])
        else:
            print(-1)
    # 👉 (8) back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif command == "back":
        if dequeList:
            print(dequeList[-1])
        else:
            print(-1)
