### 실버4 📚 https://www.acmicpc.net/problem/1388
# 성능이 더 빠른 input을 쓰기 위한 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(y, x):
    global map_
    cur = map_[y][x]
    map_[y][x] = ""

    if cur == "-" and map[y][x + 1] == "-":
        dfs(y, x + 1)
    elif cur == "|" and map[y + 1][x] == "|":
        dfs(y + 1, x)


# ✅ 0. 입력 및 초기화
N, M = map(int, input().split())
MAX = 50 + 10
map_ = [[""] * MAX for _ in range(MAX)]

# ✅ 1. map에 연결 정보 채우기
for i in range(1, N + 1):
    line = input()
    for j in range(1, M + 1):
        map_[i][j] = line[j - 1]

# ✅ 2. dfs(재귀함수) 호출
answer = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if map_[i][j] != "":
            dfs(i, j)
            answer += 1

# ✅ 3. 정답 출력
print(answer)
