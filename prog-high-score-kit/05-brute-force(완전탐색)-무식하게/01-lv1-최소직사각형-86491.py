# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/86491
"""
모든 명함의 가로 길이와 세로 길이를 나타내는 
2차원 배열 sizes가 매개변수로 주어집니다.
모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때,
지갑의 크기를 return

입력 #1
[[60, 50], [30, 70], [60, 30], [80, 40]]

출력 #1
4000

cf. 명함을 회전시킬 수 있기 때문에, 
입력받은 가로, 세로를 가로가 더 길도록 하여 최소 크기를 구하
"""


def solution(sizes):
    max_w, max_h = 0, 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    return max_w * max_h


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
