# 💡 이분 그래프 📚 https://www.acmicpc.net/problem/1707
import sys

sys.setrecursionlimit(1000000)  # 재귀 깊이 제한 설정
t = int(sys.stdin.readline())  # 테스트 케이스 개수 입력

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())  # 정점의 개수와 간선의 개수 입력
    a = [[] for _ in range(n)]  # 인접 리스트 초기화
    color = [0] * n  # 정점의 색상 정보를 저장하는 리스트 초기화

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())  # 간선의 양 끝점 입력
        a[u - 1].append(v - 1)  # 양방향 간선으로 인접 리스트에 추가
        a[v - 1].append(u - 1)

    # 깊이 우선 탐색 (DFS) 함수 정의
    def dfs(x, c):
        color[x] = c  # 현재 정점을 색상 c로 칠함
        for y in a[x]:  # 현재 정점과 연결된 이웃 정점들을 순회
            if color[y] == 0:  # 이웃 정점이 아직 색칠되지 않았다면
                dfs(y, 3 - c)  # 이웃 정점을 반대 색으로 칠하고 재귀 호출

    ans = True  # 이분 그래프인지 여부를 저장하는 변수 초기화
    for i in range(n):
        if color[i] == 0:  # 아직 색칠되지 않은 정점이 있다면
            dfs(i, 1)  # 해당 정점부터 DFS 탐색을 시작하고 색상 1로 칠함

    for i in range(n):
        for j in a[i]:
            if color[i] == color[j]:  # 인접한 정점끼리 색상이 같다면
                ans = False  # 이분 그래프가 아님

    print("YES" if ans else "NO")  # 결과 출력
