# 💡 골드바흐 파티션 📚 https://www.acmicpc.net/problem/17103
"""
골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다
짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다
짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자.
두 소수의 순서만 다른 것은 같은 파티션이다.
각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력하는 프로그램
"""
# 소수를 체크하는 리스트를 초기화합니다. (인덱스는 0부터 1000000까지)
check = [False] * 1000001

# 소수를 저장할 리스트를 초기화
primes = []

# 에라토스테네스의 체 알고리즘을 사용하여 소수를 찾습니다
for i in range(2, 1000001):
    if check[i] == False:
        # 소수를 발견하면 primes 리스트에 추가
        primes.append(i)
        j = i + i
        while j <= 1000000:
            # 소수의 배수들을 체크
            check[j] = True
            j += i

# 테스트 케이스의 개수를 입력받음
TEST_CASE = int(input())

# 각 테스트 케이스를 처리
for _ in range(TEST_CASE):
    # 정수 n을 입력받음
    n = int(input())

    # 소수 쌍의 개수를 세기 위한 변수 result를 초기화
    result = 0

    # primes 리스트의 소수들을 반복하면서 소수 쌍을 찾습니다
    for p in primes:
        if n - p >= 2 and p <= n - p:
            # n - p가 2 이상이고, p가 n - p보다 작을 경우에만 검사
            if check[n - p] == False:
                # n - p가 소수인 경우, result를 증가
                result += 1
        # 조건을 만족하지 않으면 반복을 종료
        else:
            break

    # 소수 쌍의 개수를 출력
    print(result)
