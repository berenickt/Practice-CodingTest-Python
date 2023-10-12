# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181864
"""
문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다.
myString의 "A"를 "B"로, 
"B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return

입력#1
myString : "ABBAA"
pat      : "AABB"

출력#1
1

입출력 예#1
ABBAA"에서 "A"와 "B"를 서로 바꾸면 "BAABB"입니다.
여기에는 부분문자열 "AABB"가 있기 때문에 1을 return
"""


def solution(myString, pat):
    newString = ""
    for s in myString:
        if s == "A":
            newString += "B"
        else:
            newString += "A"
    return 1 if pat in newString else 0


print(solution("ABBAA", "AABB"))


##################################
def solution2(myString, pat):
    pat = "".join(["A" if p == "B" else "B" for p in pat])
    return 1 if pat in myString else 0
