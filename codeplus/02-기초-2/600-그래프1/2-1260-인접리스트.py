# 💡 DFS와 BFS 📚 https://www.acmicpc.net/problem/1260
from collections import deque

# 입력: 정점 개수 n, 간선 개수 m, 시작 정점 start
n, m, start = map(int, input().split())

# 인접 리스트를 통해 그래프 정보 저장
a = [[] for _ in range(n + 1)]

# 정점 방문 여부를 저장할 리스트
check = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)  # 양방향 간선 정보 저장
    a[v].append(u)

# 각 정점에 연결된 정점들을 오름차순으로 정렬
for i in range(1, n + 1):
    a[i].sort()


def dfs(x):
    global check
    check[x] = True  # 현재 정점을 방문했음을 표시
    print(x, end=" ")  # 현재 정점 출력
    for y in a[x]:
        if check[y] == False:
            dfs(y)  # 방문하지 않은 인접 정점 재귀 호출


def bfs(start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)  # 시작 정점을 큐에 삽입
    check[start] = True  # 시작 정점 방문 여부 표시
    while q:
        x = q.popleft()  # 큐에서 정점을 꺼내서 출력
        print(x, end=" ")
        for y in a[x]:
            if check[y] == False:
                check[y] = True  # 방문한 정점을 표시하고 큐에 삽입
                q.append(y)


dfs(start)  # DFS 시작
print()
bfs(start)  # BFS 시작
print()
