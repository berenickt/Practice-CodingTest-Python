# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181942
"""
길이가 같은 두 문자열 str1과 str2가 주어집니다.
두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return

📌 zip() : 두 개의 리스트를 서로 묶어줄 때 사용
"""


def solution1(str1, str2):
    answer = ""
    for i in range(0, len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer


def solution2(str1, str2):
    answer = ""
    for s1, s2 in zip(str1, str2):
        answer += s1
        answer += s2
    return answer
