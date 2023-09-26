# 💡 소수 구하기 📚 https://www.acmicpc.net/problem/1929

# 소수 판별을 위한 최대 범위를 지정
MAX = 1000000

# 소수 여부를 저장하는 리스트를 생성하고, 초기값을 False로 설정
check = [0] * (MAX + 1)

# 0과 1은 소수가 아니므로 True로 표시
check[0] = check[1] = True

# 에라토스테네스의 체 알고리즘을 사용하여 소수를 판별
for i in range(2, MAX + 1):
    if not check[i]:
        j = i + i
        # i의 배수들을 소수가 아닌 것(True)으로 표시
        while j <= MAX:
            check[j] = True
            j += i

# 입력: 두 정수 m과 n을 입력받음
m, n = map(int, input().split())

# m부터 n까지의 범위에서 소수를 출력
for i in range(m, n + 1):
    if check[i] == False:
        print(i)
