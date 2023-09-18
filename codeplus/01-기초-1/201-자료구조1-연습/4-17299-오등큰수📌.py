# 💡 오등큰수 📚 https://www.acmicpc.net/problem/17299
"""
오등큰수는 등장 횟수가 가장 많은 수 중 가장 왼쪽의 수 입니다. 없는 경우 -1을 출력
"""

freq = [0] * 1000001  # 숫자 빈도수를 저장하는 리스트를 초기화
n = int(input())  # 숫자 개수 n을 입력받습니다.
a = list(map(int, input().split()))  # 숫자들을 리스트로 입력받습니다.
ans = [0] * n  # 결과를 저장할 리스트를 초기화
stack = [0]  # 스택을 초기화하고, 첫 번째 원소의 인덱스를 스택에 넣습니다

# 입력된 숫자들의 빈도수를 계산하여 freq 리스트에 저장합니다
for i in range(n):
    freq[a[i]] += 1

# 1부터 n까지 순회
for i in range(1, n):
    # 스택이 비어있으면 현재 인덱스를 스택에 추가
    if not stack:
        stack.append(i)

    # 현재 원소의 빈도수가 스택의 가장 위에 있는 원소의 빈도수보다 큰 경우
    while stack and freq[a[stack[-1]]] < freq[a[i]]:
        # 스택의 가장 위 원소와 매칭되는 값을 결과 리스트에 저장
        ans[stack.pop()] = a[i]

    # 현재 원소의 인덱스를 스택에 추가
    stack.append(i)

# 스택에 남은 인덱스들은 빈도수에 따라 오른쪽에 더 큰 원소가 없는 경우이므로 처리
while stack:
    ans[stack.pop()] = -1

# 결과 리스트의 값을 문자열로 변환하여 출력
print(" ".join(map(str, ans)))
