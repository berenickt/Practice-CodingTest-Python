# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181871
"""
문자열 myString과 pat이 주어집니다.
myString에서 pat이 등장하는 횟수를 return

입력#1
myString : "banana"
pat      : "ana"

출력#1
2

📌 cf. 문자열.startswith(인자값문자열)
인자값에 있는 문자열이 string에 있으면 true, 없으면 false를 반환
"""


def solution(myString, pat):
    repeat = 0
    for idx in range(len(myString) - len(pat) + 1):  # e.g.1) 0~4
        if pat == myString[idx : idx + len(pat)]:
            repeat += 1
    return repeat


print(solution("banana", "ana"))


################################
def solution2(myString, pat):
    answer = 0
    for idx, _ in enumerate(myString):
        if myString[idx:].startswith(pat):
            answer += 1
    return answer
