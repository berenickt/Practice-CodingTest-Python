# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181830
"""
이차원 정수 배열 arr이 매개변수로 주어집니다.
arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고,
열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return

입력#1
[[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]

출력#1
[[572, 22, 37, 0], [287, 726, 384, 0], [85, 137, 292, 0], [487, 13, 876, 0]]
"""


def solution(arr):
    col = len(arr[0])
    row = len(arr)
    answer = arr

    if col == row:
        return arr
    elif col > row:
        for _ in range(col - row):
            answer.append([0 for _ in range(col)])
    elif col < row:
        for a in answer:
            for _ in range(row - col):
                a.append(0)
    return answer


print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))
