"""
수학에서 서로소 집합이란 공통 원소가 없는 두 집합을 의미한다.
예를 들면, 집합 {1, 2}와 {3, 4}는 서로소 관계이다.
반면에, 집합 {1, 2}와 {2, 3}은 2라는 원소가 두 집합에 공통적으로 포함되어 있기 때문에 서로소 관계가 아니다.

서로소 집합 자료구조는 union-find(합치기 - 찾기) 자료구조라고도 불린다.
또한, 자료구조를 구현할때는 트리 자료구조를 이용하여 집합을 표현하는데, 알고리즘은 다음과 같다.

1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
    A와 B의 루트노드 A', B'를 각각 찾는다.
    A'를 B'의 부모 노드로 설정한다(B'가 A'를 가리키도록 한다.)
2. 모든 union(합집합) 연산을 처리할 때까지 1번 과정을 반복한다.
"""


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


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

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 내용 출력하기
print("부모 테이블: ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")
