# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181894
"""
정수 배열 arr가 주어집니다. 
배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return

단, arr에 2가 없는 경우 [-1]을 return

입력#1
[1, 2, 1, 4, 5, 2, 9]

출력#1
[2, 1, 4, 5, 2]
"""


def solution(arr):
    # 2가 존재하지 않는 경우
    if 2 not in arr:
        return [-1]

    # 배열의 첫 번째 요소와 마지막 요소가 2인 경우(배열 그대로를 출력)
    if arr[0] == 2 and arr[-1] == 2:
        return arr

    # 그 외의 케이스
    idx = arr.index(2)
    reverse_idx = -arr[::-1].index(2)
    return arr[idx:reverse_idx]


print(solution([1, 2, 1, 4, 5, 2, 9]))


#####################################
def solution2(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
