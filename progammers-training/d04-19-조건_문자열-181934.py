# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181934
"""
두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return
"""
# 📌 eval() : 문자열로 표현되는 표현식을 실행해서 결과값을 받아오는 함수


def solution1(ineq, eq, n, m):
    return int(eval(str(n) + ineq + eq.replace("!", "") + str(m)))


def solution2(ineq, eq, n, m):
    answer = 0
    if n > m and ineq == ">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1

    return answer


def solution3(ineq, eq, n, m):
    if eq == "!":
        eq = ""
    return int(eval(f"{n} {ineq}{eq} {m}"))
