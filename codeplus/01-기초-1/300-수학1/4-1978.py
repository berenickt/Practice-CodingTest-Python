# 💡 소수 찾기 📚 https://www.acmicpc.net/problem/1934
# 주어진 숫자 x가 소수인지 판별하는 함수를 정의
def is_prime(x):
    # x가 2보다 작으면 소수가 아니므로 False를 반환
    if x < 2:
        return False
    i = 2

    # i가 x의 제곱근보다 작거나 같을 때까지 반복
    while i * i <= x:
        # 만약 x가 i로 나누어 떨어진다면, x는 소수가 아니므로 False를 반환
        if x % i == 0:
            return False
        i += 1
    # 위의 조건을 모두 통과하면 x는 소수이므로 True를 반환
    return True


# 입력: 정수 n을 입력받음
n = int(input())

# 입력: 공백을 기준으로 분리된 정수 리스트를 입력받음
a = list(map(int, input().split()))

# 소수의 개수를 저장할 변수 ans를 초기화
ans = 0

# 입력 리스트 a의 각 원소에 대해 소수 판별 함수를 호출하고, 소수인 경우 ans를 1 증가
for x in a:
    if is_prime(x):
        ans += 1

# 소수의 개수인 ans를 출력
print(ans)
