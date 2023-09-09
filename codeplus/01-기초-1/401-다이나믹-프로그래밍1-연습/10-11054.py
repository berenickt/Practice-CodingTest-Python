# 💡 가장 긴 바이토닉 부분 수열 📚 https://www.acmicpc.net/problem/11054
n = int(input())
a = list(map(int, input().split()))
d1 = [0]*n
d2 = [0]*n

for i in range(n):
    d1[i] = 1
    for j in range(i):
        if a[j] < a[i] and d1[j]+1 > d1[i]:
            d1[i] = d1[j]+1

for i in range(n-1, -1, -1):
    d2[i] = 1
    for j in range(i+1, n):
        if a[i] > a[j] and d2[j]+1 > d2[i]:
            d2[i] = d2[j]+1

d = [d1[i]+d2[i]-1 for i in range(n)]
print(max(d))
