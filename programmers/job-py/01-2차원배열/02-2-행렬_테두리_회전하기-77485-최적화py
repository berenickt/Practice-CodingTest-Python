# 💡 행렬 테두리 회전하기(Lv2) 📚 https://school.programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, listOfRotation):
    answer = []
    # 📌 (1) 1씩 증가하는 행렬을 생성합니다.
    board = [[columns * j + (i + 1) for i in range(columns)] for j in range(rows)]
    # print(board) 👇
    # [[1, 2, 3, 4, 5, 6],      [7, 8, 9, 10, 11, 12],     [13, 14, 15, 16, 17, 18], 
    # [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30],  [31, 32, 33, 34, 35, 36]]

    # 📌 (2) 회전해야 할 위치들의 값을 받아옵니다.
    for rot in listOfRotation:
        a, b, c, d = rot[0] - 1, rot[1] - 1, rot[2] - 1, rot[3] - 1

        # 📌 (3) 행렬을 시계 방향으로 회전시킵니다. (반대로 구현하되, 파이썬의 슬라이싱 기능을 활용)
        row1, row2 = board[a][b:d], board[c][b + 1 : d + 1]
        _min = min(row1 + row2)

        for i in range(c, a, -1):
            board[i][d] = board[i - 1][d]
            if board[i][d] < _min:
                _min = board[i][d]

        for i in range(a, c):
            board[i][b] = board[i + 1][b]
            if board[i][b] < _min:
                _min = board[i][b]

        board[a][b + 1 : d + 1], board[c][b:d] = row1, row2

        answer.append(_min)

    return answer

print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))