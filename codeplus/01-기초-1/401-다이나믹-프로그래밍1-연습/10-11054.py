# 💡 가장 긴 바이토닉 부분 수열 📚 https://www.acmicpc.net/problem/11054
# 정수 n을 입력 받음
n = int(input())

# 정수 리스트 a를 입력 받아 공백으로 분리하여 리스트로 저장
a = list(map(int, input().split()))

# 첫 번째 동적 계획법 리스트 d1을 생성하고 초기값 설정
d1 = [0] * n

# 두 번째 동적 계획법 리스트 d2를 생성하고 초기값 설정
d2 = [0] * n

# 첫 번째 동적 계획법: 가장 긴 증가 부분 수열을 계산
for i in range(n):
    d1[i] = 1
    for j in range(i):
        if a[j] < a[i] and d1[j] + 1 > d1[i]:
            d1[i] = d1[j] + 1

# 두 번째 동적 계획법: 가장 긴 감소 부분 수열을 계산 (역방향으로 탐색)
for i in range(n - 1, -1, -1):
    d2[i] = 1
    for j in range(i + 1, n):
        if a[i] > a[j] and d2[j] + 1 > d2[i]:
            d2[i] = d2[j] + 1

# 각 위치에서 증가 부분 수열과 감소 부분 수열을 합쳐 최대 길이를 계산
d = [d1[i] + d2[i] - 1 for i in range(n)]

# 최대 길이 출력
print(max(d))
