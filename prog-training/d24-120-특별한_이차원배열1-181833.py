# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181833
"""
정수 n이 매개변수로 주어질 때,
다음과 같은 n x n 크기의 이차원 배열 arr를 return

입력#1
3

출력#1
[
  [1, 0, 0], 
  [0, 1, 0], 
  [0, 0, 1]
]
"""


def solution(n):
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    arr = [[0 for i in range(n)] for j in range(n)]

    # 주 대각선 상의 요소들을 1로 만들어서 단위 행렬의 특성
    for k in range(n):
        arr[k][k] = 1
    return arr


print(solution(3))

"""NumPy(넘파이) : 과학 계산을 위한 라이브러리, 행렬/배열 처리 및 연산
np.eye()  : 주어진 크기 n의 단위 행렬(2D 배열)을 생성
tolist()  : 배열을 파이썬의 리스트로 변환
"""
# import numpy as np
# def solution2(n):
#     return np.eye(n).tolist()
