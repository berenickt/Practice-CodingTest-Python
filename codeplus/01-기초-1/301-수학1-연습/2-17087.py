# 💡 숨바꼭질 6 📚 https://www.acmicpc.net/problem/17087
# 최대 공약수(GCD)를 계산하는 함수를 정의
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


# 정수 n과 s를 입력받습니다. n은 리스트의 길이, s는 기준값
n, s = map(int, input().split())

# 정수 리스트 a를 입력받음
a = list(map(int, input().split()))

# 리스트 a의 각 요소를 s와의 차이값으로 변환하여 리스트 a를 업데이트
a = [abs(x - s) for x in a]

# 최대 공약수를 계산할 변수 ans를 a의 첫 번째 요소로 초기화
ans = a[0]

# 나머지 요소들과 ans의 최대 공약수를 계산하여 ans를 업데이트
for i in range(1, n):
    ans = gcd(ans, a[i])

# 최종 결과인 ans를 출력
print(ans)
