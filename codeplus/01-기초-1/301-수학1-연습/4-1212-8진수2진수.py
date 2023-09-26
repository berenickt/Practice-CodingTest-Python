# 💡 8진수 2진수 📚 https://www.acmicpc.net/problem/1212
# 8진수를 이진수로 변환하기 위한 8진수-이진수 매핑 리스트를 생성
eight = ["000", "001", "010", "011", "100", "101", "110", "111"]

# 사용자로부터 문자열을 입력받음
STR = input()

start = True

# 이진수 변환 결과를 저장할 변수를 초기화
result = ""

# 입력된 문자열이 "0"인 경우, 결과를 "0"으로 설정
if STR == "0":
    result = "0"

# 입력된 문자열을 순회하면서 처리
for char in STR:
    # 문자를 숫자로 변환
    n = ord(char) - ord("0")

    # 시작 플래그인 start가 True이고, n이 4보다 작은 경우 처리
    if start and n < 4:
        if n == 0:
            continue
        elif n == 1:
            result += "1"
        elif n == 2:
            result += "10"
        elif n == 3:
            result += "11"
        # start 플래그를 False로 변경
        start = False
    else:
        # 8진수-이진수 매핑 리스트에서 이진수를 가져와 결과에 추가
        result += eight[n]

        # start 플래그를 False로 변경
        start = False

# 최종 변환된 이진수를 출력
print(result)
