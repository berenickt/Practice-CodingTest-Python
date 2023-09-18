# 💡 오큰수 📚 https://www.acmicpc.net/problem/17298
"""
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미
e.g.) A = [3, 5, 2, 7]인 경우 
NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1

e.g.)
A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1

스택에 새로 들어오는 수가 top에 존재하는 수보다 크면 그 수는 오큰수가 된다.
오큰수를 구한 후 수열에서 오큰수가 존재하지 않는 숫자에 -1을 출력
값이 아니라 인덱스를 넣는다!!!
"""
N = int(input())  # 입력으로 정수 N을 받음
sequence = list(map(int, input().split()))  # 정수들을 리스트로 입력받음
result = [0] * N  # 결과를 저장할 리스트를 초기화
stack = [0]  # 스택을 초기화하고, 첫 번째 원소의 인덱스를 스택에 넣음

# 1부터 N-1까지의 범위에서 순회
for i in range(1, N):
    # 스택이 비어있으면 현재 원소를 스택에 추가
    if not stack:
        stack.append(i)

    # 현재 원소가 스택의 가장 위에 있는 원소보다 큰 경우, => 오큰수
    while stack and sequence[stack[-1]] < sequence[i]:
        # 스택의 가장 위 원소와 매칭되는 값을 결과 리스트에 저장
        result[stack.pop()] = sequence[i]

    # 현재 원소의 인덱스를 스택에 추가
    stack.append(i)

# 스택에 남은 인덱스들은 오큰수가 없으므로 -1로 처리
while stack:
    result[stack.pop()] = -1

# 결과 리스트의 값을 문자열로 변환하여 출력
print(" ".join(map(str, result)))
