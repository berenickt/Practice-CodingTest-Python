# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181943
"""
1. myS에서 인덱스 2부터 overS의 길이(8)만큼에 해당하는 부분 추출 ===> "11oWor1"
2. 이를 "lloWorl"로 바꾸기
"""


def solution(myS, overS, num):
    sumS = myS[:num] + overS
    lastS = myS[num + len(overS) :]
    return sumS + lastS


print(solution("He11oWor1d", "lloWorl", 2))
