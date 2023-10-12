# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181867
"""
문자열 myString이 주어집니다.
myString을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return

입력#1
"oxooxoxxox"

출력#1
[1, 2, 1, 0, 1, 0]
"""


def solution(myString):
    return [len(s) for s in myString.split("x")]


print(solution("oxooxoxxox"))
