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
    pos, answer = [], []
    n = len(line)

    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)

    # 📌 (1) 주어진 직선에서 교점을 구합니다.
    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
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
                pos.append([x, y])

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
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    coord = [["."] * x_len for _ in range(y_len)]

    for star_x, star_y in pos:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        coord[ny][nx] = "*"

    # 📌 (5) 배열을 거꾸로 뒤집어 반환
    for result in coord:
        answer.append("".join(result))  # 문자열을 2~3개 이상 합친다면 ' '.join( )을 사용

    return answer[::-1]


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
# print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
