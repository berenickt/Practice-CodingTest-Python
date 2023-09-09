# 💡 최소공배수 📚 https://www.acmicpc.net/problem/1934
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(a * b // g)
