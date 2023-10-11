# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181907
"""
문자열 my_string과 정수 n이 매개변수로 주어질 때, 
my_string의 앞의 n글자로 이루어진 문자열을 return

입력#1
my_string : "ProgrammerS123"
is_suffix : 11

출력#1
"ProgrammerS"
"""


def solution(my_string, n):
    return my_string[:n]


print(solution("ProgrammerS123", 11))
