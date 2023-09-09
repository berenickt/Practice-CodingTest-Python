# 💡 A+B - 8 📚 @https://www.acmicpc.net/problem/11022
t = int(input())

for x in range(1, t + 1):  # 1부터 t까지
    a, b = map(int, input().split())
    print(f'Case #{x}: {a} + {b} = {a + b}')
