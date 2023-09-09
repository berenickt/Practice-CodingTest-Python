# 💡 A+B - 7 📚 https://www.acmicpc.net/problem/11021
# 첫 번째 입력으로 테스트 케이스의 개수를 입력받음
T = int(input())

# 테스트 케이스의 개수만큼 반복
for i in range(1, T + 1):  # 1부터 t까지
    # 사용자로부터 두 정수를 입력받고, 입력값을 공백을 기준으로 분리하여 정수 변수 a와 b에 할당
    a, b = map(int, input().split())
    print(f'Case #{i}: {a + b}')
