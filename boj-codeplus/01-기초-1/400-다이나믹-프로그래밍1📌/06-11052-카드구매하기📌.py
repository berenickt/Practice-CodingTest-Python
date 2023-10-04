# 💡 카드 구매하기 📚 https://www.acmicpc.net/problem/11052
"""
작은 문제부터 생각
dp[i] = 카드 i개 구매하는 최대 가격
price[k] = k개가 들어있는 카드팩 가격
카드를 i개 구매하는 최대 비용
p[1] + dp[i-1]
p[2] + dp[i-2]
...
p[i] + dp[0]

따라서 점화식은 dp[i] = p[k] + dp[i - k]

입력
4          ===> 사려고하는 카드 개수
1 5 6 7    ===> P_1 = 1, P_2 = 5, P_3 = 5, P_4 = 7, 가격 리스트

출력
10
"""
numOfCardPack = int(input())

# 리스트 a에 0을 추가하고, 사용자로부터 입력받은 숫자들을 리스트로 변환하여 저장
price = [0] + list(map(int, input().split()))  # e.g.1) [0, 1, 5, 6, 7]

# 각 위치에서 얻을 수 있는 최대 값을 저장할 배열 dp를 초기화
dp = [0] * (numOfCardPack + 1)

# 바텀업(DP) 방식으로 최대 가격을 계산
for i in range(1, numOfCardPack + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + price[j])

# n번째 위치에서 얻을 수 있는 최대 값을 출력
print(dp[numOfCardPack])
