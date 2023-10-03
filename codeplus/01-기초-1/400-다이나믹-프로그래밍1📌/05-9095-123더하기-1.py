# 💡 1, 2, 3 더하기 📚 https://www.acmicpc.net/problem/9095
"""
정수 n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램
"""
# 11개의 요소를 가진 배열 dp를 0으로 초기화
dp = [0] * 11

# dp의 첫 번째 요소를 1로 초기화
dp[0] = 1

# 1부터 10까지의 각 숫자에 대해 dp 배열을 순회
for i in range(1, 11):
    if i - 1 >= 0:
        dp[i] += dp[i - 1]
    if i - 2 >= 0:
        dp[i] += dp[i - 2]
    if i - 3 >= 0:
        dp[i] += dp[i - 3]

# 테스트 케이스의 개수를 입력받음
TEST_CASE = int(input())

# 각 테스트 케이스에 대해 dp 배열의 해당 인덱스 값을 출력
for _ in range(TEST_CASE):
    n = int(input())
    print(dp[n])
