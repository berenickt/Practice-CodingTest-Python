### 실버3 📚 https://www.acmicpc.net/problem/1012
### 성능이 더 빠른 input을 쓰기 위한 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 상하좌우
dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]


def dfs(y, x):
    global map_
    map_[y][x] = False

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if map_[newY][newX]:
            dfs(newY, newX)


# ✅ 0. 입력 및 초기화
T = int(input())
MAX = 50 + 10

while T > 0:
    T -= 1
    M, N, K = map(int, input().split())

    # ✅ 1. map에 연결 정보 채우기
    map_ = [[False] * MAX for _ in range(MAX)]

    for _ in range(K):
        x, y = map(int, input().split())
        map_[y + 1][x + 1] = True

    # ✅ 2. dfs(재귀함수) 호출
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if map_[i][j]:
                dfs(i, j)
                answer += 1

    # ✅ 3. 정답 출력
    print(answer)
