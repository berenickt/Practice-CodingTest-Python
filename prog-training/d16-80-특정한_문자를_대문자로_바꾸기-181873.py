# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181873
"""
영소문자로 이루어진 문자열 my_string과 
영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때,
my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return

입력#1
myString : "programmers"
alp      : "p"

출력#1
"Programmers"
"""


def solution(my_string, alp):
    new_string = []
    for s in my_string:
        if s == alp:
            new_string.append(s.upper())
        else:
            new_string.append(s)
    return "".join(new_string)


print(solution("programmers", "p"))


###################################
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())
