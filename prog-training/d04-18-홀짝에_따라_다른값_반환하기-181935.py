# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181935
"""
n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return
n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return
"""


def solution1(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)


def solution2(n):
    if n % 2 == 0:
        return sum([n**2 for n in range(2, n + 1, 2)])
    return sum([n for n in range(1, n + 1, 2)])


def solution3(n):
    if n % 2:
        return sum(range(1, n + 1, 2))
    return sum([i * i for i in range(2, n + 1, 2)])


def solution4(n):
    answer = 0
    if n % 2:
        for i in range(1, n + 1, 2):
            answer += i
    else:
        for i in range(2, n + 1, 2):
            answer += i**2
    return answer
