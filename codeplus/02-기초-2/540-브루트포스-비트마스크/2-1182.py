# 💡 부분집합의 합 📚 https://www.acmicpc.net/problem/1182
n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(1, (1 << n)):
    s = sum(a[k] for k in range(n) if (i & (1 << k)) > 0)
    if m == s:
        ans += 1

print(ans)
