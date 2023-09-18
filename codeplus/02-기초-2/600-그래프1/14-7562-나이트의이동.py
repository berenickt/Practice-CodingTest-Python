# 💡 나이트의 이동 📚 https://www.acmicpc.net/problem/7562
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]  # 나이트가 이동할 수 있는 모든 방향의 x 좌표 변화량
dy = [1, 2, 2, 1, -1, -2, -2, -1]  # 나이트가 이동할 수 있는 모든 방향의 y 좌표 변화량

t = int(input())  # 테스트 케이스 개수 입력

for _ in range(t):
    n = int(input())  # 체스판 크기 n 입력
    sx, sy = map(int, input().split())  # 시작 위치 (sx, sy) 입력
    ex, ey = map(int, input().split())  # 목표 위치 (ex, ey) 입력
    d = [[-1] * n for _ in range(n)]  # 거리 정보를 저장하는 2차원 배열 초기화
    q = deque()  # 큐 초기화
    q.append((sx, sy))  # 시작 위치 큐에 추가
    d[sx][sy] = 0  # 시작 위치의 거리는 0으로 설정

    while q:
        x, y = q.popleft()  # 큐에서 위치 꺼내기
        for k in range(8):  # 8방향에 대해서 이동 가능한 경우 확인
            nx, ny = x + dx[k], y + dy[k]  # 새로운 위치 계산
            if 0 <= nx < n and 0 <= ny < n:  # 체스판 범위 내에 있는지 확인
                if d[nx][ny] == -1:  # 아직 방문하지 않은 위치라면
                    d[nx][ny] = d[x][y] + 1  # 거리 정보 업데이트
                    q.append((nx, ny))  # 새로운 위치를 큐에 추가

    print(d[ex][ey])  # 목표 위치까지의 최단 거리 출력
