# 💡 1, 2, 3 더하기 📚 https://www.acmicpc.net/problem/9095
"""
1 -> (1) -> 1개
2 -> (1+1), (2) -> 2개
3 -> (1+1+1), (1+2), (2+1), (3) -> 4개
4 -> (1+1+1+1), (1+1+2), (1+2+1), (1+3), (2+1+1), (2+2), (3+1) -> 7개

위의 규칙을 봤을 때, 4번째 경우의 수 === 1번째 + 2번째 + 3번째 경우의 수
5번째 경우의 수는 2, 3, 4번째 경우의 수의 합과 같다.

따라서, 위의 규칙을 보면 하나의 점화식이 나온다.
n이 3보다 클 때(n > 3), 
f(n) = f(n-1) + f(n-2) + f(n-3)
"""
TEST_CASE = int(input())


def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n - 1) + sol(n - 2) + sol(n - 3)


for _ in range(TEST_CASE):
    n = int(input())
    print(sol(n))
