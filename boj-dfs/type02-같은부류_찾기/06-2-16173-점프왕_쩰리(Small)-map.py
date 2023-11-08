### 실버3 📚 https://www.acmicpc.net/problem/16173
# 성능이 더 빠른 input을 쓰기 위한 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [0, 1]
dirX = [1, 0]


def dfs(y, x):
    global map_, N
    value = map_[y][x]
    map_[y][x] = 0

    if y == N and x == N:
        return

    for i in range(2):
        newY = y + dirY[i] * value
        newX = x + dirX[i] * value
        if map_[newY][newX] != 0:
            dfs(newY, newX)


# ✅ 0. 입력 및 초기화
N = map(int, input().split())
MAX = 3 + 100 + 10
map_ = [[0] * MAX for _ in range(MAX)]

# ✅ 1. map에 연결 정보 채우기
for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        map_[i][j] = row[j - 1]

# ✅ 2. dfs(재귀함수) 호출
dfs(1, 1)

# ✅ 3. 정답 출력
print("HaruHaru" if map_[N][N] == 0 else "Hing")
