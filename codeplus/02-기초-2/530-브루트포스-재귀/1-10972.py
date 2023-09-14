# 💡 1, 2, 3 더하기 📚 https://www.acmicpc.net/problem/9095
def go(s, goal):
    if s > goal:
        return 0

    # 목표에 도달한 경우 1을 반
    if s == goal:
        return 1
    now = 0

    # 주사위를 1부터 3까지 던지는 경우를 모두 고려
    for i in range(1, 4):
        now += go(s + i, goal)
    return now


TEST_CASE = int(input())

for _ in range(TEST_CASE):
    n = int(input())

    # 시작점 0에서 목표 지점 n까지 도달하는 경우의 수를 출력
    print(go(0, n))
