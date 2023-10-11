# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181909
"""
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 
e.g. “banana”의 모든 접미사는 “banana”, “anana”, “nana”, “ana”, “na”, “a”입니다. 
문자열 my_string이 매개변수로 주어질 때, 
my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return

입력#1
"banana"

출력#1
["a", "ana", "anana", "banana", "na", "nana"]

cf.
- 리스트.sort()  : 본체의 리스트를 정렬해서 변환
- sorted(리스트) : 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환
>>> sorted([3, 5, 2, 1, 4])
[1, 2, 3, 4, 5]
>>> sorted(["D", "A", "C", "B", "E"])
['A', 'B', 'C', 'D', 'E']
>>> sorted(a, reverse=True) : 내림차순, (생략 시 기본 오름차순임)

"""


def solution(my_string):
    return sorted([my_string[-i:] for i in range(1, len(my_string) + 1)])


print(solution("banana"))
