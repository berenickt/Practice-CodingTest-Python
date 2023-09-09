# 💡 조합 0의 개수 📚 https://www.acmicpc.net/problem/2004
def calc(n, v):
    ans = 0
    i = v
    while i <= n:
        ans += n//i
        i *= v
    return ans


two = 0
five = 0
n, m = map(int, input().split())
two += calc(n, 2)
two -= calc(n-m, 2)
two -= calc(m, 2)
five += calc(n, 5)
five -= calc(n-m, 5)
five -= calc(m, 5)
print(min(two, five))
