# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181937
"""
num이 n의 배수면 1을 return
num이 n의 배수가 아니면 0을 return
"""


def solution1(num, n):
    return 1 if num % n == 0 else 0


def solution2(num, n):
    return int(num % n == 0)


def solution3(num, n):
    if num % n == 0:
        return 1
    else:
        return 0
