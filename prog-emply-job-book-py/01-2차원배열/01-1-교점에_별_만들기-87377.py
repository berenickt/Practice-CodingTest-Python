# 💡 교점에 별 만들기(Lv2) 📚 https://school.programmers.co.kr/learn/courses/30/lessons/87377
"""
1. 주어진 직선에서 교점을 구합니다.
    - 문제 설명의 교점 공식을 이용해 주어진 모든 교점을 구하기
    -  x = (b * f - e * d) / (a * d - b * c)
2. 그 중 정수 교점만 따로 변수로 저장합니다.
3. 교점을 모두 표현할 수 있는 최소한의 사각형을 알아냅니다.
4. 모든 교점을 *로 찍어서 표현합니다.
5. 배열을 거꾸로 뒤집어 반환
"""


def solution(line):
    intersections, answer = [], []
    numOfLine = len(line)

    # 2개의 변수 모두 매우 큰 정수 값으로 초기화, int(1e15)는 10의 15승을 의미하며, 매우 큰 양수 값
    x_min = y_min = int(1e15)

    # 2개의 변수 모두 매우 작은 음수 값으로 초기화, -int(1e15)는 -10의 15승을 의미하며, 매우 큰 음수 값
    x_max = y_max = -int(1e15)

    # 📌 (1) 주어진 직선에서 교점을 구합니다.
    for i in range(numOfLine):
        a, b, e = line[i]  # 순회하면서 각 선들의 값들을 받아옴, 2, -1, 4부터 쭉
        for j in range(i + 1, numOfLine):
            c, d, f = line[j]
            if a * d == b * c:
                continue

            # 두 직선의 교점이 유일하게 존재할 경우, 그 교점 구하는 공식
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            # 📌 (2) 그 중 정수 교점만 따로 변수로 저장합니다.
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                intersections.append([x, y])

                # 📌 (3) 교점을 모두 표현할 수 있는 최소한의 사각형을 알아냅니다.
                if x_min > x:
                    x_min = x
                if y_min > y:
                    y_min = y
                if x_max < x:
                    x_max = x
                if y_max < y:
                    y_max = y

    # 📌 (4) 모든 교점을 *로 찍어서 표현합니다.
    x_len = x_max - x_min + 1  # e.g.1) 9 = 4 - (-4) + 1
    y_len = y_max - y_min + 1  # e.g.1) 9 = 4 - (-4) + 1
    grid = [["."] * x_len for _ in range(y_len)]

    # intersections(교차점들) : e.g.1) [[0, 4], [-4, -4], [4, -4], [4, 1], [-4, 1]]
    for star_x, star_y in intersections:
        # x_min이 음수인 경우, star_x에 x_min의 절댓값을 더합니다. 그렇지 않으면 star_x에서 x_min을 뺌
        # 이렇게 하면 nx에는 star_x를 x_min만큼 이동한 새로운 x 좌표가 저장됨
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min

        # nx와 ny 좌표를 사용하여 grid의 해당 위치에 별표(*)를 추가
        grid[ny][nx] = "*"

    # 📌 (5) 배열을 거꾸로 뒤집어 반환 (배열과 좌표는 행이 증가하는 방향이 반대이다. 따라서 위 아래를 뒤집어서 제출)
    for row in grid:
        answer.append("".join(row))  # 문자열을 2~3개 이상 합친다면 ' '.join( )을 사용

    # print(answer)
    # ['*.......*', '.........', '.........', '.........', '.........', '*.......*', '.........', '.........', '....*....']

    return answer[::-1]


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
# ['....*....', '.........', '.........', '*.......*', '.........', '.........', '.........', '.........', '*.......*']
# print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
