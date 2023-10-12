# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181888
"""
정수 리스트 num_list와 정수 n이 주어질 때,
num_list의 첫 번째 원소부터 마지막 원소까지 
n개 간격으로 저장되어있는 원소들을 차례로 담은 리스트를 return

입력#1
num_list : [4, 2, 6, 1, 7, 6]
n        : 2

출력#1
[4, 6, 7]
"""


def solution(num_list, n):
    return num_list[::n]


print(solution([4, 2, 6, 1, 7, 6], 2))
