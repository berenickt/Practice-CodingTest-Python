# 💡 2진수 8진수 📚 https://www.acmicpc.net/problem/1373
STR = input()
StrofLen = len(STR)
result = ""

# 문자열의 길이에 따라 3으로 나눈 나머지에 따라 처리

if StrofLen % 3 == 1:
    print(STR[0], end="")  # 첫 번째 문자를 그대로 출력

elif StrofLen % 3 == 2:
    # 첫 번째 문자와 두 번째 문자를 숫자로 변환하여 계산하여 출력
    print((ord(STR[0]) - ord("0")) * 2 + ord(STR[1]) - ord("0"), end="")

# 문자열 길이를 3으로 나눈 나머지부터 시작하여 3자리씩 끊어서 계산
for i in range(StrofLen % 3, StrofLen, 3):
    print(
        (ord(STR[i]) - ord("0")) * 4
        + (ord(STR[i + 1]) - ord("0")) * 2
        + (ord(STR[i + 2]) - ord("0")),
        end="",
    )
