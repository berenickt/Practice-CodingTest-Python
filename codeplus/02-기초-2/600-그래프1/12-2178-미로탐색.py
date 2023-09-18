# 💡 미로 탐색 📚 https://www.acmicpc.net/problem/2178
from collections import deque

dx = [0, 0, 1, -1]  # 이동 방향: 오른쪽, 왼쪽, 아래, 위
dy = [1, -1, 0, 0]  # 이동 방향: 오른쪽, 왼쪽, 아래, 위

n, m = map(int, input().split())  # 입력: 행과 열의 크기 n, m
a = [list(map(int, list(input()))) for _ in range(n)]  # 입력: 2차원 배열 a
q = deque()  # 큐 초기화
check = [[False] * m for _ in range(n)]  # 방문 여부를 저장하는 2차원 배열 초기화
dist = [[0] * m for _ in range(n)]  # 거리 정보를 저장하는 2차원 배열 초기화

q = deque()
q.append((0, 0))  # 시작 위치 (0, 0)을 큐에 추가
check[0][0] = True  # 시작 위치 방문 처리
dist[0][0] = 1  # 시작 위치 거리 1로 설정

while q:
    x, y = q.popleft()  # 큐에서 위치 꺼내기
    for k in range(4):  # 상하좌우 방향에 대해서
        nx, ny = x + dx[k], y + dy[k]  # 새로운 위치 계산
        if 0 <= nx < n and 0 <= ny < m:  # 범위 내에 있는지 확인
            if check[nx][ny] == False and a[nx][ny] == 1:  # 아직 방문하지 않았고, 육지인 경우
                q.append((nx, ny))  # 새로운 위치를 큐에 추가
                dist[nx][ny] = dist[x][y] + 1  # 거리 정보 업데이트
                check[nx][ny] = True  # 새로운 위치 방문 처리

print(dist[n - 1][m - 1])  # 목적지까지의 최단 거리 출력
