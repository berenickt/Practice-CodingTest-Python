# 💡 후위 표기식 📚 https://www.acmicpc.net/problem/1918
"""
중위 표기식이 주어졌을 때 후위 표기식으로 고치는 프로그램
"""


# 연산자의 우선순위를 결정하는 함수
def precedence(ch):
    if ch == "(":
        return 0
    if ch in "+-":
        return 1
    return 2


infix = input()  # 중위 표기식을 입력받음
operators = []  # 연산자들을 저장할 스택을 초기화
result = ""  # 결과를 저장할 문자열을 초기화

for ch in infix:
    # 피연산자인 경우, 결과 문자열에 추가
    if "A" <= ch <= "Z":
        result += ch
    # 여는 괄호인 경우, 스택에 추가
    elif ch == "(":
        operators.append(ch)
    # 닫는 괄호인 경우, 여는 괄호를 만날 때까지 연산자를 스택에서 꺼내 결과에 추가
    elif ch == ")":
        while operators:
            op = operators.pop()
            if op == "(":
                break
            result += op
    # 연산자인 경우, 스택의 연산자 우선순위를 비교
    else:
        # 현재 연산자보다 우선순위가 높거나 같은 연산자를 결과에 추가
        while operators and precedence(operators[-1]) >= precedence(ch):
            result += operators.pop()
        # 현재 연산자를 스택에 추가
        operators.append(ch)

# 스택에 남은 연산자들을 결과에 추가
while operators:
    result += operators.pop()

print(result)
