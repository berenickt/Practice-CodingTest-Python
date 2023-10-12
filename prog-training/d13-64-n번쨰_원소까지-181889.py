# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181889
"""
정수 리스트 num_list와 정수 n이 주어질 때,
num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를 담은 리스트를 return

입력#1
num_list : [2, 1, 6]
n        : 1

출력#1
[2]
"""


def solution(num_list, n):
    return num_list[:n]


print(solution([2, 1, 6], 1))
