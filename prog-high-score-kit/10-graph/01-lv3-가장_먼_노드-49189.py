# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/49189
"""
n개의 노드가 있는 그래프가 있습니다.
각 노드는 1부터 n까지 번호가 적혀있습니다.
1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다.
가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 
간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때,
1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return

입력 #1
n      : 6
vertex : [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

출력 #1
3
"""
from collections import deque


def solution(n, edge):
    answer = 0
    # 연결된 노드 정보 그래프
    graph = [[] for _ in range(n + 1)]
    # 각 노드의 최단거리 리스트
    distance = [-1] * (n + 1)

    # 연결된 노드 정보 추가
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue = deque([1])  # BFS를 위한 queue, 출발 노드 = 1
    distance[1] = 0  # 출발노드의 최단거리를 0으로

    # BFS 수행
    while queue:
        now = queue.popleft()  # 현재 노드

        # 현재 노드에서 이동할 수 있는 모든 노드 확인
        for i in graph[now]:
            if distance[i] == -1:  # 아직 방문하지 않은 노드면,
                queue.append(i)  # queue에 추가
                distance[i] = distance[now] + 1  # 최단거리 갱신

    # 가장 멀리 떨어진 노드 개수 구하기
    for d in distance:
        if d == max(distance):
            answer += 1
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
