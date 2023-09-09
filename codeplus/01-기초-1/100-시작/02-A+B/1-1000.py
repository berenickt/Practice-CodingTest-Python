# 💡 A+B - 1 📚 https://www.acmicpc.net/problem/1000
"""
이썬 코드로, 두 개의 정수를 입력받아 각각 변수 a와 b에 저장하는 코드
📌 input()       : 사용자로부터 입력을 받음
📌 split()       : 입력받은 문자열을 공백을 기준으로 분리하여 리스트로 만듬
📌 map(int, ...) : 리스트의 각 요소를 int 함수를 사용하여 정수로 변환

e.g. "3 5"라고 입력하면, a에는 3이, b에는 5가 저장됨
print(input().split())
"""
a, b = map(int, input().split())
print(a + b)
