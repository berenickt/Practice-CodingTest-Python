### 실버2 📚 https://www.acmicpc.net/problem/4963
"""
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 
섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 
한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

cf. 
입력은 여러 개의 테스트 케이스로 이루어져 있다. 
각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. 
w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
입력의 마지막 줄에는 0이 두 개 주어진다.

핵심키워드
섬의 개수,
가로, 세로 또는 대각선으로 연결
한 정사각형에서 다른 정사각형으로 갈 수 있는 경로
"""
"""
input #1
1 1       ===> testcase #1 - 1열 1행 => 0개
0
2 2       ===> testcase #2 - 2열 2행 => 1개
0 1
1 0
3 2       ===> testcase #3 - 3열 2행 => 1개
1 1 1
1 1 1
5 4       ===> testcase #4 - 5열 4행 => 3개
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4       ===> testcase #5 - 5열 4행 => 1개
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5       ===> testcase #6 - 5열 5행 => 9개
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
"""
# 성능이 더 빠른 input을 쓰기 위한 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

### 각각 x축, y축 방향으로 8개 방향
# 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dirY = [-1, -1, 0, 1, 1, 1, 0, -1]
dirX = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(y, x):
    global visited, map_
    visited[y][x] = True

    for i in range(8):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if map_[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)


# ✅ 0. 입력 및 초기화
while True:
    M, N = map(int, input().split())
    MAX = 50 + 10

    if N == 0 and M == 0:
        break

    # ✅ 1. map에 연결 정보 채우기
    map_ = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]

    for i in range(1, N + 1):
        row = list(map(int, input().split()))
        for j in range(1, M + 1):
            map_[i][j] = row[j - 1] == 1

    # ✅ 2. dfs(재귀함수) 호출
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if map_[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1

    # ✅ 3. 정답 출력
    print(answer)
