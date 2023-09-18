# 💡 섬의 개수 📚 https://www.acmicpc.net/problem/4963
from collections import deque

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


# 너비 우선 탐색 (BFS) 함수 정의
def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    group[x][y] = cnt
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx, ny))
                    group[nx][ny] = cnt


while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    a = [list(map(int, input().split())) for _ in range(n)]
    group = [[0] * m for _ in range(n)]  # 그룹 정보를 저장하는 2차원 배열 초기화
    cnt = 0  # 그룹의 개수를 저장하는 변수 초기화
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and group[i][j] == 0:  # 육지이고 아직 그룹이 지정되지 않았다면
                cnt += 1  # 그룹 개수 증가
                bfs(i, j, cnt)  # BFS로 같은 그룹 결정

    print(cnt)  # 그룹의 개수 출력
