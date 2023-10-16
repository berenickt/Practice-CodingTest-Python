### 실버2 📚 https://www.acmicpc.net/problem/24479
"""
정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우
노드의 방문 순서를 출력

문제 키워드 찾기: 정점, 간선, 무방향 그래프, 노드의 방문순서, 오름차순
N : 정점의 수
M : 간선의 수
R : 시작정점

cf. 그래프를 10만 x 10만 = 100억짜리 배열을 만들면, 비효율적
그래서 매번 정적으로 무조건 크게 만드는게 아니라 필요할 때마다 쓰는 "동적할당"을 사용
빈 리스트에 apeend로 추가 
(2차원 배열 vs 빈 리스트, 고민하기 싫으면 빈 리스트로 통일)

그리고 오름차순으로 정렬하는 이유는?
1번 노드를 기준으로 누구를 방문해야 될지 찾을 떄, 가장 앞에 있는 녀석만 찾아도 된다
"""
### 성능이 더 빠른 input을 쓰기 위한 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx):
    global visited, graph, answer, order
    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)


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

# ✅ 2. 오름차순 정렬
for i in range(1, N + 1):
    graph[i] = sorted(graph[i])

# ✅ 3. dfs(재귀함수) 호출
dfs(R)

# ✅ 4. 정답 출력
for i in range(1, N + 1):
    print(answer[i])
