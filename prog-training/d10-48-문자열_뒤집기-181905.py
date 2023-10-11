# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181905
"""
문자열 my_string과 정수 s, e가 매개변수로 주어질 때,
my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return

입력#1
my_string : "Progra21Sremm3"
s         : 6
e         : 12

출력#1
"ProgrammerS123"
"""


def solution(my_string, s, e):
    answer = list(my_string)
    answer[s : e + 1] = answer[s : e + 1][::-1]
    return "".join(answer)


print(solution("Progra21Sremm3", 6, 12))
