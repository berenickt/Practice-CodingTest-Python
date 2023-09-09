# 💡 연속합 📚 https://www.acmicpc.net/problem/1912
n = int(input())
a = list(map(int, input().split()))
d = [0] * n

for i in range(n):
    d[i] = a[i]
    if i == 0:
        continue
    if d[i] < d[i - 1] + a[i]:
        d[i] = d[i - 1] + a[i]

print(max(d))
