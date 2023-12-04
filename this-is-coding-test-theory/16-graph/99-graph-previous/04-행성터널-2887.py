# 📚 https://www.acmicpc.net/problem/2887
"""
때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었습니다.
왕국은 N개의 행성으로 이루어져 있습니다.
민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 합니다.
행성은 3차원 좌표 위의 한 점으로 생각하면 됩니다.
두 행성 A(Xa, Ya, Za)와 B(Xb, Yb, Zb)를 터널로 연결할 때 드는 비용은 min(|Xa - Xb|, |Ya - Yb|, |Za - Zb|)입니다.
민혁이는 터널을 총 N - 1개 건설해서 모든 행성이 서로 연결되게 하려고 합니다.
이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하세요

cf.
첫째 줄에 행성의 개수 N이 주어집니다. (1 <= N <= 100,000)
다음 N개 줄에는 각 행성의 x, y, z 좌표가 주어집니다.
모든 좌표 값은 -10의 9승보다 크거나 같고, 10의 9승보다 작거나 같은 정수입니다.
한 위치에 행성이 두 개 이상 있는 경우는 없습니다.

input #1
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19

output #1 모든 행성을 터널로 연결하는데 필요한 최소 비용
4
"""


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수 입력받기
n = int(input())
parent = [0] * (n + 1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

x = []
y = []
z = []

# 모든 노드에 대한 좌표 값 입력받기
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n - 1):
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
