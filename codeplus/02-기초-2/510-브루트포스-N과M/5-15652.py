# 💡 N과 M (4) 📚 https://www.acmicpc.net/problem/15652
import sys

n, m = map(int, input().split())
c = [False] * (n + 1)
a = [0] * n


def go(index, start, n, m):
    if index == m:
        for i in range(m):
            sys.stdout.write(str(a[i]) + " ")
        sys.stdout.write("\n")
        return
    for i in range(start, n + 1):
        c[i] = True
        a[index] = i
        go(index + 1, i, n, m)
        c[i] = False


go(0, 1, n, m)
