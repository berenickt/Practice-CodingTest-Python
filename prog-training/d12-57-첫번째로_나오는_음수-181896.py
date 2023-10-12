# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181896
"""
정수 리스트 num_list가 주어질 때, 
첫 번째로 나오는 음수의 인덱스를 return
음수가 없다면 -1을 return

입력#1
[12, 4, 15, 46, 38, -2, 15]

출력#1
5
"""


def solution(num_list):
    # 음수가 존재하는 경우
    for idx, n in enumerate(num_list):
        if n < 0:
            return idx
    # 음수가 존재하지 않다면 -1 값이 리턴
    return -1


print(solution([12, 4, 15, 46, 38, -2, 15]))
