# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/49190
"""
원점(0,0)에서 시작해서 아래처럼 숫자가 적힌 방향으로 이동하며 선을 긋습니다.

ex) 1일때는 오른쪽 위로 이동

그림을 그릴 때, 사방이 막히면 방하나로 샙니다.
이동하는 방향이 담긴 배열 arrows가 매개변수로 주어질 때, 방의 갯수를 return 

입력 #1
[6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]

출력 #1
3
"""
from collections import defaultdict


def solution(arrows):
    answer = 0
    visit = defaultdict(list)
    x, y = 0, 0
    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

    for arrow in arrows:
        for _ in range(2):  # 대각선 판별을 위해 2씩
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            if (nx, ny) in visit and (x, y) not in visit[
                (nx, ny)
            ]:  # 방문했던 점이지만 경로가 겹치지 않는 경우, 방+1
                answer += 1
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x, y))
            elif (nx, ny) not in visit:  # 방문하지 않았던 경우
                visit[(x, y)].append((nx, ny))  # 경로가 겹치는 경우는 따로 해줄 필요 없음
                visit[(nx, ny)].append((x, y))
            x, y = nx, ny  # 이동
    return answer


print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
