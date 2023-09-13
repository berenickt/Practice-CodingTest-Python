# 💡 날짜 계산 📚 https://www.acmicpc.net/problem/1476
# 입력받은 세 개의 정수 E, S, M을 각각 월, 일, 요일로 간주하고
# 해당 날짜가 되는 해를 구하는 프로그램입니다.

# 입력받은 세 개의 정수를 각각 변수에 저장합니다.
e, s, m = map(int, input().split())

# 월, 일, 요일을 1부터 시작하는 변수에 저장합니다.
e -= 1
s -= 1
m -= 1

# 해를 0부터 시작하는 변수에 저장합니다.
year = 0

# 조건을 만족할 때까지 반복합니다.
while True:
    # 월, 일, 요일이 모두 일치하는 경우 해를 출력하고 종료합니다.
    if year % 15 == e and year % 28 == s and year % 19 == m:
        print(year + 1)
        break

    # 해를 1씩 증가시킵니다.
    year += 1
