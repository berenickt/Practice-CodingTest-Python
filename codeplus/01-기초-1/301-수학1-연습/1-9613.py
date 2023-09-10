# 💡 GCD 합 📚 @https://www.acmicpc.net/problem/9613
# 최대 공약수(GCD)를 계산하는 함수를 정의
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


# 테스트 케이스의 개수를 입력받음
TEST_CASE = int(input())

# 각 테스트 케이스를 처리
for _ in range(TEST_CASE):
    # 공백으로 구분된 정수 리스트를 입력받음
    a = list(map(int, input().split()))

    # 리스트의 첫 번째 요소를 n으로 저장하고, 나머지를 a로 저장
    n = a[0]
    a = a[1:]

    # 정답을 저장할 변수 ans를 초기화
    ans = 0

    # 모든 가능한 조합을 반복하여 최대 공약수를 계산하고 ans에 더함
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            ans += gcd(a[i], a[j])

    # 테스트 케이스의 정답을 출력
    print(ans)
