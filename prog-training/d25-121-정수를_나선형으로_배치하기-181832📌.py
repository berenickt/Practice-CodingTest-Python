# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181832
"""
양의 정수 n이 매개변수로 주어집니다.
n x n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return

입력#1
4

출력#1
[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
"""


def solution(n):
    # 0으로 채워진 초기 배열 지정
    arr = [[0 for i in range(n)] for j in range(n)]
    # 시작 위치, 방향 설정
    x, y = 0, 0
    direc = "r"

    for i in range(n**2):
        arr[x][y] = i + 1
        if direc == "r":
            if y == n - 1 or arr[x][y + 1] != 0:
                direc = "d"
                x += 1
            else:
                y += 1
        elif direc == "d":
            if x == n - 1 or arr[x + 1][y] != 0:
                direc = "l"
                y -= 1
            else:
                x += 1
        elif direc == "l":
            if y == 0 or arr[x][y - 1] != 0:
                direc = "u"
                x -= 1
            else:
                y -= 1
        elif direc == "u":
            if x == 0 or arr[x - 1][y] != 0:
                direc = "r"
                y += 1
            else:
                x -= 1
    return arr


print(solution(4))
