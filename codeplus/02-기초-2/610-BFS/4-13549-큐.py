# 💡 숨바꼭질 3 📚 https://www.acmicpc.net/problem/13549
from collections import deque

MAX = 200000  # 최대값 상수 설정
check = [False] * MAX  # 방문 여부를 저장하는 배열 초기화
dist = [-1] * MAX  # 거리 정보를 저장하는 배열 초기화
n, m = map(int, input().split())  # n과 m을 입력으로 받음
check[n] = True  # 시작 지점을 방문 처리
dist[n] = 0  # 시작 지점의 거리를 0으로 초기화
q = deque()  # 큐 생성
next_queue = deque()  # 다음 단계의 큐 생성
q.append(n)  # 시작 지점을 큐에 추가

while q:
    now = q.popleft()  # 큐에서 현재 위치를 꺼냄
    if now * 2 < MAX and check[now * 2] == False:  # 현재 위치를 이중으로 증가시키는 경우
        q.append(now * 2)  # 다음 위치를 큐에 추가
        check[now * 2] = True  # 다음 위치를 방문 처리
        dist[now * 2] = dist[now]  # 거리 정보 업데이트 (이동하지 않았으므로 거리는 그대로)
    if now - 1 >= 0 and check[now - 1] == False:  # 현재 위치를 1 감소시키는 경우
        next_queue.append(now - 1)  # 다음 위치를 다음 단계 큐에 추가
        check[now - 1] = True  # 다음 위치를 방문 처리
        dist[now - 1] = dist[now] + 1  # 거리 정보 업데이트 (1 만큼 이동했으므로 거리 +1)
    if now + 1 < MAX and check[now + 1] == False:  # 현재 위치를 1 증가시키는 경우
        next_queue.append(now + 1)  # 다음 위치를 다음 단계 큐에 추가
        check[now + 1] = True  # 다음 위치를 방문 처리
        dist[now + 1] = dist[now] + 1  # 거리 정보 업데이트 (1 만큼 이동했으므로 거리 +1)
    if not q:
        q = next_queue  # 현재 큐가 비었다면 다음 단계의 큐로 교체
        next_queue = deque()

print(dist[m])  # 목표 위치까지의 최소 거리 출력
