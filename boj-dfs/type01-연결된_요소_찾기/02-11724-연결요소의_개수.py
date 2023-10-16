### 실버2 📚 https://www.acmicpc.net/problem/11724
"""
방향 없는 그래프가 주어졌을 때,
연결 요소 (Connected Component)의 개수를 구하는 프로그램

📌 cf. 방향없는 그래프
가장 일반적인 형태의 그래프
1 -> 2로 갈수도 있고, 2 -> 1로 갈수도 있음

📌 cf. 방향있는 그래프 => 길을 생각했을 때, 일반통행의 그래프
1 -> 2로만 갈 수 있음

📌cf. 연결요소 : 선으로 연결되어 나누어진 각각의 그래프

문제 키워드 찾기: 연결요소의 개수 => DFS/BFS
N : 정점의 개수
M : 간선의 개수

1번 문제와 차이점은 어디에서 DFS를 시작할까이다.
DFS 유형의 쉬운문제는 보통 1번부터 시작하지만,
살짝 꼬운 것들은 1번이 아닌 n번, 즉 문제에서 주어지는 그 요소부터 시작하라는 식입니다.
"""
### 성능이 더 빠른 input을 쓰기 위한 아래 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx):
    global visited, graph
    visited[idx] = True  # idx번쨰 노드를 이미 방문했으니 다시 방문못하도록 막기

    # i번을 방문하지 않았고, 개가 나랑 연결되어 있으면, dfs 재귀호출
    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


# ✅ 0. 입력 및 초기화
MAX = 1000 + 10  # 문제의 최대값 1000에 여유분 10
N, M = map(int, input().split())
graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * MAX
answer = 0

# ✅ 1. graph에 연결 정보 채우기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True


# ✅ 2. dfs(재귀함수) 호출
# 저번 문제는 1번과 연결된 게 누구인지 찾는 것이었다면
# 이번 문제는 연결되어 있는 요소의 묶음이 몇 개인지 visited배열이 모두 true가 되기까지 계속 순회
for i in range(1, N + 1):
    # 방문된 적이 없으면, dfs 호출
    if not visited[i]:
        dfs(i)
        answer += 1

# ✅ 3. 정답 출력
print(answer)
