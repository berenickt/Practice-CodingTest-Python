# 💡 진법 변환 📚 https://www.acmicpc.net/problem/2745

# 문자열 STR와 진법 b를 입력받음
STR, b = input().split()
b = int(b)

result = 0

# 문자열 STR를 한 글자씩 처리
for char in STR:
    # 만약 문자가 '0'부터 '9' 사이에 있는 숫자라면, result에 현재 문자를 정수로 변환하여 더함
    if "0" <= char <= "9":
        result = result * b + (ord(char) - ord("0"))
    # 문자가 'A'부터 시작하는 대문자 알파벳인 경우, result에 현재 문자를 10진수 숫자로 변환하여 더함
    else:
        result = result * b + (ord(char) - ord("A") + 10)

# 최종 결과를 출력
print(result)
