# 💡 A+B - 4 📚 https://www.acmicpc.net/problem/10951
while True:
    try:
        # 사용자로부터 두 정수를 입력받고, 공백을 기준으로 분리하여 정수 변수 a와 b에 할당
        a, b = map(int, input().split())
        print(a + b)
    except:
        # 예외가 발생하면(예: 입력이 정수가 아닌 경우), 루프를 종료
        break
