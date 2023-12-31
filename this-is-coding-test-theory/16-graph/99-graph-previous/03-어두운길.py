"""
한 마을은 N개의 집과 M개의 도로로 구성되어 있습니다.
각 집은 0번부터 N - 1번까지의 번호로 구분됩니다.

모든 도로에는 가로등이 구비되어 있는데, 
특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일합니다.

예를 들어 2번 집과 3번 집 사이를 연결하는 길이가 7인 도로가 있다고 해봅시다.
하루동안 이 가로등을 켜기 위한 비용은 7이 됩니다.

정부에서는 일부 가로등을 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만을 절약하고자 합니다.
결과적으로 일부 가로등을 비활성화하여 최대한 많은 금액을 절약하고자 합니다.

마을의 집과 도로 정보가 주어졌을 때, 
일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성하세요.

cf.
첫째 줄에 집의 수 N(1 <= N <= 200,000)과 도로의 수 M(N-1 <= M <= 200,000)이 주어집니다.
다음 M개의 줄에 걸쳐서 각 도로에 대한 정보 X, Y, Z가 주어지며, 공백으로 구분합니다.(0 <= X, Y < N)
이는 X번 집과 Y번 집 사이에 양방향 도로가 있으며, 그 길이가 Z라는 의미입니다.
단, X와 Y가 동일한 경우는 없으며 마을을 구성하는 모든 도로의 길이 합은 2의 31제곱보다 작습니다.

input #1
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

output #1
51

Tip
주어진 입력을 통해서 그래프를 구성한 뒤에 크루스칼 알고리즘을 수행하면 된다.
다만, 문제에서 요구하는 정답은 '절약할 수 있는 최대 금액'이다.
그러므로 `전체 가로등을 켜는 비용 - 최소 신장 트리를 구성하는 비용`을 출력하면 정답
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


# 노드의 개수와 간선의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((z, x, y))

# 간선을 비용순으로 정렬
edges.sort()
total = 0  # 전체 가로등 비용

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    total += cost
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total - result)
