# 💡 2×n 타일링 2 📚 https://www.acmicpc.net/problem/11727
"""
dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 2] 
"""
# 사용자로부터 정수 n을 입력받음
n = int(input())

# Fibonacci 수열의 각 항을 저장하기 위한 배열 d를 초기화
dp = [0] * 1001

# 0번째 항은 1로, 1번째 항은 1로 초기화
dp[0] = 1
dp[1] = 1

# Fibonacci 수열을 계산
for i in range(2, n + 1):
    # 현재 항은 이전 항과 그 이전 항 두 개의 합으로 계산
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 2]

    # 각 항을 10007로 나눈 나머지를 저장 (정수 오버플로우 방지)
    dp[i] %= 10007

# n번째 Fibonacci 수를 출력
print(dp[n])
