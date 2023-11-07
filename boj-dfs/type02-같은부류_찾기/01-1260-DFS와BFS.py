### 실버3 📚 https://www.acmicpc.net/problem/1260
"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램
단, 방문할 수 있는 정점이 여러 개인 경우에는 
정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.

cf.
첫째 줄에 
정점의 개수 N(1 ≤ N ≤ 1,000), 
간선의 개수 M(1 ≤ M ≤ 10,000), 
탐색을 시작할 정점의 번호 V가 주어진다. 

다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다

input #1
4 5 1
1 2
1 3
1 4
2 4
3 4

output #1
1 2 4 3
1 2 3 4
"""
### 성능이 더 빠른 input을 쓰기 위한 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx):
    visited[idx] = True
    print(idx, end=" ")

    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


def bfs():
    queue = []

    queue.append(V)
    visited[V] = True

    while queue:
        idx = queue.pop(0)
        print(idx, end=" ")

        for i in range(1, N + 1):
            if not visited[i] and graph[idx][i]:
                queue.append(i)
                visited[i] = True


# ✅ 0. 입력 및 초기화
N, M, V = map(int, input().split())
MAX = 1000 + 10
graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * MAX

# ✅ 1. graph에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

# ✅ 2. dfs(재귀함수) 호출
dfs(V)
print()

# ✅ 3. bfs 호출
visited = [False] * MAX
bfs()
