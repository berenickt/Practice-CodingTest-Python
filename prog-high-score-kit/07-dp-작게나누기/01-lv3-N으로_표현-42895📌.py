# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42895
"""
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다.
그리고 이중 가장 작은 경우는 4입니다.

이처럼 숫자 N과 number가 주어질 때,
N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return

입력 #1
N      : 5
number : 12

출력 #1
4

cf. N은 1 이상 9 이하
cf2. 최솟값이 8보다 크면 -1을 return

cf. 작은 문제로 큰 문제 해결할 수 있는지 확인
N을 1개 사용해서 표현하기
N을 2개 사용해서 표현하기
"""


from collections import defaultdict


def solution(N, number):
    # dp[i]: N을 i번 사용해서 만들 수 있는 수들의 집합
    dp = defaultdict(set)

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # NNN...N
        for j in range(1, i):
            for n1 in dp[j]:
                for n2 in dp[i - j]:
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n1 * n2)
                    if n2 != 0:
                        dp[i].add(n1 // n2)  # 0으로 나눌 수 없음

        if number in dp[i]:
            return i  # N을 i번 사용해서 number를 만들 수 있음

    return -1  # 최솟값이 8번보다 클 경우


print(solution(5, 12))
