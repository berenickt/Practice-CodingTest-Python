# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181938
"""
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다.
e.g. 12 ⊕ 3 = 123

양의 정수 a와 b가 주어졌을 때, 
a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수
단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 
"""


def solution1(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)


def solution2(a, b):
    res = int(str(a) + str(b))
    comp = 2 * a * b
    return max(res, comp)
