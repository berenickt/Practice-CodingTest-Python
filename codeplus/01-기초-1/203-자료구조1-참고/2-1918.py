# 💡 후위 표기식 @https://www.acmicpc.net/problem/1918

# 연산자의 우선순위를 결정하는 함수를 정의
def precedence(ch):
  if ch == '(': return 0
  if ch in '+-': return 1
  return 2

s = input() # 중위 표기식을 입력받습니다.
ops = []    # 연산자들을 저장할 스택을 초기화
ans = ''    # 결과를 저장할 문자열을 초기화

# 중위 표기식의 각 문자를 처리
for ch in s:
  # ** 피연산자인 경우, 결과 문자열에 추가합
  if 'A' <= ch <= 'Z': ans += ch
  # 여는 괄호인 경우, 스택에 추가
  elif ch == '(': ops.append(ch)
  # 닫는 괄호인 경우
  elif ch == ')':
    while ops:
      op = ops.pop()
      if op == '(': break # 여는 괄호를 만날 때까지 연산자를 스택에서 꺼내 결과에 추가
      ans += op
  # ** 연산자인 경우
  else:
    # 스택의 연산자 우선순위를 비교
    while ops and precedence(ops[-1]) >= precedence(ch):
      ans += ops.pop() # 현재 연산자보다 우선순위가 높거나 같은 연산자를 결과에 추가
    ops.append(ch)     # 현재 연산자를 스택에 추가

# 스택에 남은 연산자들을 결과에 추가
while ops:
  ans += ops.pop()

print(ans) # 최종 결과를 출력