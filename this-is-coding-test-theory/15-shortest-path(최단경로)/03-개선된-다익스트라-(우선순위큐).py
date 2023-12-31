"""📍 heap을 이용한 다익스트라 알고리즘
개선된 다익스트라 알고리즘에서는 기본적으로 힙(heap)자료구조를 이용한다.
힙(Heap)자료구조를 이용하게 되면 
특정 노드까지의 최단 거리에 대한 정보를 힙에 담아 처리하므로 
출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.
"""

"""📍 heap이란?
힙 자료구조는 우선순위(priority_queue)를 구현하기 위해 사용하는 자료구조 중 하나다.
우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제한다는 점이 특징인데, 표로 나타내면 다음과 같다.

스택(stack)	               : 가장 나중에 삽입된 데이터
큐(queue)	                : 가장 먼저 삽입된 데이터
우선순위 큐(priority_queue) : 가장 우선순위가 높은 데이터

우선순위 큐를 구현할 때는 내부적으로 최소 힙(min_heap) 혹은 최대 힙(max_heap)을 이용한다.
최소 힙을 이용할때는 값이 가장 낮은 데이터가 먼저 삭제되며,
최대 힙은 값이 큰 데이터가 가장 먼저 삭제됨을 알아두자.

파이썬에서 우선순위 큐 라이브러리를 사용할때는 default값이 최소 최소 힙(min_heap)으로 설정되어있는데,
최대 힙(max_heap)으로 사용하고 싶다면,
값에 음수 부호(-)를 붙여서 넣었다가 heapq.heappop 할 때 다시 음수 부호(-)를 붙여 원래의 값으로 돌리면 된다.
"""

"""
[input #1]
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

[output #1]
0
2
3
1
2
4
"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
