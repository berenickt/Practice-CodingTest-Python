# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181920
"""
정수 start_num와 end_num가 주어질 때,
start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return

입력#1
start_num : 3
end_num   : 10

출력#1
[3, 4, 5, 6, 7, 8, 9, 10]

cf. 컴프리헨션
for문과 if문을 이용해서 리스트나 딕셔너리 등의 자료형을 구현하는 방법
(계산식) for (요소) in range(시작, 끝) 
"""


def solution(start, end):
    answer = [n for n in range(start, end + 1)]
    return answer


print(solution(3, 10))
