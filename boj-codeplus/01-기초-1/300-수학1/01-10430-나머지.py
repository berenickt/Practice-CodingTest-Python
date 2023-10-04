# 💡 나머지 📚 https://www.acmicpc.net/problem/10430

# 사용자로부터 세 개의 정수를 입력받고, 입력값을 공백을 기준으로 분리하여 정수 변수 a, b, c에 할당
a, b, c = map(int, input().split())

# (a를 c로 나눈 나머지 + b를 c로 나눈 나머지)를 c로 나눈 나머지를 계산하고 출력
print((a % c + b % c) % c)

# 위와 같은 계산을 다시 출력합니다. 결과는 동일
print((a % c + b % c) % c)

# (a를 c로 나눈 나머지 * b를 c로 나눈 나머지)를 c로 나눈 나머지를 계산하고 출력
print((a % c * b % c) % c)

# 위와 같은 계산을 다시 출력합니다. 결과는 동일
print((a % c * b % c) % c)
