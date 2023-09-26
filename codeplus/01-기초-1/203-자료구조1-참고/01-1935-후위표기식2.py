# 💡 후위 표기식2 📚 https://www.acmicpc.net/problem/1935
n = int(input())  # 피연산자의 개수 n을 입력받음
postfix = input()  # 후위 표기식을 입력받음

# 피연산자들을 리스트로 입력받음
operand = [int(input()) for _ in range(n)]
stack = []  # 스택을 초기화

# 문자 'A'와 'Z'에 해당하는 아스키 코드를 저장
A = ord("A")
Z = ord("Z")

# 후위 표기식을 순회
for ch in postfix:
    # 피연산자인 경우, 해당 피연산자 값을 스택에 추가
    if A <= ord(ch) <= Z:
        stack.append(operand[ord(ch) - A])
    # 연산자인 경우
    else:
        op2 = stack.pop()  # 스택에서 피연산자 2를 꺼냄
        op1 = stack.pop()  # 스택에서 피연산자 1을 꺼냄
        if ch == "+":
            stack.append(op1 + op2)
        elif ch == "-":
            stack.append(op1 - op2)
        elif ch == "*":
            stack.append(op1 * op2)
        elif ch == "/":
            stack.append(op1 / op2)

# 최종 결과를 소수점 2자리까지 출력
print("%.2f" % stack[-1])
