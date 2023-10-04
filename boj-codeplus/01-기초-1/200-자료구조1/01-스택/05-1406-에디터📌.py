# 💡 에디터 📚 https://www.acmicpc.net/problem/1406
"""
'L'은 커서를 왼쪽으로 옮김 
'D'는 커서를 오른쪽으로 옮김 
'P'는 커서 왼쪽에 문자를 추가 
'B'는 커서 왼쪽에 문자를 삭제
모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램

커서를 기준으로 커서의 왼쪽 스택(left)와 오른쪽 스택(right)로 나눠서 문제를 풀 수 있다.
e.g. abc | xyz (|는 커서를 의미)
"""
import sys

input = sys.stdin.readline

left = list(input().strip())  # 왼쪽 문자열 초기화
right = []  # 오른쪽 문자열을 위한 빈 리스트 생성

M = int(input())  # 수행할 명령어 개수 입력

for _ in range(M):
    line = input().strip().split()  # 공백을 기준으로 입력을 나눠 리스트에 저장
    command = line[0]  # 명령어의 첫 번째 요소 (어떤 작업을 할지)

    if command == "L":
        # 왼쪽 문자열에 남아있는 문자가 있는 경우, 왼쪽 문자열의 마지막 문자를 오른쪽 문자열로 이동
        if left:
            right.append(left.pop())
    elif command == "D":
        # 오른쪽 문자열에 남아있는 문자가 있는 경우, 오른쪽 문자열의 마지막 문자를 왼쪽 문자열로 이동
        if right:
            left.append(right.pop())
    elif command == "P":
        # 두 번째 요소로 주어진 문자를 왼쪽 문자열에 추가
        left.append(line[1])
    elif command == "B":
        # 왼쪽 문자열에 남아있는 문자가 있는 경우, 왼쪽 문자열의 마지막 문자 삭제
        if left:
            left.pop()

left += right[::-1]  # 남은 문자열을 모두 왼쪽 문자열에 추가 (오른쪽 문자열을 뒤집어서)

print("".join(left))  # 왼쪽 문자열을 하나의 문자열로 합쳐서 출력
