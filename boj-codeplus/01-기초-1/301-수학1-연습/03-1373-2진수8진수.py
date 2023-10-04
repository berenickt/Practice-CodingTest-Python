# 💡 2진수 8진수 📚 https://www.acmicpc.net/problem/1373
"""
2진수를 3자리씩 뒤에서부터 끊으면, 8진수를 만들 수 있다.
• 11 | 001 | 100  (2진수 11001100)
•  3     1     4  (8진수 314)
"""
STR = input()
StrOfLen = len(STR)
result = ""

if StrOfLen % 3 == 1:
    # 첫 번째 문자를 그대로 출력
    print(STR[0], end="")

elif StrOfLen % 3 == 2:
    # 첫 번째 문자와 두 번째 문자를 숫자로 변환하여 계산하여 출력
    print((ord(STR[0]) - ord("0")) * 2 + ord(STR[1]) - ord("0"), end="")

# 문자열 길이를 3으로 나눈 나머지부터 시작하여 3자리씩 끊어서 계산
for i in range(StrOfLen % 3, StrOfLen, 3):
    print(
        (ord(STR[i]) - ord("0")) * 4
        + (ord(STR[i + 1]) - ord("0")) * 2
        + (ord(STR[i + 2]) - ord("0")),
        end="",
    )
