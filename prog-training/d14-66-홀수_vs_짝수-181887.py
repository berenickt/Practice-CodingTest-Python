# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181887
"""
정수 리스트 num_list가 주어집니다.
가장 첫 번째 원소를 1번 원소라고 할 때,
홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return

두 값이 같을 경우 그 값을 return

입력#1
[4, 2, 6, 1, 7, 6]

출력#1
17
"""


def solution(num_list):
    even = sum([n for idx, n in enumerate(num_list) if idx % 2 == 0])
    odd = sum([n for idx, n in enumerate(num_list) if idx % 2 != 0])
    return even if even >= odd else odd


print(solution([4, 2, 6, 1, 7, 6]))
