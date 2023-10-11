# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181911
"""
길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. 
parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다.
각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return

입력#1
my_strings : ["progressive", "hamburger", "hammer", "ahocorasick"]
parts      : [[0, 4], [1, 2], [3, 5], [7, 7]]

출력#1
"programmers"

cf. zip()
여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 
각 객체가 담고 있는 원소를 튜플의 형태로 만듬
"""


def solution(my_strings, parts):
    answer = ""
    for s, p in zip(my_strings, parts):
        answer += s[p[0] : p[1] + 1]
    return answer


print(
    solution(
        ["progressive", "hamburger", "hammer", "ahocorasick"],
        [[0, 4], [1, 2], [3, 5], [7, 7]],
    )
)
