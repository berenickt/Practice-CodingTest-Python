# 💡 가장 큰 증가하는 부분 수열 📚 https://www.acmicpc.net/problem/11055
n = int(input())
a = list(map(int, input().split()))
d = [0]*n

for i in range(n):
    d[i] = a[i]
    for j in range(i):
        if a[j] < a[i] and d[j]+a[i] > d[i]:
            d[i] = d[j]+a[i]

print(max(d))
