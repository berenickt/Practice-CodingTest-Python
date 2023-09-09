# 💡 후위 표기식2 📚 https://www.acmicpc.net/problem/1935
n = int(input())  # 피연산자의 개수 n을 입력받습니다.
postfix = input()  # 후위 표기식을 입력받습니다.

# 피연산자들을 리스트로 입력받습니다.
operand = [int(input()) for _ in range(n)]
s = []  # 스택을 초기화

# 문자 'A'와 'Z'에 해당하는 아스키 코드를 저장
A = ord("A")
Z = ord("Z")

# 후위 표기식을 순회하며 계산합니다.
for ch in postfix:
    if A <= ord(ch) <= Z:  # 피연산자인 경우, 해당 피연산자 값을 스택에 추가
        s.append(operand[ord(ch) - A])
    else:  # 연산자인 경우
        op2 = s.pop()  # 스택에서 피연산자 2를 꺼냄
        op1 = s.pop()  # 스택에서 피연산자 1을 꺼냄
        if ch == "+":
            s.append(op1 + op2)  # 덧셈 연산을 수행하고 결과를 스택에 추가
        elif ch == "-":
            s.append(op1 - op2)  # 뺄셈 연산을 수행하고 결과를 스택에 추가
        elif ch == "*":
            s.append(op1 * op2)  # 곱셈 연산을 수행하고 결과를 스택에 추가
        elif ch == "/":
            s.append(op1 / op2)  # 나눗셈 연산을 수행하고 결과를 스택에 추가

# 최종 결과를 소수점 2자리까지 출력합니다.
print("%.2f" % s[-1])
