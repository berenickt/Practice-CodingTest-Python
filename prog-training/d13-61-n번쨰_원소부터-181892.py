# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181892
"""
정수 리스트 num_list와 정수 n이 주어질 때, 
n번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return

입력#1
num_list : [2, 1, 6]
n        : 3

출력#1
[6]
"""


def solution(num_list, n):
    return num_list[n - 1 :]


print(solution([2, 1, 6], 3))
# print(solution([5, 2, 1, 7, 5], 2))  # [2, 1, 7, 5]
