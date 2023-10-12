# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181879
"""
정수가 담긴 리스트 num_list가 주어질 때,
리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 
리스트의 길이가 10 이하이면 모든 원소의 곱을 return

입력#1
[3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]

출력#1
51
"""


def solution(num_list):
    num = 1
    if len(num_list) > 10:
        return sum(num_list)
    else:
        for n in num_list:
            num *= n
    return num


print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
