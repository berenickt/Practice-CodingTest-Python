# 💡 알고스팟 📚 https://www.acmicpc.net/problem/1261
from collections import deque

# 상하좌우 이동을 위한 dx, dy 배열 초기화
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 입력 받기
m, n = map(int, input().split())  # 가로, 세로 크기 입력
a = [list(map(int, list(input()))) for _ in range(n)]  # 미로 정보 입력

# 거리 정보를 저장할 2차원 배열 초기화
dist = [[-1] * m for _ in range(n)]

# 큐 생성 및 시작 위치 초기화
q = deque()
next_queue = deque()
q.append((0, 0))  # 시작 위치 (0, 0)
dist[0][0] = 0  # 시작 위치의 거리는 0으로 설정

while q:
    x, y = q.popleft()  # 큐에서 현재 위치 꺼내기
    for k in range(4):  # 상하좌우 이동을 위한 반복문
        nx, ny = x + dx[k], y + dy[k]  # 이동할 다음 위치 계산
        if 0 <= nx < n and 0 <= ny < m:  # 미로 범위 내에서만 처리
            if dist[nx][ny] == -1:  # 아직 방문하지 않은 위치라면
                if a[nx][ny] == 0:  # 이동 가능한 위치인 경우
                    dist[nx][ny] = dist[x][y]  # 거리 정보 업데이트 (이동하지 않았으므로 거리 그대로)
                    q.append((nx, ny))  # 다음 위치를 큐에 추가
                else:  # 벽(1)인 경우
                    dist[nx][ny] = dist[x][y] + 1  # 거리 정보 업데이트 (벽을 한 번 뚫었으므로 거리 +1)
                    next_queue.append((nx, ny))  # 다음 위치를 다음 큐에 추가

    if not q:  # 현재 큐가 비었다면 (다음 큐로 교체)
        q = next_queue
        next_queue = deque()

print(dist[n - 1][m - 1])  # 목표 위치까지의 최단 거리 출력
