# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""
게임 맵의 상태 maps가 매개변수로 주어질 때,
캐릭터가 상대 팀 진영에 도착하기 위해서, 
지나가야 하는 칸의 개수의 최솟값을 return
단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return

입력 #1
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

출력 #1
11
"""

from collections import deque


def solution(maps):
    answer = 0

    # 상하좌우
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        # queue가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()

            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵을 벗어나면 무시하기
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue

                # 벽이면 무시하기
                if maps[nx][ny] == 0:
                    continue

                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))  # 재귀

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[len(maps) - 1][len(maps[0]) - 1]

    answer = bfs(0, 0)

    # 상대 팀 진영에 도착할 수 없을 때 -1
    return -1 if answer == 1 else answer


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)
