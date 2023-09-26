# 💡 합분해 📚 https://www.acmicpc.net/problem/2225
# 모듈러 연산을 위한 상수 설정
mod = 1000000000

# 입력을 받아서 n과 m에 할당
n, m = map(int, input().split())

# 배열 d 초기화
d = [0] * (n + 1)

# 초기값 설정
d[0] = 1

# m번 반복하는 반복문
for i in range(1, m + 1):
    # 1부터 n까지 반복하는 반복문
    for j in range(1, n + 1):
        # 현재 위치의 값을 이전 값과 더하고 모듈러 연산을 수행
        d[j] += d[j - 1]
        d[j] %= mod

# 결과 출력
print(d[n])
