# 💡 다리 만들기 📚 https://www.acmicpc.net/problem/2146
from collections import deque

n = int(input())  # 미로의 크기를 입력받음
a = [list(map(int, input().split())) for _ in range(n)]  # 미로 정보를 입력받아 2차원 배열로 저장
g = [[0] * n for _ in range(n)]  # 그룹 정보를 저장할 배열 초기화
d = [[0] * n for _ in range(n)]  # 거리 정보를 저장할 배열 초기화
cnt = 0  # 그룹 번호 초기화

dx = [0, 0, 1, -1]  # 이동 방향을 나타내는 배열
dy = [1, -1, 0, 0]

# DFS를 사용하여 미로를 그룹화하고 그룹 정보를 저장
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and g[i][j] == 0:
            cnt += 1
            g[i][j] = cnt
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny] == 1 and g[nx][ny] == 0:
                            g[nx][ny] = cnt
                            q.append((nx, ny))

q = deque()
for i in range(n):
    for j in range(n):
        d[i][j] = -1
        if a[i][j] == 1:
            q.append((i, j))
            d[i][j] = 0

# BFS를 사용하여 거리 정보와 그룹 정보를 업데이트
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                g[nx][ny] = g[x][y]
                q.append((nx, ny))

ans = -1  # 정답 초기화

# 각 그룹의 가장자리 셀을 확인하며 최대 거리를 찾음
for i in range(n):
    for j in range(n):
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < n and 0 <= y < n:
                if g[i][j] != g[x][y]:
                    if ans == -1 or ans > d[i][j] + d[x][y]:
                        ans = d[i][j] + d[x][y]

print(ans)  # 정답 출력
