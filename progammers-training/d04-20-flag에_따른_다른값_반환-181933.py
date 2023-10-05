# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181933
"""
flag가 true면 a + b를 false면 a - b를 return
"""


def solution1(a, b, flag):
    return a + b if flag else a - b


def solution2(a, b, flag):
    if flag:
        return a + b
    return a - b
