# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181857
"""
정수 배열 arr이 매개변수로 주어집니다.
arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다.
arr에 최소한의 개수로 0을 추가한 배열을 return

입력#1
[1, 2, 3, 4, 5, 6]

출력#1
[1, 2, 3, 4, 5, 6, 0, 0]
"""


def solution(arr):
    n = 1
    arrLen = len(arr)
    while n < arrLen:
        n *= 2
    return arr + [0] * (n - arrLen)


print(solution([0, 1, 1, 2, 2, 3], 3))
