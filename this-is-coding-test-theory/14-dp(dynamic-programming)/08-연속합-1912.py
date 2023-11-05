# 📚 https://www.acmicpc.net/problem/1912
import sys

n = int(input())

array = list(map(int, sys.stdin.readline().split()))

d = [0] * n
d[0] = array[0]

for i in range(1, n):
    if d[i - 1] + array[i] > array[i]:
        d[i] = d[i - 1] + array[i]
    else:
        d[i] = array[i]

print(max(d))
# 👉🏽 33 14 -1
