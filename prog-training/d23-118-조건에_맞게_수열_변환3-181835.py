# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181835
"""
정수 배열 arr와 자연수 k가 주어집니다.
만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고,
k가 짝수라면 arr의 모든 원소에 k를 더합니다.
이러한 변환을 마친 후의 arr를 return

입력#1
arr : [1, 2, 3, 100, 99, 98]
k   : 3

출력#1
[3, 6, 9, 300, 297, 294]
"""


def solution(arr, k):
    return [n + k for n in arr] if k % 2 == 0 else [m * k for m in arr]


print(solution([1, 2, 3, 100, 99, 98], 3))


def solution(arr, k):
    if k % 2 == 0:
        return [a + k for a in arr]
    else:
        return [a * k for a in arr]
