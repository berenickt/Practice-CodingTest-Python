"""
알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출련한 뒤에,
그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

e.g. K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

input #1
K1KA5CB7

output #1
ABCKK13
"""
str = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for s in str:
    # 알파벳인 경우 결과 리스트에 삽입
    if s.isalpha():
        result.append(s)
    # 숫자는 따로 더하기
    else:
        value += int(s)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print("".join(result))
