# 💡 ABCDE 📚 https://www.acmicpc.net/problem/13023
import sys

# 입력: 노드 수 n, 간선 수 m
n, m = map(int, input().split())

# 간선 정보를 저장할 리스트
edges = []

# 인접 행렬을 통해 연결 관계를 나타내는 이차원 리스트
a = [[False] * n for _ in range(n)]

# 인접 리스트를 통해 각 노드에 연결된 노드를 저장하는 리스트
g = [[] for _ in range(n)]

# 간선 정보 입력 및 그래프 정보 초기화
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    edges.append((v, u))
    a[u][v] = a[v][u] = True
    g[u].append(v)
    g[v].append(u)
m *= 2  # 양방향 간선이므로 간선 수를 2배로 계산

for i in range(m):
    for j in range(m):
        A, B = edges[i]  # 현재 간선 (A, B)
        C, D = edges[j]  # 현재 간선 (C, D)

        # 서로 다른 노드들 간의 조건 확인
        # A, B, C, D 중 하나라도 같다면 스킵
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue

        # B와 C 사이에 간선이 없다면 스킵
        if not a[B][C]:
            continue
        for E in g[D]:
            # A, B, C, D, E 중 하나라도 같다면 스킵
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            sys.exit(0)  # 조건을 만족하는 경우 1 출력 후 종료

print(0)  # 조건을 만족하는 경우가 없으면 0 출력
