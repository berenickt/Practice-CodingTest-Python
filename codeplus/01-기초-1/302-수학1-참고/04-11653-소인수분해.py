# 💡 소인수분해 📚 https://www.acmicpc.net/problem/11653
"""
정수 N이 주어졌을 때, 소인수분해하는 프로그램
"""
n = int(input())
i = 2

# i가 n의 제곱근보다 작거나 같은 동안 순회
while i * i <= n:
    while n % i == 0:
        print(i)  # i를 출력 (i는 n의 소인수 중 하나)
        n //= i
    i += 1

# 남은 n이 1보다 크면, 그 값은 소수이므로 출력
if n > 1:
    print(n)
