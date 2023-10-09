# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181924
"""
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. 
queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.

각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.
위 규칙에 따라 queries를 처리한 이후의 arr를 return

입력
arr     : [0, 1, 2, 3, 4],	
queries : [[0, 3],[1, 2],[1, 4]]

출력
[3, 4, 1, 0, 2]

예 설명
[0, 1, 2, 3, 4]
[3, 1, 2, 0, 4]
[3, 2, 1, 0, 4]
[3, 4, 1, 0, 2]
"""


def solution(arr, queries):
    for a, b in queries:
        arr[a], arr[b] = arr[b], arr[a]
    return arr
