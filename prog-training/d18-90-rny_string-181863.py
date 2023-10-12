# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181863
"""
'm'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다.
문자열 rny_string이 주어질 때,
rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return

입력#1
"masterpiece"

출력#1
"rnasterpiece"
"""


def solution(rny_string):
    answer = ""
    for s in rny_string:
        if s == "m":
            answer += "rn"
        else:
            answer += s
    return answer


print(solution("masterpiece"))


####################################3
def solution2(rny_string):
    return "".join(["rn" if s == "m" else s for s in rny_string])
