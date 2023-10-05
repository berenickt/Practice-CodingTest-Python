# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181928
"""
정수가 담긴 리스트 num_list가 주어집니다.
num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return

입력#1
[3, 4, 5, 2, 1]	

출력#1 
393

홀수만 이어 붙인 수는 351이고 짝수만 이어 붙인 수는 42
"""


def solution(num_list):
    even = ""
    odd = ""
    for num in num_list:
        if num % 2 == 0:
            even += str(num)
        else:
            odd += str(num)
    return int(even) + int(odd)
