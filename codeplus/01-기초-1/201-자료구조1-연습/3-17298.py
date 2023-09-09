# 💡 오큰수 📚 https://www.acmicpc.net/problem/17298
# 입력된 정수 리스트에서 각 원소 오른쪽에 처음으로 나오는 큰 수를 찾아 결과 리스트에 저장하는 코드

n = int(input())                     # 입력으로 정수 n을 받습니다
a = list(map(int, input().split()))  # 정수들을 리스트로 입력받습니다
ans = [0] * n                        # 결과를 저장할 리스트를 초기화
s = [0]                              # 스택을 초기화하고, 첫 번째 원소의 인덱스를 스택에 넣습니다

# 두 번째 원소부터 끝까지 처리
for i in range(1, n):
    if not s:
        s.append(i)

    # 현재 원소가 스택의 가장 위에 있는 원소보다 큰 경우
    while s and a[s[-1]] < a[i]:
        ans[s.pop()] = a[i]  # 스택의 가장 위 원소와 매칭되는 값을 결과 리스트에 저장
    s.append(i)            # 현재 원소의 인덱스를 스택에 추가

# 스택에 남은 인덱스들은 오른쪽에 큰 원소가 없는 경우이므로 처리
while s:
    ans[s.pop()] = -1

# 결과 리스트의 값을 문자열로 변환하여 출력
print(' '.join(map(str, ans)))
