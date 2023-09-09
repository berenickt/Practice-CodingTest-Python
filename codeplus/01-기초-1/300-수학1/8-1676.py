# 💡 팩토리얼 0의 개수 📚 https://www.acmicpc.net/problem/1676
def calc(n, v):
    ans = 0
    i = v
    while i <= n:
        ans += n//i
        i *= v
    return ans


n = int(input())
ans = calc(n, 5)
print(ans)
