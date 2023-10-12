# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181882
"""
정수 배열 arr가 주어집니다. 
arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고,
50보다 작은 홀수라면 2를 곱합니다.
그 결과인 정수 배열을 return

입력#1
[1, 2, 3, 100, 99, 98]

출력#1
[2, 2, 6, 50, 99, 49]
"""


def solution(arr):
    l = []
    for a in arr:
        if a >= 50 and a % 2 == 0:
            l.append(a // 2)
        elif a < 50 and a % 2 != 0:
            l.append(a * 2)
        else:
            l.append(a)
    return l


print(solution([1, 2, 3, 100, 99, 98]))
