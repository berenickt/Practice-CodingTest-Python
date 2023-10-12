# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181872
"""
문자열 myString과 pat가 주어집니다.
myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return

입력#1
myString : "AbCdEFG"
pat      : "dE"

출력#1
"AbCdE"
"""


def solution(myString, pat):
    # 맨 뒤 문장과 pat이 동일한 경우
    if myString[-len(pat) :] == pat:
        return myString
    # 문자열 사이에 pat이 위치한 경우
    idx = myString[::-1].index(pat[::-1])  # 문자열 myString을 뒤집어서 idx 찾기
    return myString[:-idx]


print(solution("AbCdEFG", "dE"))


################################
def solution2(myString, pat):
    idx = myString[::-1].index(pat[::-1])
    return myString[: len(myString) - idx]
