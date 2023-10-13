# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181842
"""
어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다.
e.g. 문자열 "abc"는 문자열 "aabcc"의 부분 문자열입니다.

문자열 str1과 str2가 주어질 때,
str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return

입력#1
str1 : "abc"
str2 : "aabcc"

출력#1
1
"""


def solution(str1, str2):
    return 1 if str1 in str2 else 0


print(solution("abc", "aabcc"))
