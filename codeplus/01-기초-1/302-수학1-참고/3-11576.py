# 💡 Base Conversion 📚 https://www.acmicpc.net/problem/11576
def convert(num, base):
    if num == 0:
        return
    convert(num//base, base)
    print(num % base, end=' ')


a, b = map(int, input().split())
n = int(input())
ans = 0
num = list(map(int, input().split()))

for x in num:
    ans = ans * a + x

convert(ans, b)
