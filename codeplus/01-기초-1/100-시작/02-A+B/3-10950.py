# 💡 A+B - 3 📚 https://www.acmicpc.net/problem/10950

# (1) 테스트 케이스 T 값을 입력 받습니다.
t = int(input())

# (2) 테스트 케이스마다 a, b 를 입력 받고, a+b 를 출력
for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)
