# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181917
"""
boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 
다음의 식의 true/false를 return

입력#1
False, True, True, True

출력#1
True
"""


def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)


print(solution(False, True, True, True))
