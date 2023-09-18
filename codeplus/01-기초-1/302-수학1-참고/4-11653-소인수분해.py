# 💡 소인수분해 📚 https://www.acmicpc.net/problem/11653
# 정수 n을 입력받음
n = int(input())

# i를 2로 초기화
i = 2

# i가 n의 제곱근보다 작거나 같은 동안 반복
while i * i <= n:
    # n이 i로 나누어 떨어질 때까지 반복
    while n % i == 0:
        # i를 출력합니다. (i는 n의 소인수 중 하나)
        print(i)
        # n을 i로 나눔
        n //= i
    # i를 1 증가
    i += 1

# 남은 n이 1보다 크면, 그 값은 소수이므로 출력
if n > 1:
    print(n)
