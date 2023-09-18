# 💡 연속합 2 📚 https://www.acmicpc.net/problem/13398
# 정수 n을 입력 받음
n = int(input())

# 정수 리스트 a를 입력 받아 공백으로 분리하여 리스트로 저장
a = list(map(int, input().split()))

# 첫 번째 동적 계획법 리스트 d를 생성하고 초기값 설정
d = [0] * n

# 두 번째 동적 계획법 리스트 dr을 생성하고 초기값 설정 (역방향으로 탐색)
dr = [0] * n

# 첫 번째 동적 계획법: 왼쪽에서 오른쪽으로 증가하는 부분 수열의 합을 계산
for i in range(n):
    d[i] = a[i]
    if i == 0:
        continue
    if d[i] < d[i - 1] + a[i]:
        d[i] = d[i - 1] + a[i]

# 두 번째 동적 계획법: 오른쪽에서 왼쪽으로 증가하는 부분 수열의 합을 계산 (역방향으로 탐색)
for i in range(n - 1, -1, -1):
    dr[i] = a[i]
    if i == n - 1:
        continue
    if dr[i] < dr[i + 1] + a[i]:
        dr[i] = dr[i + 1] + a[i]

# 초기값 설정과 함께 양쪽에서부터 중간 지점까지 최대 합을 계산
ans = max(d)

# 중간 지점에서부터 양쪽으로 확장하여 최대 합을 계산
for i in range(1, n - 1):
    if ans < d[i - 1] + dr[i + 1]:
        ans = d[i - 1] + dr[i + 1]

# 최대 합 출력
print(ans)
