# 💡 오르막 수 📚 https://www.acmicpc.net/problem/11057
# 2차원 배열 d를 생성하고 초기화, 모듈러 연산을 위한 상수 설정
d = [[0] * 10 for _ in range(1001)]
mod = 10007

# 사용자로부터 정수 n을 입력 받음
n = int(input())

# 초기값 설정: 1자리 수의 경우, 각 숫자는 1가지 경우의 수로 초기화
for i in range(10):
    d[1][i] = 1

# 동적 계획법을 활용하여 경우의 수를 계산하는 반복문 시작
for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            d[i][j] += d[i - 1][k]
            d[i][j] %= mod

# 모든 경우의 수를 더하고 모듈러 연산을 적용하여 결과를 출력
ans = sum(d[n])
print(ans % mod)
