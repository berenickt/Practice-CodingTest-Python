# 💡 트리의 지름 📚 https://www.acmicpc.net/problem/1167
import sys
from collections import deque

N = int(sys.stdin.readline())  # 노드 개수 입력
graph = [[] for i in range(N + 1)]  # 노드 연결 정보를 저장할 리스트 초기화

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())  # 연결된 노드 정보 입력
    graph[a].append(b)  # 양방향 연결
    graph[b].append(a)

queue = deque()
queue.append(1)  # 시작 노드를 큐에 추가

ans = [0] * (N + 1)  # 각 노드의 부모 노드를 저장할 리스트 초기화


def bfs():
    while queue:
        now = queue.popleft()  # 큐에서 현재 노드를 꺼냅니다.
        for nxt in graph[now]:  # 현재 노드와 연결된 노드들에 대해서
            if ans[nxt] == 0:  # 아직 부모 노드가 없는 경우
                ans[nxt] = now  # 현재 노드를 부모 노드로 설정
                queue.append(nxt)  # 다음 노드를 큐에 추가


bfs()  # 너비 우선 탐색 실행

res = ans[2:]  # 결과에서 첫 번째 원소(루트 노드) 제외

for x in res:
    print(x)  # 결과 출력
