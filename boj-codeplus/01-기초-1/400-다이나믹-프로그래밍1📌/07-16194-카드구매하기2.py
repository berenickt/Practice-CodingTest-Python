# 💡 카드 구매하기 2 📚 https://www.acmicpc.net/problem/16194
# 정수 n을 입력받음
numOfCardPack = int(input())
price = [0] + list(map(int, input().split()))

# d[i] = -1은 아직 정답을 구하지 않았다는 의미
dp = [-1] * (numOfCardPack + 1)
print(dp)

# 처음 위치(0)에서의 비용은 0으로 초기화
dp[0] = 0

# 바텀업(DP) 방식으로 최소 비용을 계산
for i in range(1, numOfCardPack + 1):
    for j in range(1, i + 1):
        # d[i]가 -1이거나 d[i]가 현재 계산된 비용보다 크면,
        # d[i]를 d[i - j] + a[j]로 업데이트하여 더 작은 비용을 저장함
        if dp[i] == -1 or dp[i] > dp[i - j] + price[j]:
            dp[i] = dp[i - j] + price[j]

# n번째 위치에서 얻을 수 있는 최소 비용을 출력합니다
print(dp[numOfCardPack])
