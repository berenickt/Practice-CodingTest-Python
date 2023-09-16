# 💡 토마토 📚 https://www.acmicpc.net/problem/7576
from collections import deque

dx = [0, 0, 1, -1]  # 상하좌우 방향
dy = [1, -1, 0, 0]  # 상하좌우 방향

m, n = map(int, input().split())  # 입력: 열과 행의 크기 m, n
a = [list(map(int, input().split())) for _ in range(n)]  # 입력: 2차원 배열 a
q = deque()  # 큐 초기화
dist = [[-1] * m for _ in range(n)]  # 거리 정보를 저장하는 2차원 배열 초기화

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:  # 익은 토마토인 경우
            dist[i][j] = 0  # 거리를 0으로 설정
            q.append((i, j))  # 큐에 시작 위치 추가

while q:
    x, y = q.popleft()  # 큐에서 위치 꺼내기
    for k in range(4):  # 상하좌우 방향에 대해서
        nx, ny = x + dx[k], y + dy[k]  # 새로운 위치 계산
        if 0 <= nx < n and 0 <= ny < m:  # 범위 내에 있는지 확인
            if a[nx][ny] == 0 and dist[nx][ny] == -1:  # 안 익은 토마토이고, 아직 방문하지 않았다면
                q.append((nx, ny))  # 새로운 위치를 큐에 추가
                dist[nx][ny] = dist[x][y] + 1  # 거리 정보 업데이트

ans = max([max(row) for row in dist])  # 최대 거리를 찾기 위해 2차원 배열에서 최댓값 찾기

for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and dist[i][j] == -1:  # 안 익은 토마토에 도달할 수 없는 경우
            ans = -1  # 결과를 -1로 설정

print(ans)  # 결과 출력
