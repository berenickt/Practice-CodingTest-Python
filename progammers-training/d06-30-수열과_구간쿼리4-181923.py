# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181924
"""
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. 
queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.
각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수 만들기
단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장

입력
arr     : [0, 1, 2, 4, 3]
queries : [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

출력
[3, 4, -1]

예 설명
첫 번째 쿼리의 범위에는 0, 1, 2, 4, 3이 있으며 이 중 2보다 크면서 가장 작은 값은 3
두 번째 쿼리의 범위에는 0, 1, 2, 4가 있으며 이 중 2보다 크면서 가장 작은 값은 4
세 번째 쿼리의 범위에는 0, 1, 2가 있으며 여기에는 2보다 큰 값이 없으므로 -1
"""


def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        # 주어진 범위(s부터 e까지)에 있는 원소를 순회
        for el in arr[s : e + 1]:
            if el > k:
                tmp.append(el)
        answer.append(-1 if not tmp else min(tmp))
    return answer


print(solution([0, 1, 2, 4, 3], [[0, 4, 2], [0, 3, 2], [0, 2, 2]]))
