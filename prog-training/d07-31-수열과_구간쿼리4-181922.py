# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181922
"""
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. 
queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 
i가 k의 배수이면 arr[i]에 1을 더합니다.
위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수

입력#1
arr     : [0, 1, 2, 4, 3]
queries : [[0, 4, 1],[0, 3, 2],[0, 3, 3]]

출력#1
[3, 2, 4, 6, 4]

예 설명#1
[0, 1, 2, 4, 3]
[1, 2, 3, 5, 4]
[2, 2, 4, 5, 4]
[3, 2, 4, 6, 4]
"""


def solution(arr, queries):
    for q in queries:
        for i in range(q[0], q[1] + 1):
            if i % q[-1] == 0:
                arr[i] = arr[i] + 1
    return arr


print(solution([0, 1, 2, 4, 3], [[0, 4, 1], [0, 3, 2], [0, 3, 3]]))
