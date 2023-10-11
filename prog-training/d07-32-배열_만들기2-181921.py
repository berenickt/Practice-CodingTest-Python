# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181921
"""
정수 l과 r이 주어졌을 때,
l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 
오름차순으로 저장한 배열을 return
만약 그러한 정수가 없다면, -1이 담긴 배열을 return

입력#1
l : 5
r : 555

출력#1
[5, 50, 55, 500, 505, 550, 555]

예 설명#1
5 이상 555 이하의 0과 5로만 이루어진 정수는 
작은 수부터 5, 50, 55, 500, 505, 550, 555
"""


def solution(l, r):
    # set 으로 중복제거 후, 길이가 2 이하
    num_list = []
    condition = set(["0", "5"])  # {'0', '5'}

    for n in range(l, r + 1):
        if n % 5 == 0 and len(set(str(n)) - set(condition)) == 0:
            num_list.append(n)

    return num_list if len(num_list) >= 1 else [-1]


print(solution(5, 555))
