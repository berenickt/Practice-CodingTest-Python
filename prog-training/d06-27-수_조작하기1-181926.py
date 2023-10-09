# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181926
"""
정수 n과 문자열 control이 주어집니다. 
control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, 
control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.

"w" : n이 1 커집니다.
"s" : n이 1 작아집니다.
"d" : n이 10 커집니다.
"a" : n이 10 작아집니다.

위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return
"""


def solution1(n, control):
    for c in control:
        if c == "w":
            n += 1
        elif c == "s":
            n -= 1
        elif c == "d":
            n += 10
        else:
            n -= 10
    return n


def solution2(n, control):
    key = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))
    return n + sum([key[c] for c in control])


def solution(n, control):
    answer = n
    c = {"w": 1, "s": -1, "d": 10, "a": -10}
    for i in control:
        answer += c[i]
    return answer
