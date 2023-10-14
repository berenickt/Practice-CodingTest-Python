### 실버3 📚 https://www.acmicpc.net/problem/2606
"""
문제 키워드 찾기: 네트워크 상에서
이미 방문한 지점을 다시 방문하지 않으려면?

cf. input() : 문제에서 주어지는 정보 or 사람이 입력하는 정보를 string 형태로 받아옴
N : 컴퓨터의 수
M : 네트워크 상에 직접 연결되어 있는 컴퓨터 쌍의 수
"""


def dfs(idx):
    global visited, graph, answer  # 3개 변수를 참조
    visited[idx] = True
    answer += 1

    # i번쨰 노드 방문한 적 없고, 그래프 인덱스의 i번째가 true면,
    # (즉, i번쟤 노드가 나랑 연결되어 있다면)
    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


# ✅ 0. 입력 및 초기화
N = int(input())
M = int(input())

graph = [[False] * (N + 1) for _ in range(N + 1)]

# 한 행을 만든 것(0번 인덱스을 포함하기에 8개)
visited = [False] * (N + 1)
answer = 0


# ✅ 1. graph에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input.split())
    graph[x][y] = True
    graph[y][x] = True

# ✅ 2. dfs(재귀함수) 호출
dfs(1)

# ✅ 3. 정답 출력, (1번 컴퓨터 1개를 뺀 감연된 컴퓨터의 수)
print(answer - 1)
