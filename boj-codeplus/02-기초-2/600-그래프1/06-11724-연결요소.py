# 💡 연결 요소 📚 https://www.acmicpc.net/problem/11724
import sys

sys.setrecursionlimit(100000)  # 재귀 깊이 제한 설정

n, m = map(int, input().split())  # 정점의 개수와 간선의 개수 입력
a = [[] for _ in range(n)]  # 인접 리스트 초기화
check = [False] * (n)  # 정점 방문 여부를 저장하는 리스트 초기화

for _ in range(m):
    u, v = map(int, input().split())  # 간선의 양 끝점 입력
    a[u - 1].append(v - 1)  # 양방향 간선으로 인접 리스트에 추가
    a[v - 1].append(u - 1)


# 깊이 우선 탐색 (DFS) 함수 정의
def dfs(x):
    check[x] = True  # 현재 정점 방문 처리
    for y in a[x]:  # 현재 정점과 연결된 이웃 정점들을 순회
        if check[y] == False:  # 이웃 정점이 아직 방문되지 않았다면
            dfs(y)  # 이웃 정점을 DFS로 재귀 호출


ans = 0  # 연결 요소 개수를 저장하는 변수 초기화
for i in range(n):
    if not check[i]:  # 아직 방문되지 않은 정점이 있다면
        dfs(i)  # 해당 정점부터 DFS 탐색 시작
        ans += 1  # 연결 요소 개수 증가
print(ans)  # 연결 요소 개수 출력
