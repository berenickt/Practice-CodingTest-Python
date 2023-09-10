# 💡 골드바흐 파티션 📚 https://www.acmicpc.net/problem/17103

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

    # 소수 쌍의 개수를 세기 위한 변수 ans를 초기화
    ans = 0

    # primes 리스트의 소수들을 반복하면서 소수 쌍을 찾습니다
    for p in primes:
        if n - p >= 2 and p <= n - p:
            # n - p가 2 이상이고, p가 n - p보다 작을 경우에만 검사
            if check[n - p] == False:
                # n - p가 소수인 경우, ans를 증가
                ans += 1
        # 조건을 만족하지 않으면 반복을 종료
        else:
            break

    # 소수 쌍의 개수를 출력
    print(ans)
