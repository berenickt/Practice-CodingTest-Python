# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181939
"""
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 
e.g. 12 ⊕ 3 = 123

양의 정수 a와 b가 주어졌을 때, 
a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 
"""


# 방법 1
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))


# 방법 2
def solution(a, b):
    a, b = str(a), str(b)
    return int(max(a + b, b + a))
