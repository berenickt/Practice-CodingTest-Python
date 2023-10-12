# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181875
"""
문자열 배열 strArr가 주어집니다.
모든 원소가 알파벳으로만 이루어져 있을 때,
배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로, 
짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환

입력#1
["AAA","BBB","CCC","DDD"]

출력#1
["aaa","BBB","ccc","DDD"]
"""


def solution(strArr):
    answer = []
    for idx, arr in enumerate(strArr):
        if idx % 2 == 0:
            answer.append(arr.lower())
        else:
            answer.append(arr.upper())
    return answer


print(solution(["AAA", "BBB", "CCC", "DDD"]))
