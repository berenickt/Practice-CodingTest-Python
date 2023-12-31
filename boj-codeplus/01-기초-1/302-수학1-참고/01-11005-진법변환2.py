# 💡 진법 변환 2 📚 https://www.acmicpc.net/problem/11005

# 10진수 정수 n과 변환할 진법 b를 입력받음
n, b = map(int, input().split())

# 변환된 결과를 저장할 빈 문자열 result를 초기화
result = ""

# n이 0보다 클 때까지 반복 (진법 변환 진행)
while n > 0:
    # n을 b로 나눈 나머지(remain)를 구함
    remain = n % b

    # 나머지가 10 미만인 경우, 그대로 문자열에 추가
    if remain < 10:
        result += str(remain)
    # 나머지가 10 이상인 경우, A부터 시작하는 문자로 변환하여 문자열에 추가
    else:
        result += chr(remain - 10 + ord("A"))

    # n을 b로 나눈 몫을 새로운 n으로 설정
    n //= b

# 결과 문자열을 역순으로 만듬 (진법 변환 결과)
result = result[::-1]

# 변환된 결과를 출력
print(result)
