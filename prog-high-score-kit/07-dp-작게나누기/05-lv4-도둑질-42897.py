# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42897
"""
도둑이 어느 마을을 털 계획을 하고 있습니다.
이 마을의 모든 집들은 그림과 같이 동그랗게 배치되어 있습니다.

각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 
인접한 두 집을 털면 경보가 울립니다.

각 집에 있는 돈이 담긴 배열 money가 주어질 때,
도둑이 훔칠 수 있는 돈의 최댓값을 return

입력 #1
[1, 2, 3, 1]

출력 #1
4
"""


def solution(money):
    a = [money[0], money[0]]
    b = [0, money[1]]

    for i in range(2, len(money) - 1):
        a.append(max(a[i - 2] + money[i], a[i - 1]))
        b.append(max(b[i - 2] + money[i], b[i - 1]))
    answer = max(a[-1], b[-2] + money[-1])

    return answer


print(solution([1, 2, 3, 1]))
