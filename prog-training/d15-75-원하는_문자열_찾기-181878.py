# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181878
"""
알파벳으로 이루어진 문자열 myString과 pat이 주어집니다.
myString의 연속된 부분 문자열 중 pat이 존재하면 1을 
그렇지 않으면 0을 return

단, 알파벳 대문자와 소문자는 구분하지 않습니다

입력#1
myString : "AbCdEfG"
pat      : "aBc"

출력#1
1


"""


def solution(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0


print(solution("AbCdEfG", "aBc"))
