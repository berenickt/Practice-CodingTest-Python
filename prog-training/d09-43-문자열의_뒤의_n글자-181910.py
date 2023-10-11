# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181910
"""
문자열 my_string과 정수 n이 매개변수로 주어질 때, 
my_string의 뒤의 n글자로 이루어진 문자열을 return

입력#1
my_string	   : "ProgrammerS123"
n              : 11

출력#1
"grammerS123"

입력 설명#1
my_string에서 뒤의 11글자는 "grammerS123"이므로 이 문자열을 return
"""


def solution(my_string, n):
    return my_string[-n:]


print(solution("ProgrammerS123", 11))
