# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/86971
"""
현재의 전력망 네트워크를 2개로 분할하려고 합니다.
이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추기

송전탑의 개수 n,
전선 정보 wires가 매개변수로 주어집니다. 
전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 
두 전력망으로 나누었을 때,
두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return

입력#1
k     : 9
wires : [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

출력#1
3
"""
from collections import deque


def solution(n, wires):
    def bfs(start):
        visited = [0] * (n + 1)
        q = deque([start])
        visited[start] = 1
        cnt = 1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        return cnt

    res = 0
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    res = n
    for a, b in wires:
        # graph에서 remove
        graph[a].remove(b)
        graph[b].remove(a)

        res = min(abs(bfs(a) - bfs(b)), res)

        # 다시 append
        graph[a].append(b)
        graph[b].append(a)

    return res


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
