# 💡 합분해 📚 https://www.acmicpc.net/problem/2225
mod = 1000000000
n, m = map(int, input().split())
d = [0] * (n + 1)
d[0] = 1

for i in range(1, m + 1):
    for j in range(1, n + 1):
        d[j] += d[j - 1]
        d[j] %= mod

print(d[n])
