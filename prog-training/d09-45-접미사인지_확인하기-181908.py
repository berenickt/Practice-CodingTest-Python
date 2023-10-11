# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181908
"""
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다.
e.g. "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string과 is_suffix가 주어질 때,
is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 

입력#1
my_string : "banana"
is_suffix : "ana"

출력#1
1
"""


def solution(my_string, is_suffix):
    real_suffix = [my_string[-i:] for i in range(1, len(my_string) + 1)]
    return 1 if is_suffix in real_suffix else 0


print(solution("banana", "ana"))
