# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181883
"""
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다.
queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.
위 규칙에 따라 queries를 처리한 이후의 arr를 return

입력#1
arr     : [0, 1, 2, 3, 4]
queries : [[0, 1],[1, 2],[2, 3]]

출력#1
[1, 3, 4, 4, 4]

입출력 설명#1
-	-	    [0, 1, 2, 3, 4]
0	[0,1]	[1, 2, 2, 3, 4]
1	[1,2]	[1, 3, 3, 3, 4]
2	[2,3]	[1, 3, 4, 4, 4]
"""


def solution(arr, queries):
    for q in queries:
        for i in range(q[0], q[1] + 1):
            arr[i] += 1
    return arr


print(solution([0, 1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]]))
