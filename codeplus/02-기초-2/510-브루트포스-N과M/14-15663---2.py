# 💡 N과 M (9) 📚 https://www.acmicpc.net/problem/15663
import sys
from collections import Counter

n, m = map(int, input().split())
temp = list(map(int, input().split()))
temp = list(Counter(temp).items())
temp.sort()
n = len(temp)
num, cnt = map(list, zip(*temp))
a = [0] * m


def go(index, n, m):
    if index == m:
        sys.stdout.write(" ".join(map(str, a)) + "\n")
        return
    for i in range(n):
        if cnt[i] > 0:
            cnt[i] -= 1
            a[index] = num[i]
            go(index + 1, n, m)
            cnt[i] += 1


go(0, n, m)
