# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181898
"""
정수 배열 arr가 주어집니다. 
이때 arr의 원소는 1 또는 0입니다. 정수 idx가 주어졌을 때, 
idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 
반환하는 solution 함수

단, 만약 그러한 인덱스가 없다면 -1을 반환

입력#1
arr        : [0, 0, 0, 1]
idx        : 1

출력#1
3
"""


def solution(arr, idx):
    new_arr = arr[idx:]  # e.g.1 [0, 0, 1], e.g.2 [1, 0]
    if 1 not in new_arr:
        return -1
    return new_arr.index(1) + idx


print(solution([0, 0, 0, 1], 1))
# print(solution([1, 1, 1, 1, 0], 3))
