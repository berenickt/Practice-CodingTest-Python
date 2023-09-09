# 💡 가장 긴 증가하는 부분 수열 4 📚 https://www.acmicpc.net/problem/14002
n = int(input())
a = list(map(int, input().split()))
d = [0]*n
v = [-1]*n

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i] and d[j]+1 > d[i]:
            d[i] = d[j]+1
            v[i] = j

ans = max(d)
p = [i for i, x in enumerate(d) if x == ans][0]
print(ans)


def go(p):
    if p == -1:
        return
    go(v[p])
    print(a[p], end=' ')


go(p)
print()
