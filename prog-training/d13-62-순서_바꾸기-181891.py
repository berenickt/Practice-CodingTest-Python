# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181891
"""
정수 리스트 num_list와 정수 n이 주어질 때, 
num_list를 n번째 원소 이후의 원소들과 
n번째까지의 원소들로 나눠 n번째 원소 이후의 원소들을 
n번째까지의 원소들 앞에 붙인 리스트를 return

입력#1
num_list : [2, 1, 6]
n        : 1

출력#1
[1, 6, 2]
"""


def solution(num_list, n):
    lr = num_list[n:] + num_list[: n - 1]
    lr.append(num_list[n - 1])
    return lr


print(solution([2, 1, 6], 1))
# print(solution([5, 2, 1, 7, 5], 3))  # [7, 5, 5, 2, 1]
