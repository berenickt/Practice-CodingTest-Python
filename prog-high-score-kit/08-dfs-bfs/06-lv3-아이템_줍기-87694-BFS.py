# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/87694
"""
지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle,
초기 캐릭터의 위치 characterX, characterY,
아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때,
캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return

입력 #1
rectangle  : [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX : 1
characterY : 3
itemX      : 7 
itemY      : 8

출력 #1
17

cf. 
2차원 배열 만들어 두고
테두리는 1, 내부는 0으로 표시
테두리와 내부가 겹칠경우 0으로 표시
"""

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102  # 두배로 늘리기 때문에 최대 102
    # 테투리 그리기
    field = [[5] * MAX for _ in range(MAX)]  # 5는 맨처음 땅
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:  # 내부일 때
                    field[i][j] = 0
                elif field[i][j] != 0:  # 테두리일 때 그리고 이미 내부가 아닐 때
                    field[i][j] = 1  # 테투리랑 내부랑 겹치면 그건 내부

    # 길 찾기 (최단거리는 BFS)
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[0] * MAX for _ in range(MAX)]
    visited[characterX * 2][characterY * 2] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = (visited[x][y] - 1) // 2
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if visited[nx][ny] == 0 and field[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return answer


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
