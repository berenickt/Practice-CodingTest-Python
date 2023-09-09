# 💡 에디터 📚 https://www.acmicpc.net/problem/1406
'''
문자열 편집 명령어를 처리하여 최종 결과를 출력하는 프로그램
'L'은 커서를 왼쪽으로 옮기고, 'D'는 커서를 오른쪽으로 옮기며, 
'P'는 문자를 추가하고, 'B'는 왼쪽의 문자를 삭제하는 작업
'''
import sys

input = sys.stdin.readline    # 입력 속도 향상을 위해 사용
left = list(input().strip())  # 왼쪽 문자열 초기화
right = []                    # 오른쪽 문자열을 위한 빈 리스트 생성
m = int(input())              # 수행할 명령어 개수 입력

for _ in range(m):
    line = input().strip().split()  # 공백을 기준으로 입력을 나눠 리스트에 저장
    what = line[0]                  # 명령어의 첫 번째 요소 (어떤 작업을 할지)

    if what == 'L':
        if left:                      # 왼쪽 문자열에 남아있는 문자가 있는 경우에만
            right.append(left.pop())  # 왼쪽 문자열의 마지막 문자를 오른쪽 문자열로 이동
    elif what == 'D':
        if right:       # 오른쪽 문자열에 남아있는 문자가 있는 경우에만
            left.append(right.pop())  # 오른쪽 문자열의 마지막 문자를 왼쪽 문자열로 이동
    elif what == 'P':
        left.append(line[1])  # 두 번째 요소로 주어진 문자를 왼쪽 문자열에 추가
    elif what == 'B':
        if left:         # 왼쪽 문자열에 남아있는 문자가 있는 경우에만
            left.pop()     # 왼쪽 문자열의 마지막 문자 삭제

left += right[::-1]  # 남은 문자열을 모두 왼쪽 문자열에 추가 (오른쪽 문자열을 뒤집어서)

print(''.join(left))  # 왼쪽 문자열을 하나의 문자열로 합쳐서 출력
