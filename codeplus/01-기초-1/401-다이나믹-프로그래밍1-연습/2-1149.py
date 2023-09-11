# 💡 RGB거리 📚 https://www.acmicpc.net/problem/1149
# 정수 n을 입력 받음
n = int(input())

# 각 집을 칠하는 비용을 저장하는 리스트 a를 생성하고 초기값 추가
a = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

# 동적 계획법을 위한 2차원 리스트 d를 생성하고 초기화
d = [[0, 0, 0] for _ in range(n + 1)]

# 각 집을 칠하는 경우의 최소 비용을 계산하는 반복문 시작
for i in range(1, n + 1):
    # i번째 집을 빨강으로 칠하는 경우
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + a[i][0]

    # i번째 집을 초록으로 칠하는 경우
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + a[i][1]

    # i번째 집을 파랑으로 칠하는 경우
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + a[i][2]

# 모든 집을 칠한 후의 최소 비용 출력
print(min(d[n][0], d[n][1], d[n][2]))
