# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/43162
"""
컴퓨터의 개수 n, 
연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
네트워크의 개수를 return

입력 #1
n         : 3
computers : [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

출력 #1
2
"""


def solution(n, computers):
    def dfs(idx):
        # idx번쨰 노드를 이미 방문했으니 다시 방문못하도록 막기
        visited[idx] = True

        # j번을 방문하지 않았고, 개가 나랑 연결되어 있으면, dfs 재귀호출
        for j in range(n):
            if not visited[j] and computers[idx][j]:
                dfs(j)

    # ✅ 0. 입력 및 초기화
    count = 0
    visited = [False] * n

    # ✅ 2. dfs(재귀함수) 호출
    # 연결되어 있는 요소의 묶음이 몇 개인지 visited배열이 모두 true가 되기까지 계속 순회
    for i in range(n):
        # 방문된 적이 없으면, dfs 호출
        if not visited[i]:
            dfs(i)
            count += 1
    return count


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
