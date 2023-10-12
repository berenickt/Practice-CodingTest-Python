# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181874
"""
문자열 myString이 주어집니다.
myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고,
"A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return

입력#1
"abstract algebra"

출력#1
"AbstrAct AlgebrA"
"""


def solution(myString):
    myString = myString.lower()
    newString = ""
    for s in myString:
        if s == "a":
            newString += "A"
        else:
            newString += s
    return newString


print(solution("abstract algebra"))


###################################
def solution2(myString):
    return myString.lower().replace("a", "A")
