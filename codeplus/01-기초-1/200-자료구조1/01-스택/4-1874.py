# 💡 스택 수열 📚 https://www.acmicpc.net/problem/1874
# 주어진 입력 순서대로 숫자를 스택에 push하고 pop하여 주어진 수열을 만들 수 있는지 판단하는 프로그램
import sys

n = int(input())                     # 숫자 개수 입력
a = [int(input()) for _ in range(n)]  # n개의 숫자를 입력받아 리스트에 저장
stack = []  # 스택을 초기화할 리스트
m = 0      # 현재까지 스택에 push한 숫자의 최댓값을 나타내는 변수
ans = []   # 결과를 저장할 리스트

for x in a:
    # ** 입력된 숫자가 현재 최댓값보다 큰 경우
    if x > m:
        while x > m:      # x와 같아질 때까지 반복
            m += 1          # 최댓값을 증가시키며
            stack.append(m)  # 스택에 값을 추가하고
            ans += ['+']    # 결과 리스트에 '+' 기호를 추가하여 push 동작을 표시
        stack.pop()       # 반복이 끝난 후 스택에서 값을 제거하여 pop 동작 표시
        ans += ['-']      # 결과 리스트에 '-' 기호를 추가하여 pop 동작을 표시
    # ** 입력된 숫자가 현재 최댓값보다 작거나 같은 경우
    else:
        if stack[-1] != x:  # 스택의 맨 위 값과 입력된 숫자가 다른 경우 'NO' 출력
            print('NO')
            sys.exit(0)      # 프로그램 종료
        stack.pop()        # 스택의 맨 위 값과 입력된 숫자가 같은 경우, 스택에서 값을 제거하여 pop 동작 표시
        ans += ['-']       # 결과 리스트에 '-' 기호를 추가하여 pop 동작을 표시

# 결과 리스트의 내용을 개행문자와 함께 출력
print('\n'.join(ans)+'\n')
