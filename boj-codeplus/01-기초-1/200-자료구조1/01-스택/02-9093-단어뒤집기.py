# 💡 단어 뒤집기 📚 https://www.acmicpc.net/problem/9093
"""
N개의 글자를 스택에 넣었다가 빼면 순서가 역순이 된다.
알파벳을 스택에 넣고, 공백이나 문자열의 끝이면 스택에서 모두 빼내서 역순을 만든다.

📌 [::-1] : 리스트를 처음부터 끝까지 거꾸로 스텝하라는 의미
            -> 파이썬 리스트에서 슬라이싱을 사용하여 역순으로 된 리스트를 생성
📌 join() : 문자열 리스트의 각 요소들을 하나의 문자열로 이어붙이는 역할
"""
import sys

input = sys.stdin.readline

TEST_CASE = int(input())


for _ in range(TEST_CASE):
    inputSentence = input()  # 한 줄을 읽어들여 변수에 저장
    stack = []

    # 문자열 inputSentence에 대해 한 문자씩 반복
    for charactor in inputSentence:
        if charactor == " " or charactor == "\n":
            # stack에 저장된 문자들을 역순으로 이어붙여서 출력하고, 마지막의 개행 문자를 제거
            print("".join(stack[::-1]), end="")
            stack.clear()

            # 공백(' ') 또는 개행 문자('\n')를 출력
            print(charactor, end="")
        # 문자 ch가 공백 또는 개행 문자가 아니라면, stack에 문자를 추가
        else:
            stack.append(charactor)
