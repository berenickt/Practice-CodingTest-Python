# 💡 RGB거리 2 📚 https://www.acmicpc.net/problem/17404
# 정수 n을 입력 받음
n = int(input())

# 각 집의 색깔과 비용을 튜플로 저장하는 리스트 a를 생성하고 초기값 설정
a = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

# 동적 계획법을 위한 이중 리스트 d를 생성하고 초기값 설정
d = [[0] * 3 for _ in range(n + 1)]

# 초기 최소 비용을 설정 (아주 큰 값)
ans = 1000 * 1000 + 1

# 첫 번째 집의 색깔을 바꿔가며 최소 비용을 계산
for k in range(3):  # house1's color
    for j in range(3):
        # 첫 번째 집의 색깔을 설정
        if j == k:
            d[1][j] = a[1][j]
        else:
            d[1][j] = 1000 * 1000 + 1  # 아주 큰 값으로 초기화

    # 두 번째 집부터 마지막 집까지 최소 비용을 계산
    for i in range(2, n + 1):
        d[i][0] = min(d[i - 1][1], d[i - 1][2]) + a[i][0]
        d[i][1] = min(d[i - 1][0], d[i - 1][2]) + a[i][1]
        d[i][2] = min(d[i - 1][0], d[i - 1][1]) + a[i][2]

    # 마지막 집의 색깔을 바꿔가며 최소 비용을 갱신
    for j in range(3):
        if j == k:
            continue
        ans = min(ans, d[n][j])

# 최소 비용 출력
print(ans)
