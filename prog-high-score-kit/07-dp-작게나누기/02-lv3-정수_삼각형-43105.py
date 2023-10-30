# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/43105
"""
삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때,
거쳐간 숫자의 최댓값을 return

입력 #1
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

출력 #1
30
"""


def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            left = triangle[i - 1][j - 1] if j != 0 else 0
            right = triangle[i - 1][j] if j != i else 0
            triangle[i][j] = triangle[i][j] + max(left, right)
    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
