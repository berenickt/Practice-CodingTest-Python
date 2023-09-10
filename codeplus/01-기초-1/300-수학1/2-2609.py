# 💡 최대공약수와 최소공배수 📚 https://www.acmicpc.net/problem/2609
# 최대공약수(GCD)를 계산하는 함수를 정의
def gcd(x, y):
    # 만약 y가 0이라면 x를 반환, 이것이 GCD의 종료 조건
    if y == 0:
        return x
    # y가 0이 아니라면, x를 y로 나눈 나머지를 계산하여 재귀적으로 GCD 함수를 호출
    else:
        return gcd(y, x % y)


# 사용자로부터 두 개의 정수를 입력받고, 입력값을 공백을 기준으로 분리하여 정수 변수 a와 b에 할당합
a, b = map(int, input().split())

# 입력받은 두 정수 a와 b의 최대공약수(GCD)를 계산하고 출력
g = gcd(a, b)
print(g)

# a와 b의 최소공배수(LCM)를 계산하고 출력, LCM은 (a * b) / GCD 로 계산됨
print(a * b // g)
