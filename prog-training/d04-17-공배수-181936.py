# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181936
"""
number가 n의 배수이면서 m의 배수이면 1
아니라면 0을 return
"""


def solution1(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0


def solution2(number, n, m):
    return int(bool(number % n == 0) & bool(number % m == 0))


def solution3(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    return 0
