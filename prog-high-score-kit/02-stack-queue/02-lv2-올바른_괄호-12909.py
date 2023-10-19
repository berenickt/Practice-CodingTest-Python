# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/12909
"""
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 
반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 

예를 들어
"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.

'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 
문자열 s가 올바른 괄호이면 true를 return 하고, 
올바르지 않은 괄호이면 false를 return

입력 #1
"()()"

출력 #1
true
"""


def solution(s):
    s_list = []
    for bra in s:
        if bra == "(":
            s_list.append(bra)
        elif bra == ")" and len(s_list) >= 1:
            s_list.pop()
        else:
            return False
    return len(s_list) == 0


print(solution("()()"))


def solution2(s):
    pair = 0
    for x in s:
        if pair < 0:
            break
        pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
    return pair == 0
