# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181901
"""
정수 n과 k가 주어졌을 때,
1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return

입력#1
n         : 10
k         : 3

출력#1
[3, 6, 9]
"""


def solution(n, k):
    return [n for n in range(1, n + 1) if n % k == 0]


print(solution(10, 3))
