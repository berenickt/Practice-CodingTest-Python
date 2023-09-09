# 💡 N과 M (9) 📚 https://www.acmicpc.net/problem/15663
import sys

n, m = map(int, input().split())
c = [False] * (n + 1)
num = list(map(int, input().split()))
num.sort()
a = [0] * m
d = []


def go(index, n, m):
    if index == m:
        temp = [num[a[i]] for i in range(m)]
        d.append(tuple(temp))
        return
    for i in range(n):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index + 1, n, m)
        c[i] = False


go(0, n, m)
d = list(set(d))
d.sort()
for v in d:
    print(" ".join(map(str, v)))
