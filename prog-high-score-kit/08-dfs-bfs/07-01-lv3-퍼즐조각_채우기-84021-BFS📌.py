# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/84021
"""
현재 게임 보드의 상태 game_board,
테이블 위에 놓인 퍼즐 조각의 상태 table이 매개변수로 주어집니다
규칙에 맞게 최대한 많은 퍼즐 조각을 채워 넣을 경우, 
총 몇 칸을 채울 수 있는지 return

입력 #1
game_board  : [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table       : [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

출력 #1
14

cf.
우선, game_board에서 빈공간과 table에서 퍼즐들의 정보를 알아야 함
즉, game_board에서는 0의 위치, table에서는 1의 위치를 알아야 함
game_board의 인접한 0들은 하나의 퍼즐이 들어갈 수 있는 하나의 빈공간으로 취급하고,
table에서 인접한 1은 하나의 퍼즐이므로 BFS 알고리즘을 사용

"""
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# board와 puzzle의 각각 빈공간과 블럭을 찾는 함수 (BFS)
def find_block(board, f):
    empty_board_list = []
    visited = [[False] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if not visited[i][j] and board[i][j] == f:
                queue = deque([(i, j)])
                board[i][j] = f ^ 1
                visited[i][j] = True
                lst = [(i, j)]

                while queue:
                    x, y = queue.popleft()
                    for _ in range(4):
                        nx, ny = x + dx[_], y + dy[_]
                        if (
                            nx < 0
                            or nx > len(board) - 1
                            or ny < 0
                            or ny > len(board) - 1
                        ):
                            continue
                        elif board[nx][ny] == f:
                            queue.append((nx, ny))
                            board[nx][ny] = f ^ 1
                            visited[nx][ny] = True
                            lst.append((nx, ny))
                empty_board_list.append(lst)

    return empty_board_list


# block의 인덱스들로 table을 만드는 함수
def make_table(block):
    x, y = zip(*block)
    c, r = max(x) - min(x) + 1, max(y) - min(y) + 1
    table = [[0] * r for _ in range(c)]

    for i, j in block:
        i, j = i - min(x), j - min(y)
        table[i][j] = 1
    return table


# 오른쪽으로 90도 회전하는 함수
def rotate(puzzle):
    rotate = [[0] * len(puzzle) for _ in range(len(puzzle[0]))]
    count = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 1:
                count += 1
            rotate[j][len(puzzle) - 1 - i] = puzzle[i][j]
    return rotate, count


def solution(game_board, table):
    answer = 0
    empty_blocks = find_block(game_board, 0)
    puzzles = find_block(table, 1)

    for empty in empty_blocks:
        filled = False
        table = make_table(empty)

        for puzzle_origin in puzzles:
            if filled == True:
                break

            puzzle = make_table(puzzle_origin)
            for i in range(4):
                puzzle, count = rotate(puzzle)

                if table == puzzle:
                    answer += count
                    puzzles.remove(puzzle_origin)
                    filled = True
                    break

    return answer


game_board = [
    [1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0],
]

table = [
    [1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
]

print(solution(game_board, table))
