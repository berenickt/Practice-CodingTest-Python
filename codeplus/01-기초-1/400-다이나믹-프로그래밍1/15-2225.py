# 💡 합분해 📚 https://www.acmicpc.net/problem/2225
# 모듈러 연산을 위한 상수 설정
mod = 1000000000

# 사용자로부터 두 정수 n과 k를 입력 받음
n, k = map(int, input().split())

# 2차원 리스트 d를 생성하여 초기화
d = [[0] * (n + 1) for _ in range(k + 1)]
d[0][0] = 1

# 동적 계획법을 활용하여 계수를 계산하는 반복문 시작
for i in range(1, k + 1):
    for j in range(0, n + 1):
        for l in range(0, j + 1):
            # d[i][j]에 이전 단계의 값들을 더함
            d[i][j] += d[i - 1][j - l]
        # 모듈러 연산 적용
        d[i][j] %= mod

# 결과 값 출력
print(d[k][n])
