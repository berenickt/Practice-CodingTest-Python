# 💡 덱 📚 https://www.acmicpc.net/problem/10866
# 덱의 앞과 뒤에서 원소를 추가하거나 삭제하고, 덱의 길이나 비어있는지 여부를 출력하는 기능을 수행
import sys
from collections import deque

input = sys.stdin.readline  # 입력을 빠르게 받기 위해 sys.stdin.readline을 사용
n = int(input())  # 명령어의 개수 n을 입력받습니다.
d = deque()  # 덱을 생성

# n번의 반복을 통해 명령어를 처리
for _ in range(n):
    s = input().split()  # 입력을 공백으로 나누어 명령어와 값(숫자)을 분리
    cmd = s[0]  # 명령어 부분을 추출

    if cmd == "push_front":
        num = int(s[1])
        d.appendleft(num)  # 덱의 왼쪽에 값을 추가
    elif cmd == "push_back":
        num = int(s[1])
        d.append(num)  # 덱의 오른쪽에 값을 추가
    elif cmd == "pop_front":
        if d:
            print(d.popleft())  # 덱의 왼쪽에서 값을 빼고 출력
        else:
            print(-1)  # 덱이 비어있으면 -1을 출력
    elif cmd == "pop_back":
        if d:
            print(d.pop())  # 덱의 오른쪽에서 값을 빼고 출력
        else:
            print(-1)  # 덱이 비어있으면 -1을 출력
    elif cmd == "size":
        print(len(d))  # 덱의 길이를 출력
    elif cmd == "empty":
        print(0 if d else 1)  # 덱이 비어있으면 1, 아니면 0을 출력
    elif cmd == "front":
        if d:
            print(d[0])  # 덱의 가장 왼쪽 값을 출력
        else:
            print(-1)  # 덱이 비어있으면 -1을 출력
    elif cmd == "back":
        if d:
            print(d[-1])  # 덱의 가장 오른쪽 값을 출력
        else:
            print(-1)  # 덱이 비어있으면 -1을 출력
