# 💡 A+B - 7 📚 https://www.acmicpc.net/problem/11021
TEST_CASE = int(input())

# 1부터 TEST_CASE까지 반복
for i in range(1, TEST_CASE + 1):
    # 사용자로부터 두 정수를 입력받고, 입력값을 공백을 기준으로 분리하여 정수 변수 a와 b에 할당
    a, b = map(int, input().split())
    print(f"Case #{i}: {a + b}")
