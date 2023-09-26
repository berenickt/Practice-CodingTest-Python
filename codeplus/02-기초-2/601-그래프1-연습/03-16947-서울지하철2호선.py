# 💡 서울 지하철 2호선 📚 https://www.acmicpc.net/problem/16947
from collections import deque
import sys

sys.setrecursionlimit(1000000)
n = int(input())  # 노드 개수 입력
a = [[] for _ in range(n)]  # 빈 인접 리스트 초기화

for _ in range(n):
    u, v = map(int, input().split())  # 간선 정보 입력
    u -= 1  # 1부터 시작하는 인덱스를 0부터 시작하는 인덱스로 변경
    v -= 1  # 1부터 시작하는 인덱스를 0부터 시작하는 인덱스로 변경
    a[u].append(v)  # 양방향 간선 추가
    a[v].append(u)  # 양방향 간선 추가

check = [0] * n  # 노드의 방문 여부 및 사이클 여부를 저장하는 배열 초기화
# 0: 방문하지 않음, 1: 방문했으나 사이클에 속하지 않음, 2: 방문하며 사이클에 속함


def go(x, p):
    # -2: 사이클 발견하였으나 포함되지 않음
    # -1: 사이클을 찾지 못함
    # 0~n-1: 사이클 발견하였으며 시작 인덱스

    if check[x] == 1:  # 이미 방문한 노드인 경우
        return x

    check[x] = 1  # 노드 방문 처리
    for y in a[x]:
        if y == p:  # 부모 노드로 되돌아가는 경우는 건너뛰기
            continue
        res = go(y, x)  # 재귀 호출
        if res == -2:
            return -2
        if res >= 0:
            check[x] = 2
            if x == res:  # 현재 노드가 사이클의 시작 노드인 경우
                return -2  # 사이클에 속하지 않음
            else:
                return res  # 사이클의 시작 노드 인덱스 반환
    return -1  # 사이클을 찾지 못한 경우


go(0, -1)  # DFS를 통해 사이클 여부 확인

q = deque()  # 큐 초기화
dist = [-1] * n  # 거리 정보를 저장하는 배열 초기화

for i in range(n):
    if check[i] == 2:  # 사이클에 속한 노드인 경우
        dist[i] = 0  # 거리 초기화
        q.append(i)  # 큐에 시작 노드 추가
    else:
        dist[i] = -1  # 사이클에 속하지 않은 노드의 거리 초기화

while q:
    x = q.popleft()  # 큐에서 노드 꺼내기
    for y in a[x]:
        if dist[y] == -1:  # 아직 방문하지 않은 노드인 경우
            q.append(y)  # 큐에 추가
            dist[y] = dist[x] + 1  # 거리 정보 업데이트

print(*dist, sep=" ")  # 결과 출력
