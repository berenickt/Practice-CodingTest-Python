"""
간단한 dijkstra_algorithm은 최단 거리가 가장 짧은 노드를 찾기 위해 
매번 최단거리 테이블을 선형적으로(모든 원소를 앞에서부터 하나씩) 탐색해야했다.
선형적으로 탐색한 코드는 다음과 같다.
"""

for i in range(1, n + 1):
    if distance[i] < min_value and not visited[i]:
        min_value = distance[i]
        index = i
return index

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


# desc heap_example
def heapsort(n):
    h = []
    result = []

    for i in n:
        heapq.heappush(h, -i)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


"""
linear_path와의 주요 차이점은 방문처리해주는 함수(get_smallest_node())가 없고,
대신 우선순위 큐를 이용하는 방식으로 대체할 수 있기 때문에 코드가 간결해진다.
"""
"""
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
"""

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i], end=" ")
# 👉🏽 0 2 3 1 2 4

"""
이와 같이 모든 단계를 거친 후 최단 거리 테이블에 남아 있는 0, 2, 3, 1, 2, 4가 각 노드로의 최단 거리이다.

다익스트라 최단 경로 알고리즘은 우선순위 큐를 이용한다는 점에서 
우선순위 큐를 필요로 하는 다른 문제 유형과도 흡사하다는 특징이 있다. 
그래서 최단 경로를 찾는 문제를 제외하고도 다른 문제에도 두루 적용되는 소스코드 형태라고 이해할 수 있다.
"""
