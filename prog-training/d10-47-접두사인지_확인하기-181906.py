# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181906
"""
어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 
e.g. "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
문자열 my_string과 is_prefix가 주어질 때,
is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return

입력#1
my_string : "banana"
is_prefix : "ban"

출력#1
1
"""


def solution(my_string, is_prefix):
    real_prefix = [my_string[:i] for i in range(1, len(my_string) + 1)]
    return 1 if is_prefix in real_prefix else 0


print(solution("banana", "ban"))
