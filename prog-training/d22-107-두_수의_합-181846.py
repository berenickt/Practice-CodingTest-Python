# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181846
"""
0 이상의 두 정수가 문자열 a, b로 주어질 때, 
a + b의 값을 문자열로 return

입력#1
a  : "582"
b  : "734"

출력#1
"1316"
"""


def solution(a, b):
    return str(int(a) + int(b))


print(solution("582", "734"))
