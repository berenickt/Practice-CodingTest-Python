# 💡 교점에 별 만들기(Lv2) 📚 https://school.programmers.co.kr/learn/courses/30/lessons/87377
"""
1. 주어진 직선에서 교점을 구합니다.
    - 문제 설명의 교점 공식을 이용해 주어진 모든 교점을 구하기
    -  x = (b * f - e * d) / (a * d - b * c)
2. 그 중 정수 교점만 기억하고, 최소/최대 크기를 알아냅니다.
3. 교점을 모두 표현할 수 있는 최소한의 사각형을 알아냅니다.
4. 모든 교점을 *로 찍어서 표현합니다.

이 방법은 별을 찍을 때 무조건 가장 작은 좌표부터 시작하므로 
나중에 배열을 뒤집을 필요가 없고, 
점을 찍을 때 주어진 값이 양수인지 음수인지 
매번 확인할 필요가 없으므로 실수할 가능성을 크게 낮췄습니다. 
이런 식으로 무조건 빠르게 돌아가는 것에만 집중하는 것이 아니라, 
자신의 약점(자주 실수하는 유형, 반복적으로 틀리는 부분)은 
시간 복잡도를 조금 희생하여 커버할 수도 있기 때문에, 
시간이 느리더라도 얻을 수 있는 이득을 살펴보기 바랍니다.
"""


def solution(numOfLine):
    meet = list()

    # 음의 무한대(-float("inf"))로 초기화, 음의 무한대는 어떤 실수보다도 작은 값으로 간주
    x_max = y_max = -float("inf")

    # 양의 무한대(float("inf"))로 초기화, 양의 무한대는 어떤 실수보다도 큰 값으로 간주
    x_min = y_min = float("inf")

    # 📌 (1) 주어진 직선에서 교점을 구합니다.
    for i in range(len(numOfLine)):
        a, b, e = numOfLine[i]
        for j in range(i + 1, len(numOfLine)):
            c, d, f = numOfLine[j]
            if ((a * d) - (b * c)) == 0:
                continue

            # 두 직선의 교점이 유일하게 존재할 경우, 그 교점 구하는 공식
            x = ((b * f) - (e * d)) / ((a * d) - (b * c))
            y = ((e * c) - (a * f)) / ((a * d) - (b * c))

            # 📌 (2) 그 중 정수 교점만 기억하고, 최소/최대 크기를 알아냅니다.
            if x.is_integer() and y.is_integer():
                x = int(x)
                y = int(y)
                meet.append([x, y])
                x_max, y_max = max(x_max, x), max(y_max, y)
                x_min, y_min = min(x_min, x), min(y_min, y)

    # 📌 (3) 교점을 모두 표현할 수 있는 최소한의 사각형을 알아냅니다.
    width = abs(x_max - x_min) + 1
    height = abs(y_max - y_min) + 1
    answer = [["."] * width for _ in range(height)]

    # 📌 (4) 모든 교점을 *로 찍어서 표현합니다.
    meet = sorted(meet, key=lambda i: -i[1])
    for x, y in meet:
        ny = y_max - y
        nx = x - x_min
        answer[ny][nx] = "*"

    return list(map("".join, answer))


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
# print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
