### 실버2 📚 https://www.acmicpc.net/problem/24479
"""
정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우
노드의 방문 순서를 출력

문제 키워드 찾기: 정점, 간선, 무방향 그래프, 노드의 방문순서, 오름차순
N : 정점의 수
M : 간선의 수
R : 시작정점
"""


def dfs(idx):
    global visited, graph, answer, order
    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)


### 성능이 더 빠른 input을 쓰기 위한 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# ✅ 0. 입력 및 초기화
N, M, R = map(int, input().split())
MAX = 100000 + 10
graph = [[] for _ in range(N + 1)]
visited = [False] * MAX
answer = [0] * MAX
order = 1

# ✅ 1. graph에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# ✅ 2. dfs(재귀함수) 호출
dfs(R)

# ✅ 3. 정답 출력
for i in range(1, N + 1):
    print(answer[i])
