# 💡 1로 만들기 - Top-Down 📚 https://www.acmicpc.net/problem/1463
"""
문제의 메모리 제한이 너무 작고, Python은 재귀를 사용하면 시간이 너무 오래 걸리고 
메모리도 너무 많이 차지해서 실제로 제출하면 False를 받게 됩니다.
Python은 다이나믹을 풀 때 Bottom-Up을 사용하는 것이 좋고, 이 소스는 참고용으로만 사용해주세요.
"""
# 필요한 재귀 깊이를 설정
import sys

sys.setrecursionlimit(10000000)


# 메모이제이션을 위한 배열 d를 초기화
# d[i]는 정수 i를 1로 만드는 데 필요한 연산 횟수를 저장
def go(n):
    # 재귀 종료 조건: 정수가 1인 경우 연산 횟수는 0
    if n == 1:
        return 0

    # 이미 연산된 값이라면 해당 값을 반환
    if d[n] > 0:
        return d[n]

    # 정수 n을 1로 만드는 연산 중에서 최소 연산 횟수를 구함
    # n에서 1을 빼는 경우
    d[n] = go(n - 1) + 1

    # n이 2로 나누어 떨어질 경우, 2로 나눈 결과의 연산 횟수를 구하고 더 작은 값을 선택
    if n % 2 == 0:
        temp = go(n // 2) + 1
        if d[n] > temp:
            d[n] = temp

    # n이 3으로 나누어 떨어질 경우, 3으로 나눈 결과의 연산 횟수를 구하고 더 작은 값을 선택
    if n % 3 == 0:
        temp = go(n // 3) + 1
        if d[n] > temp:
            d[n] = temp
    return d[n]


# 사용자로부터 입력받은 정수 n을 1로 만드는 데 필요한 최소 연산 횟수를 출력
n = int(input())

# 연산 횟수를 저장할 배열 d를 초기화
d = [0] * (n + 1)
print(go(n))
