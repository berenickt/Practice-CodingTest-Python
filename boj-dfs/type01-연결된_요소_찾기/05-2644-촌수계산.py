### 실버2 📚 https://www.acmicpc.net/problem/2644
"""
여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 
주어진 두 사람의 촌수를 계산하는 프로그램

e.g. 나와 아버지, 아버지와 할아버지는 각각 1촌으
나와 할아버지는 2촌이 되고, 
아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌

문제 키워드 찾기: 부모 자식들 간의 관계, 두 사람의 촌수 계산
N : 사람들의 번호(1 <= N <= 100)
M : 부모 자식들 간의 관계의 개수

cf.
9 # 전체 사람 수
7 3 # 촌수를 계산해야 하는 서로 다른 두사람의 번호
7 # 부모 자식들 간의 관계의 개수
1 2 # 부모 자식간의 관계
1 3
2 7
2 8
2 9
4 5
4 6
"""
### 성능이 더 빠른 input을 쓰기 위한 3줄
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx, count):
    global visited, graph, end, answer
    visited[idx] = True
    if idx == end:
        answer = count
        return

    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i, count + 1)


# ✅ 0. 입력 및 초기화
N = int(input())
start, end = map(int, input().split())
M = int(input())
MAX = 100 + 10
graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * MAX
answer = -1

# ✅ 1. graph에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[y][x] = True
    graph[x][y] = True


# ✅ 2. dfs(재귀함수) 호출
dfs(start, 0)

# ✅ 3. 정답 출력
print(answer)
