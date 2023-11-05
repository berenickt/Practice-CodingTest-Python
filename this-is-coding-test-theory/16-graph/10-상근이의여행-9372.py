# 📚 https://www.acmicpc.net/problem/9372
import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    for j in range(m):
        a, b = map(int, input().split())
    print(n - 1)
