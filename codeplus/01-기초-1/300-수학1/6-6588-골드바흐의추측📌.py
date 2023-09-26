# 💡 골드바흐의 추측 📚 https://www.acmicpc.net/problem/6588
# 소수 판별을 위한 최대 범위를 지정
MAX = 1000000

# 소수 여부를 저장하는 리스트를 생성하고, 초기값을 False로 설정
check = [0] * (MAX + 1)

# 0과 1은 소수가 아니므로 True로 표시
check[0] = check[1] = True

# 소수를 저장할 리스트를 생성
prime = []

# 에라토스테네스의 체 알고리즘을 사용하여 소수를 판별하고 소수를 prime 리스트에 추가
for i in range(2, MAX + 1):
    if not check[i]:
        prime.append(i)
        j = i + i
        # i의 배수들을 소수가 아닌 것으로 표시
        while j <= MAX:
            check[j] = True
            j += i

# prime 리스트의 첫 번째 요소를 제거
prime = prime[1:]

# 사용자로부터 입력을 계속 받고, 0이 입력되면 종료
while True:
    n = int(input())
    if n == 0:
        break
    for p in prime:
        # n에서 p를 뺀 숫자가 소수인 경우, 두 소수를 더해서 n을 만들 수 있으므로 출력
        if check[n - p] == False:
            print("{0} = {1} + {2}".format(n, p, n - p))
            break
