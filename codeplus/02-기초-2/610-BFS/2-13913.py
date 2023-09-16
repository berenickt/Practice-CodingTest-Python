# 💡 숨바꼭질 4 📚 https://www.acmicpc.net/problem/13913
from collections import deque
import sys

MAX = 200000  # 최대 범위 설정
sys.setrecursionlimit(MAX)  # 재귀 깊이 제한 설정
check = [False] * MAX  # 방문 여부를 나타내는 배열 초기화
dist = [-1] * MAX  # 거리 정보를 나타내는 배열 초기화
via = [-1] * MAX  # 이동 경로를 저장하는 배열 초기화
n, m = map(int, input().split())  # 시작점과 목표점을 입력받음
check[n] = True  # 시작점을 방문했다고 표시
dist[n] = 0  # 시작점까지의 거리는 0으로 초기화
q = deque()
q.append(n)

while q:
    now = q.popleft()  # 현재 위치를 큐에서 꺼냄
    if now - 1 >= 0 and not check[now - 1]:  # 현재 위치에서 이동할 수 있는 왼쪽 위치 확인
        q.append(now - 1)  # 큐에 추가하여 다음에 탐색할 수 있도록 함
        check[now - 1] = True  # 방문했다고 표시
        dist[now - 1] = dist[now] + 1  # 거리를 업데이트
        via[now - 1] = now  # 경로를 저장
    if now + 1 < MAX and not check[now + 1]:  # 현재 위치에서 이동할 수 있는 오른쪽 위치 확인
        q.append(now + 1)  # 큐에 추가하여 다음에 탐색할 수 있도록 함
        check[now + 1] = True  # 방문했다고 표시
        dist[now + 1] = dist[now] + 1  # 거리를 업데이트
        via[now + 1] = now  # 경로를 저장
    if now * 2 < MAX and not check[now * 2]:  # 현재 위치에서 이동할 수 있는 2배 위치 확인
        q.append(now * 2)  # 큐에 추가하여 다음에 탐색할 수 있도록 함
        check[now * 2] = True  # 방문했다고 표시
        dist[now * 2] = dist[now] + 1  # 거리를 업데이트
        via[now * 2] = now  # 경로를 저장

print(dist[m])  # 목표점까지의 최단 거리 출력


def go(n, m):
    if n != m:
        go(n, via[m])  # 경로를 따라 거꾸로 이동하여 출력
    print(m, end=" ")


go(n, m)  # 시작점부터 목표점까지의 경로 출력
