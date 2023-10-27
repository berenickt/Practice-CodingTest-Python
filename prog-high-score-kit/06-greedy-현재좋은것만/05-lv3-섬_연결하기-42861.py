# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42861
"""
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때,
최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return

입력 #1
n      : 4
costs  : [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

출력 #1
4

cf. [도착, 종료, 비용] 형태
cf. lambda 매개변수 : 표현식

cf. 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 
e.g. A 섬과 B 섬 사이에 다리가 있고, 
B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능
"""


def solution(n, costs):
    minCost = 0

    # 비용 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    # 시작 연결점을 set 리스트에 추가, => {0}
    link = set([costs[0][0]])

    ### Kruskal 알고리즘으로 최소 비용 구하기
    # set 안에 연결된 모든 위치가 연결되기전까지 실행하는 조건
    # 문제의 제한사항 중: 연결할 수 없는 섬은 주어지지 않습니다 를 만족
    while len(link) != n:
        for v in costs:
            # 두 섬이 이미 더 낮은 가격으로 연결이 되었을 경우 무시
            if v[0] in link and v[1] in link:
                continue
            # 두 섬 중 하나가 연결이 되어있지 않을 때 비용을 더하기
            if v[0] in link or v[1] in link:
                # set.update()는 중복을 제거
                # 이미 섬이 연결되었을경우 중복된 섬은 추가되지 않고 최대 n 개의 섬을 유지
                link.update([v[0], v[1]])
                minCost += v[2]
                break

    return minCost


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
