# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/43164
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


def solution(rectangle, characterX, characterY, itemX, itemY):
    MAXNUM = 1000
    board = [[0 for j in range(MAXNUM)] for i in range(MAXNUM)]

    # 사각형 1로 채우기 (테두리+내부)
    for c1, r1, c2, r2 in rectangle:
        for i in range(2 * r1, 2 * r2 + 1):
            for j in range(2 * c1, 2 * c2 + 1):
                board[i][j] = 1

    # 사각형 테두리 0으로 채우기
    for c1, r1, c2, r2 in rectangle:
        for i in range(2 * r1 + 1, 2 * r2):
            for j in range(2 * c1 + 1, 2 * c2):
                board[i][j] = 0

    # 테두리 따라가기
    chR, chC, itR, itC = 2 * characterY, 2 * characterX, 2 * itemY, 2 * itemX
    stack = [(0, chR, chC)]
    while stack:
        w, chR, chC = stack.pop(0)  # 너비 우선 탐색
        board[chR][chC] = -1  # passed

        if board[itR][itC] < 0:
            return w // 2

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if board[chR + dr][chC + dc] > 0:
                stack.append((w + 1, chR + dr, chC + dc))


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
