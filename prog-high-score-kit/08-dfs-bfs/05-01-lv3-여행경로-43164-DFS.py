# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/43164
"""
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다.
항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때,
방문하는 공항 경로를 배열에 담아 return

입력 #1
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

출력 #1
["ICN", "JFK", "HND", "IAD"]
"""


def solution(tickets):
    answer = []
    visited = [False] * len(tickets)

    def dfs(airport, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[idx] = False

    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
