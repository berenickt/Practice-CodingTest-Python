# 💡 DFS와 BFS 📚 https://www.acmicpc.net/problem/1260
from collections import deque

# 입력: 정점 개수 n, 간선 개수 m, 시작 정점 start
n, m, start = map(int, input().split())

# 간선 정보를 저장할 리스
edges = []

# 정점 방문 여부를 저장할 리스트
check = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))  # 양방향 간선 정보 저장
    edges.append((v, u))

m *= 2  # 양방향 간선이므로 간선 수를 2배로 계산
edges.sort()  # 간선을 정렬
cnt = [0] * (n + 1)

# 각 정점에 연결된 간선의 개수를 계산
for u, v in edges:
    cnt[u] += 1

# 누적 합을 구하여 정점마다 간선 리스트의 시작과 끝 인덱스를 계산
for i in range(1, n + 1):
    cnt[i] += cnt[i - 1]


def dfs(x):
    global check
    check[x] = True
    print(x, end=" ")  # 현재 정점 출력
    for i in range(cnt[x - 1], cnt[x]):
        y = edges[i][1]
        if check[y] == False:
            dfs(y)  # 방문하지 않은 인접 정점 재귀 호출


def bfs(start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=" ")  # 현재 정점 출력
        for i in range(cnt[x - 1], cnt[x]):
            y = edges[i][1]
            if check[y] == False:
                check[y] = True
                q.append(y)


dfs(start)  # DFS 시작
print()
bfs(start)  # BFS 시작
print()
