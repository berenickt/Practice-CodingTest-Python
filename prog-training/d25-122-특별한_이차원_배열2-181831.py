# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181831
"""
n x n 크기의 이차원 배열 arr이 매개변수로 주어질 때,
arr이 다음을 만족하면 1을 아니라면 0을 return

0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]

입력#1
[[5, 192, 33], [192, 72, 95], [33, 95, 999]]

출력#1
1
"""


def solution(arr):
    for i, a in enumerate(arr):
        for j in range(len(a)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1


print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))


def solution2(arr):
    return int(arr == list(map(list, zip(*arr))))
