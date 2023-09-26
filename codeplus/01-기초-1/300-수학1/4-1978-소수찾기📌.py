# 💡 소수 찾기 📚 https://www.acmicpc.net/problem/1978
"""
소수 : 1과 자기자신을 제외하면 자연수 중에서 어떤 숫자로도 나누어 떨어지지 않는 숫자
e.g. 3, 5, 7 (1은 소수에 포함되지 않는다)

1과 자기자신을 제외한 약수가 존재하는지 확인하려면, 
자기자신의 제곱근(루트)까지만 확인하면 된다는 뜻이다.
어차피 약수들이 대칭적으로 짝을 이루기 때문에.
그러므로 25의 절반인 즉 루트25인 5까지만 나눠떨어지는지 확인하면 
해당 숫자가 소수인지 아닌지를 알 수 있다.
"""


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

# 소수의 개수를 저장할 변수 result를 초기화
result = 0

# 입력 리스트 a의 각 원소에 대해 소수 판별 함수를 호출하고, 소수인 경우 ans를 1 증가
for x in a:
    if is_prime(x):
        result += 1

# 소수의 개수인 result를 출력
print(result)
