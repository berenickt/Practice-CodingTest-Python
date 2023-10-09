# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181929
"""
정수가 담긴 리스트 num_list가 주어질 때,
모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return

입력#1
[3, 4, 5, 2, 1]	

출력#1
1
"""
# 📌 eval 함수 : 매개변수로 받은 expression(=식)을 문자열로 받아서, 실행하는 함수


def solution1(num_list):
    sumSquare = sum(num_list) ** 2
    multi = eval("*".join([str(n) for n in num_list]))
    return 1 if sumSquare > multi else 0


def solution2(num_list):
    sumSquare = 1
    multi = 0
    for el in num_list:
        sumSquare *= el
        multi += el
    return 1 if sumSquare < multi * multi else 0
