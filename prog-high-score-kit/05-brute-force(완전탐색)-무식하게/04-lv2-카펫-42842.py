# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42842
"""
Leo가 본 카펫에서 갈색 격자의 수 brown, 
노란색 격자의 수 yellow가 매개변수로 주어질 때,
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return

입력#1
brown  : 10
yellow : 2

출력#1
[4, 3]
"""


def solution(brown, yellow):
    total = brown + yellow  # a * b = total

    for b in range(1, total + 1):
        if (total / b) % 1 == 0:  # total / b = a
            a = total / b
            if a >= b:
                if 2 * a + 2 * b == brown + 4:  # 2*a + 2*b = brown + 4
                    return [a, b]


print(solution(10, 2))
