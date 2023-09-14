# 💡 종이 조각 📚 https://www.acmicpc.net/problem/14391
# 입력: 행과 열의 크기 n, m
n, m = map(int, input().split())

# 입력: n개의 행에 각각 m개의 숫자를 가지는 이차원 리스트 a
a = [list(map(int, list(input()))) for _ in range(n)]

# 결과를 저장할 변수
ans = 0

# 모든 가능한 비트마스크 조합을 검사하기 위한 반복문
for s in range(1 << (n * m)):
    sum = 0  # 현재 비트마스크 조합에서의 숫자 합을 저장할 변수

    # 가로 방향으로 숫자를 합산
    for i in range(n):
        cur = 0
        for j in range(m):
            # 이차원 리스트를 일차원으로 변환하는 인덱스 계산
            k = i * m + j
            # 현재 비트가 0인 경우 숫자를 계속 더함
            if (s & (1 << k)) == 0:
                cur = cur * 10 + a[i][j]
            else:
                # 현재 비트가 1인 경우 숫자 합을 갱신하고 cur 초기화
                sum += cur
                cur = 0
        # 가로 방향으로 숫자 합산 완료
        sum += cur

    # 세로 방향으로 숫자를 합산
    for j in range(m):
        cur = 0
        for i in range(n):
            # 이차원 리스트를 일차원으로 변환하는 인덱스 계산
            k = i * m + j
            if (s & (1 << k)) != 0:
                # 현재 비트가 1인 경우 숫자를 계속 더함
                cur = cur * 10 + a[i][j]
            else:
                # 현재 비트가 0인 경우 숫자 합을 갱신하고 cur 초기화
                sum += cur
                cur = 0
        sum += cur  # 세로 방향으로 숫자 합산 완료

    # 현재 조합에서의 숫자 합을 최대값과 비교하여 갱신
    ans = max(ans, sum)

print(ans)  # 최대 숫자 합 출력
