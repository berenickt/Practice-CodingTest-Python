# 💡 쇠막대기 📚 https://www.acmicpc.net/problem/10799
'''
주어진 문자열에서 괄호 쌍의 개수를 계산하는 코드
'('일 경우 스택에 추가하고, ')'일 경우 스택에서 짝이 맞는 여는 괄호를 제거하고 결과에 추가
'''
# 입력으로 받은 문자열을 저장
arr = input()

# 스택과 결과를 초기화
stack = []
result = 0

# 문자열의 각 문자를 처리
for i in range(len(arr)):
    if arr[i] == '(':        # **** 여는 괄호일 경우, 스택에 추가
        stack.append(arr[i])
    else:                    # **** 닫는 괄호일 경우
        if arr[i-1] == '(':    # ** 짝이 맞는 여는 괄호 바로 앞에 있는 경우
            stack.pop()          # 짝이 맞는 여는 괄호를 스택에서 제거
            result += len(stack)  # 현재 스택의 길이를 결과에 더함
        else:                  # ** 짝이 맞는 여는 괄호가 바로 앞에 없는 경우
            stack.pop()          # 스택에서 여는 괄호를 제거
            result += 1          # 결과에 1을 더함

print(result)
