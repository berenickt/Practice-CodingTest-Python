# 💡 동물원 📚 https://www.acmicpc.net/problem/1309
d = [0] * 100001
s = [0] * 100001
n = int(input())
d[0] = 1
s[0] = 1
d[1] = 2
s[1] = d[0] + d[1]

for i in range(2, n + 1):
    d[i] = d[i - 1] + 2 * s[i - 2]
    s[i] = s[i - 1] + d[i]
    d[i] %= 9901
    s[i] %= 9901

print(s[n])
