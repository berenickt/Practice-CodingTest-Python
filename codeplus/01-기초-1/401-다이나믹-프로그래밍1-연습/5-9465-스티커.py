# 💡 스티커 📚 https://www.acmicpc.net/problem/9465
# 테스트 케이스의 개수 입력
t = int(input())

# 각 테스트 케이스별로 수행하는 반복문 시작
for _ in range(t):
    # 정수 n 입력
    n = int(input())

    # 두 개의 리스트 t1과 t2를 입력 받아서 합침
    t1 = [0] + list(map(int, input().split()))
    t2 = [0] + list(map(int, input().split()))
    a = list(zip(t1, t2))

    # 동적 계획법을 위한 2차원 리스트 d를 생성하고 초기화
    d = [[0] * 3 for _ in range(n + 1)]

    # 각 시간대별 최대 행복도를 계산하는 반복문 시작
    for i in range(1, n + 1):
        # 현재 시간대에서 아무것도 하지 않는 경우의 최대 행복도
        d[i][0] = max(d[i - 1])

        # 현재 시간대에서 t1을 선택하는 경우의 최대 행복도
        d[i][1] = max(d[i - 1][0], d[i - 1][2]) + a[i][0]

        # 현재 시간대에서 t2를 선택하는 경우의 최대 행복도
        d[i][2] = max(d[i - 1][0], d[i - 1][1]) + a[i][1]

    # 최종 시간대에서의 최대 행복도를 출력
    ans = max(d[n])
    print(ans)
