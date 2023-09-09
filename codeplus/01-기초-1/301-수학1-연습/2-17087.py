# 💡 숨바꼭질 6 📚 https://www.acmicpc.net/problem/17087
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


n, s = map(int, input().split())
a = list(map(int, input().split()))
a = [abs(x-s) for x in a]
ans = a[0]

for i in range(1, n):
    ans = gcd(ans, a[i])

print(ans)
