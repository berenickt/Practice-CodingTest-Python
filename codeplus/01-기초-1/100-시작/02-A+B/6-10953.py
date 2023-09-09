# 💡 A+B - 6 📚 https://www.acmicpc.net/problem/10953
# 첫 번째 입력으로 테스트 케이스의 개수를 입력 받음
T = int(input())

# 테스트 케이스의 개수만큼 반복
for _ in range(T):
    # 사용자로부터 두 정수를 입력받고, 입력값을 콤마(,)를 기준으로 분리하여 정수 변수 a와 b에 할당
    a, b = map(int, input().split(','))
    print(a + b)
