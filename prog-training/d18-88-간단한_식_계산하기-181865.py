# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181865
"""
문자열 binomial이 매개변수로 주어집니다. 
binomial은 "a op b" 형태의 이항식이고,
a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다.
주어진 식을 계산한 정수를 return

입력#1
"43 + 12"

출력#1
55

📌 cf. eval()
매개변수로 받은 식(expression)을 문자열로 받아서 실행할 수 있다. 
e.g. ‘2 + 1’이라는 문자열이 들어와도 하나의 식으로 판단하여 계산
"""


def solution(binomial):
    cal = binomial.split()
    if cal[1] == "+":
        return int(cal[0]) + int(cal[-1])
    elif cal[1] == "-":
        return int(cal[0]) - int(cal[-1])
    return int(cal[0]) * int(cal[-1])


print(solution("43 + 12"))


###################################
def solution2(binomial):
    return eval(binomial)
