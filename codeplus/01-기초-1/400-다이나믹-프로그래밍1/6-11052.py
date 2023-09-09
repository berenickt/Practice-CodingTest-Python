# 💡 카드 구매하기 📚 https://www.acmicpc.net/problem/11052
n = int(input())
a = [0] + list(map(int, input().split()))
d = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        d[i] = max(d[i], d[i-j]+a[j])

print(d[n])
