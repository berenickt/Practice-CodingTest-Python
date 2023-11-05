"""📍 kruskal_algorithm(크루스칼 알고리즘)
크루스칼 알고리즘은 다양한 문제 상황에서 가능한 한 최소한의 비용으로 신장 트리를 찾아야 할 때가 있다.

예를 들어, N개의 도시에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우에서,
2개의 도시 A, B를 선택했을 때, 도시 A에서 B로 이동하는 경로가 반드시 존재해야한다.

이때, 모든 도시를 연결할 때 최소한의 비용으로 연결하려면 어떤 알고리즘을 사용해야 할까? 
와 같은 문제에서 크루스칼을 이용하면 효율적으로 답을 구할 수 있다.

짧게나마 예시를 들었는데, 이처럼 3개의 노드와 간선이 있다고 가정했을때,
한 노드에서 다른노드를 가는 비용이 최소일때는 23 + 13 = 36인 경우가 있다.

이처럼 신장 트리 중에서 최소 비용으로 만들 수 있는 신장트리를 찾는 알고리즘을 최소 신장트리 알고리즘이고 
또 이를 활용하는 대표적인 알고리즘이 크루스칼 알고리즘인 것이다.

알고리즘의 핵심 원리는 다음과 같다.

1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
    사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
3. 모든 간선에 대하여 2번의 과정을 반복한다.

시간복잡도는 다음과 같다.
간선의 개수가 E개 일때, O(ElogE)
- 간선을 정렬하는 작업의 시간복잡도가 O(ElogE)이기 때문이다.
- 서로소 집합 알고리즘 시간 복잡도 < 정렬 시간복잡도

@see 동빈나 19강 크루스칼 https://www.youtube.com/watch?v=LQ3JHknGy8c&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz&index=19
@see 이코테 2021 https://www.youtube.com/watch?v=aOhhNFTIeFI&t=2120s
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


# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

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
