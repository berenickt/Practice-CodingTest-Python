# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181840
"""
정수 리스트 num_list와 찾으려는 정수 n이 주어질 때,
num_list안에 n이 있으면 1을 없으면 0을 return

입력#1
num_list : [1, 2, 3, 4, 5]
n        : 3

출력#1
1
"""


def solution(num_list, n):
    return 1 if n in num_list else 0


print(solution([1, 2, 3, 4, 5], 3))
