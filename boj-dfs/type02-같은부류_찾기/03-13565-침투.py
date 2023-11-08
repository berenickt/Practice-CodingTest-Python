### 실버2 📚 https://www.acmicpc.net/problem/13565
"""
전류가 침투(percolate) 할 수 있는 섬유 물질을 개발하고 있다.
이 섬유 물질은 2차원 M x N 격자로 표현될 수 있다. 
편의상 2차원 격자의 위쪽을 바깥쪽(outer side),
아래쪽을 안쪽(inner side)라고 생각하기로 한다. 

또한 각 격자는 검은색 아니면 흰색인데, 
- 검은색(1)은 전류를 차단하는 물질임을 뜻하고, 
- 흰색(0)은 전류가 통할 수 있는 물질임을 뜻한다. 
- cf. 그림의 파란색은 전기를 의미

전류는 섬유 물질의 가장 바깥쪽(out side) 흰색 격자들에 공급되고, 
이후에는 상하좌우로 인접한 흰색 격자들로 전달될 수 있다.

김 교수가 개발한 섬유 물질을 나타내는 정보가 2차원 격자 형태로 주어질 때, 
바깥쪽에서 흘려 준 전류가 안쪽까지 침투될 수 있는지 아닌지를 판단하는 프로그램

cf.
첫 줄에 격자의 크기를 나타내는  M(행), N(열)이 주어짐
그 다음에는 0과 1로 이루어진 격자 정보

input #1
5 6
010101
010000
011101
100011
001011

output #1
NO
"""

# 성능이 더 빠른 input을 쓰기 위한 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 상하좌우
dirY = [-1, 1, 0, 0]  # 상하
dirX = [0, 0, -1, 1]  # 좌우


def dfs(y, x):
    global visited, map_, answer, M  # M(행)
    visited[y][x] = True  # y(행), x(열)

    if y == M:
        answer = True
        return

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if map_[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)


# ✅ 0. 입력 및 초기화
M, N = map(int, input().split())  # M(행), N(열)
MAX = 1000 + 10

# 1010(행) x 1010(열)의 False 2차원 배열
map_ = [[False] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]

# ✅ 1. map에 연결 정보 채우기
for i in range(1, M + 1):  # 1 ~ M(행)까지
    row = input()
    for j in range(1, N + 1):  # 1 ~ N(열)까지
        map_[i][j] = row[j - 1] == "0"  # 행의 원소가 0이면 True

# ✅ 2. dfs(재귀함수) 호출
answer = False
for j in range(1, N + 1):  # 1 ~ N(열)까지
    if map_[1][j]:  # 1행과 j번째 열 원소가 참(True, 0)이면,
        dfs(1, j)


# ✅ 3. 정답 출력
print("YES" if answer else "NO")
