# 💡 문자열 분석 📚 https://www.acmicpc.net/problem/10820
'''
입력된 여러 줄의 문자열을 처리하면서 소문자, 대문자, 숫자, 공백의 개수를 세고 출력하는 코드
'''
import sys
lines = sys.stdin.readlines()  # 표준 입력에서 여러 줄을 읽어옵니다.

# 읽어온 각 줄에 대해 처리합니다.
for s in lines:
    # 소문자, 대문자, 숫자, 공백의 개수를 초기화
    lower = 0
    upper = 0
    number = 0
    space = 0

    # 현재 줄의 각 문자를 처리
    for ch in s:
        x = ord(ch)  # 현재 문자의 아스키 코드를 구함

        if ord('a') <= x <= ord('z'):
            lower += 1    # 소문자인 경우
        elif ord('A') <= x <= ord('Z'):
            upper += 1  # 대문자인 경우
        elif ord('0') <= x <= ord('9'):
            number += 1  # 숫자인 경우
        elif ch == ' ':
            space += 1                  # 공백인 경우

    # 각 카테고리별 개수를 출력
    print('%d %d %d %d' % (lower, upper, number, space))
