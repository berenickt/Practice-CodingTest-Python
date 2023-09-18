# 💡 정수 삼각형 📚 https://www.acmicpc.net/problem/1932
# 정수 n을 입력 받음
n = int(input())

# 2차원 리스트 a에 n x n 크기의 배열을 입력 받음
a = [list(map(int, input().split())) for _ in range(n)]

# 동적 계획법을 위한 2차원 리스트 d를 생성하고 초기값 설정
d = [[0] * n for i in range(n)]
d[0][0] = a[0][0]

# 각 셀에 최대 합을 계산하는 반복문 시작
for i in range(1, n):
    for j in range(0, i + 1):
        # 현재 셀의 값은 이전 행의 값과 현재 셀의 값 더하기
        d[i][j] = d[i - 1][j] + a[i][j]

        # 왼쪽 위 대각선 방향으로 이동하여 최대 합을 비교하여 업데이트
        if j - 1 >= 0 and d[i][j] < d[i - 1][j - 1] + a[i][j]:
            d[i][j] = d[i - 1][j - 1] + a[i][j]

# 최종 행의 값 중에서 가장 큰 값이 최대 합
print(max(d[n - 1]))
