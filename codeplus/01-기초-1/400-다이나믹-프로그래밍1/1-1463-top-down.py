# 💡 1로 만들기 - Top-Down 📚 https://www.acmicpc.net/problem/1463
'''
문제의 메모리 제한이 너무 작고, Python은 재귀를 사용하면 시간이 너무 오래 걸리고 
메모리도 너무 많이 차지해서 실제로 제출하면 를 받게 됩니다.
Python은 다이나믹을 풀 때 Bottom-Up을 사용하는 것이 좋고, 이 소스는 참고용으로만 사용해주세요.
'''
import sys

sys.setrecursionlimit(10000000)


def go(n):
    if n == 1:
        return 0
    if d[n] > 0:
        return d[n]
    d[n] = go(n-1) + 1
    if n % 2 == 0:
        temp = go(n//2) + 1
        if d[n] > temp:
            d[n] = temp
    if n % 3 == 0:
        temp = go(n//3) + 1
        if d[n] > temp:
            d[n] = temp
    return d[n]


n = int(input())
d = [0] * (n + 1)
print(go(n))
