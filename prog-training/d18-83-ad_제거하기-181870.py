# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181870
"""
문자열 배열 strArr가 주어집니다.
배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 
남은 문자열을 순서를 유지하여 배열로 return

입력#1
["and","notad","abcd"]

출력#1
["and","abcd"]
"""


def solution(strArr):
    return [word for word in strArr if "ad" not in word]


print(solution(["and", "notad", "abcd"]))


#####################
def solution2(strArr):
    answer = []
    for el in strArr:
        if "ad" in el:
            continue
        answer.append(el)
    return answer
