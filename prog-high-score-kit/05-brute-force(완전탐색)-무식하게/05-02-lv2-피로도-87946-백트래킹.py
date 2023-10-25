# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
유저의 현재 피로도 k와 
각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons가 매개변수로 주어질 때, 
유저가 탐험할수 있는 최대 던전 수를 return

입력#1
k        : 80
dungeons : [[80, 20], [50, 40], [30, 10]]

출력#1
3

입출력 예 설명#1
첫 번째 → 두 번째 → 세 번째 던전 순서로 탐험한다면 2번밖에 못함
첫 번째 → 세 번째 → 두 번째 던전 순서로 탐험한다면 3번 가능
"""

answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    # 최대 방문 횟수 초기화
    if cnt > answer:
        answer = cnt
    # 방문 시작 점 설정
    # DFS로 탐색이 끝나고, 다른 시작 점으로 탐색 시작
    for j in range(N):
        # 피로도가 충분해서 방문할 수 있지만, 아직 방문하지 않은 경우
        if k >= dungeons[j][0] and not visited[j]:
            # 방문 처리
            visited[j] = 1
            # 줄어든 피로도로 던전 방문 시작
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            # 해당 순서로 던전을 모두 방문했으니, 다시 초기화
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
