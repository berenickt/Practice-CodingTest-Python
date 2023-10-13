# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181849
"""
한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return

입력#1
"123456789"

출력#1
45
"""


def solution(num_str):
    return sum([int(s) for s in num_str])


print(solution("123456789"))
