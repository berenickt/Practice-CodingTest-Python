### 실버3 📚 https://www.acmicpc.net/problem/1012
"""
지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면, 
이 지렁이는 인접한 다른 배추로 이동할 수 있어, 
그 배추들 역시 해충으로부터 보호받을 수 있다. 
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 
서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면, 
총 몇 마리의 지렁이가 필요한지 알 수 있다

0은 배추가 심어져 있지 않은 땅이고,
1은 배추가 심어져 있는 땅을 나타낸다.

cf.
첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
그 다음 줄부터 각각의 테스트 케이스에 대해 
첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 
세로길이 N(1 ≤ N ≤ 50), 
그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다

input #1
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
"""
### 성능이 더 빠른 input을 쓰기 위한 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

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
    visited = [[False] * MAX for _ in range(MAX)]

    for _ in range(K):
        x, y = map(int, input().split())
        map_[y + 1][x + 1] = True

    # ✅ 2. dfs(재귀함수) 호출
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if map_[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1

# ✅ 3. bfs 호출
print(answer)
