# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181899
"""
정수 start_num와 end_num가 주어질 때,
start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return

입력#1
start_num  : 10
end_num    : 3

출력#1
[10, 9, 8, 7, 6, 5, 4, 3]

cf. range(이상, 미만, 간격), 간격(-1)은 1씩 줄어듬
"""


def solution(start, end):
    return [n for n in range(start, end - 1, -1)]


print(solution(10, 3))
