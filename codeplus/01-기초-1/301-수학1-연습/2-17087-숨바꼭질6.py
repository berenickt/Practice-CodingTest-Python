# 💡 숨바꼭질 6 📚 https://www.acmicpc.net/problem/17087
# 최대 공약수(GCD)를 계산하는 함수를 정의
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


# 정수 동생 N명과 수빈이의 초기 위치(S)를 입력받음
BRO_NUM, SUBIN_INIT_VALUE = map(int, input().split())

# 정수 동생 위치 리스트 broList를 입력받음
BRO_LIST = list(map(int, input().split()))

# 각 요소를 S(수빈이의 초기위치)와의 차이값으로 변환하여 업데이트
BRO_LIST = [abs(broLocation - SUBIN_INIT_VALUE) for broLocation in BRO_LIST]

# 최대 공약수를 계산할 변수 result를 broList의 첫 번째 요소로 초기화
result = BRO_LIST[0]

# 나머지 요소들과 result의 최대 공약수를 계산하여 result를 업데이트
for i in range(1, BRO_NUM):
    result = gcd(result, BRO_LIST[i])

print(result)
