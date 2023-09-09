# 💡 N과 M (8) 📚 https://www.acmicpc.net/problem/15657
import sys

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
cnt = [0] * n


def go(index, selected, n, m):
    if selected == m:
        for i in range(n):
            for j in range(cnt[i]):
                sys.stdout.write(str(num[i]) + " ")
        sys.stdout.write("\n")
        return
    if index >= n:
        return
    for i in range(m - selected, 0, -1):
        cnt[index] = i
        go(index + 1, selected + i, n, m)
    cnt[index] = 0
    go(index + 1, selected, n, m)


go(0, 0, n, m)
