# 💡 DFS와 BFS 📚 https://www.acmicpc.net/problem/1260
from collections import deque

# 정점의 개수, 간선의 개수, 시작 정점 입력
n, m, start = map(int, input().split())
a = [[] for _ in range(n + 1)]  # 인접 리스트 초기화

# 간선 정보 입력받기
for _ in range(m):
    u, v = map(int, input().split())  # 간선의 양 끝점 입력
    a[u].append(v)  # 양방향 간선으로 인접 리스트에 추가
    a[v].append(u)  # 양방향 간선으로 인접 리스트에 추가

# 각 정점의 이웃 정점을 정렬
for i in range(1, n + 1):
    a[i].sort()


# 깊이 우선 탐색 (DFS) 함수 정의
def dfs(node):
    check = [False] * (n + 1)  # 방문 여부를 저장하는 리스트 초기화
    stack = []  # 스택을 활용한 DFS를 위한 리스트 초기화
    stack.append((node, 0))  # 시작 노드와 시작 인덱스를 스택에 추가
    check[node] = True  # 시작 노드를 방문 처리
    print(node, end=" ")  # 시작 노드 출력
    while stack:
        x, start = stack.pop()  # 현재 노드와 시작 인덱스 가져오기
        for i in range(start, len(a[x])):  # 현재 노드의 이웃 노드 순회
            y = a[x][i]  # 이웃 노드 y
            if check[y] == False:  # 이웃 노드가 아직 방문되지 않았다면
                print(y, end=" ")  # 이웃 노드 출력
                check[y] = True  # 이웃 노드를 방문 처리
                stack.append((x, i + 1))  # 현재 노드와 다음 인덱스를 스택에 추가
                stack.append((y, 0))  # 이웃 노드와 시작 인덱스를 스택에 추가
                break


# 너비 우선 탐색 (BFS) 함수 정의
def bfs(start):
    check = [False] * (n + 1)  # 방문 여부를 저장하는 리스트 초기화
    q = deque()  # 큐를 활용한 BFS를 위한 덱 초기화
    q.append(start)  # 시작 노드를 큐에 추가
    check[start] = True  # 시작 노드를 방문 처리
    while q:
        x = q.popleft()  # 큐에서 노드 하나를 꺼내기
        print(x, end=" ")  # 꺼낸 노드 출력
        for y in a[x]:  # 현재 노드의 이웃 노드 순회
            if check[y] == False:  # 이웃 노드가 아직 방문되지 않았다면
                check[y] = True  # 이웃 노드를 방문 처리
                q.append(y)  # 이웃 노드를 큐에 추가


# DFS 호출하여 시작
dfs(start)
print()  # 줄 바꿈
# BFS 호출하여 시작
bfs(start)
print()  # 줄 바꿈
