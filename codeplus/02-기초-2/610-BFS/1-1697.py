# 💡 숨바꼭질 📚 https://www.acmicpc.net/problem/1697
from collections import deque

MAX = 200000  # 최대 범위 설정
check = [False] * (MAX + 1)  # 방문 여부를 나타내는 배열 초기화
dist = [-1] * (MAX + 1)  # 거리 정보를 나타내는 배열 초기화
n, m = map(int, input().split())  # 시작점과 목표점을 입력받음
check[n] = True  # 시작점을 방문했다고 표시
dist[n] = 0  # 시작점까지의 거리는 0으로 초기화
q = deque()
q.append(n)

while q:
    now = q.popleft()  # 현재 위치를 큐에서 꺼냄
    for nxt in [now - 1, now + 1, now * 2]:  # 현재 위치에서 이동할 수 있는 경우를 나타내는 리스트 순회
        if 0 <= nxt <= MAX and check[nxt] == False:  # 범위 내에 있고 아직 방문하지 않은 경우
            check[nxt] = True  # 방문했다고 표시
            dist[nxt] = dist[now] + 1  # 거리를 업데이트
            q.append(nxt)  # 큐에 추가하여 다음에 탐색할 수 있도록 함

print(dist[m])  # 목표점까지의 최단 거리 출력
