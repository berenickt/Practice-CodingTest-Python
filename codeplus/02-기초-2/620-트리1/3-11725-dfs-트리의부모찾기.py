# 💡 트리의 부모 찾기 📚 https://www.acmicpc.net/problem/11725
import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 설정
n = int(sys.stdin.readline())  # 노드 개수 입력

graph = [[] for i in range(n + 1)]  # 노드 연결 정보를 저장할 리스트 초기화

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())  # 연결된 노드 정보 입력
    graph[a].append(b)  # 양방향 연결
    graph[b].append(a)

visited = [0] * (n + 1)  # 방문 여부를 저장할 리스트 초기화

arr = []  # 결과를 저장할 리스트 초기화


def dfs(s):
    for i in graph[s]:  # 현재 노드와 연결된 노드들에 대해서
        if visited[i] == 0:  # 아직 방문하지 않은 경우
            visited[i] = s  # 방문 표시 및 부모 노드 기록
            dfs(i)  # 재귀적으로 방문


dfs(1)  # 루트 노드인 1부터 DFS 탐색 시작

for x in range(2, n + 1):  # 2부터 n까지 순회하며 부모 노드 출력
    print(visited[x])
