# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181854
"""
정수 배열 arr과 정수 n이 매개변수로 주어집니다.
arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을,
arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return

입력#1
arr : [49, 12, 100, 276, 33]
n   : 27

출력#1
[76, 12, 127, 276, 60]
"""


def solution(arr, n):
    arrLen = len(arr)
    if arrLen % 2:
        for i in range(0, arrLen, 2):
            arr[i] += n
    else:
        for i in range(1, arrLen, 2):
            arr[i] += n
    return arr


print(solution([49, 12, 100, 276, 33], 27))


def solution2(arr, n):
    odd = []
    even = []
    for i, el in enumerate(arr):
        if i % 2 == 0:
            odd.append(el + n)
            even.append(el)
        else:
            odd.append(el)
            even.append(el + n)
    return even if len(arr) % 2 == 0 else odd
