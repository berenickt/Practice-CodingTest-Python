""" heapq()
최단 경로 알고리즘을 포함해 
다양한 알고리즘에서 우선순위 큐 기능을 구현하는 함수
"""
import heapq


def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
# 👉🏽 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# max_heapq
def max_heapq(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


print(max_heapq([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
# 👉🏽 [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
