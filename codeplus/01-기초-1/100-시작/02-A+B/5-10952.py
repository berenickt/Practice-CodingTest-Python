# 💡 A+B - 5 📚 https://www.acmicpc.net/problem/10952
while True:
  # 사용자로부터 두 정수를 입력받고, 입력값을 공백을 기준으로 분리하여 정수 변수 a와 b에 할당
    a, b = map(int, input().split())

    # 만약 a와 b가 모두 0이라면, 루프를 종료
    if (a == 0 and b == 0):
        break

    # a와 b의 합을 계산하고 출력
    else:
        print(a + b)
