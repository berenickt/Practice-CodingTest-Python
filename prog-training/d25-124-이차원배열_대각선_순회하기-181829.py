# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181829
"""
2차원 정수 배열 board와 정수 k가 주어집니다.
i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 return

입력#1
board : [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]
k     : 2

출력#1
8
"""


def solution(board, k):
    answer = 0
    for i, b in enumerate(board):
        for j in range(len(b)):
            if i + j <= k:
                answer += board[i][j]
    return answer


print(solution([[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]], 2))
