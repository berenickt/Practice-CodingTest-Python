# 💡 진법 변환 @ 📚 https://www.acmicpc.net/problem/2745
s, b = input().split()
b = int(b)
ans = 0

for ch in s:
    if '0' <= ch <= '9':
        ans = ans * b + (ord(ch) - ord('0'))
    else:
        ans = ans * b + (ord(ch) - ord('A') + 10)

print(ans)
