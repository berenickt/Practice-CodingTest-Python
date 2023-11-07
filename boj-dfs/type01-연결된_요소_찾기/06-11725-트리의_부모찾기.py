### 실버2 📚 https://www.acmicpc.net/problem/11725
"""
루트 없는 트리가 주어진다.
이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램

cf. 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력

input #1 
7
1 6
6 3
3 5
4 1
2 4
4 7

output #1
4
6
1
3
1
4
"""
### 성능이 더 빠른 input을 쓰기 위한 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx):
    global visited, graph, answer
    visited[idx] = True

    for next in graph[idx]:
        if not visited[next]:
            answer[next] = idx
            dfs(next)


# ✅ 0. 입력 및 초기화
N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = [0] * (N + 1)

# ✅ 1. graph에 연결 정보 채우기
for _ in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# ✅ 2. dfs(재귀함수) 호출
dfs(1)

# ✅ 3. 정답 출력
for i in range(2, N + 1):
    print(answer[i])
