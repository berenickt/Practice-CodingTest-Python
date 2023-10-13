# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181843
"""
부분 문자열이란 문자열에서 연속된 일부분에 해당하는 문자열을 의미합니다.
e.g. 문자열 "ana", "ban", "anana", "banana", "n"는 
모두 문자열 "banana"의 부분 문자열이지만,
"aaa", "bnana", "wxyz"는 모두 "banana"의 부분 문자열이 아닙니다.

문자열 my_string과 target이 매개변수로 주어질 때,
target이 문자열 my_string의 부분 문자열이라면 1을, 
아니라면 0을 return

입력#1
my_string : "banana"
target    : "ana"

출력#1
1
"""


def solution(my_string, target):
    return 1 if target in my_string else 0


print(solution("banana", "ana"))
