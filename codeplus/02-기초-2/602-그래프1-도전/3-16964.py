# 💡 DFS 스페셜 저지 📚 https://www.acmicpc.net/problem/16964
from collections import deque

n = int(input())  # 노드 개수 입력
a = [[] for _ in range(n)]  # 빈 인접 리스트 초기화

for _ in range(n - 1):
    u, v = map(int, input().split())  # 간선 정보 입력
    u -= 1  # 1부터 시작하는 인덱스를 0부터 시작하는 인덱스로 변경
    v -= 1  # 1부터 시작하는 인덱스를 0부터 시작하는 인덱스로 변경
    a[u].append(v)  # 양방향 간선 추가
    a[v].append(u)  # 양방향 간선 추가

b = list(map(int, input().split()))  # 방문 순서 입력
b = [x - 1 for x in b]  # 1부터 시작하는 인덱스를 0부터 시작하는 인덱스로 변경
order = [0] * n

for i in range(n):
    order[b[i]] = i  # 방문 순서를 인덱스로 역순으로 저장

for i in range(n):
    a[i].sort(key=lambda x: order[x])  # 인접 리스트를 방문 순서에 따라 정렬

dfs_order = []  # DFS 순서를 저장하는 리스트
check = [False] * n  # 노드 방문 여부를 저장하는 배열 초기화


def dfs(x):
    if check[x]:  # 이미 방문한 노드인 경우 종료
        return
    dfs_order.append(x)  # DFS 순서에 노드 추가
    check[x] = True  # 노드 방문 처리
    for y in a[x]:
        dfs(y)  # 재귀적으로 인접한 노드를 방문


dfs(0)  # DFS 탐색 시작
ok = True  # 순서가 일치하는지 여부를 저장하는 변수 초기화

for i in range(n):
    if dfs_order[i] != b[i]:  # DFS 순서와 방문 순서가 일치하지 않는 경우
        ok = False  # 순서가 일치하지 않음을 표시

print(1 if ok else 0)  # 순서가 일치하는 경우 1 출력, 그렇지 않으면 0 출력
