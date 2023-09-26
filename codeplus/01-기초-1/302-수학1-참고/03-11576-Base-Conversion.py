# 💡 Base Conversion 📚 https://www.acmicpc.net/problem/11576
def convert(num, base):
    # 재귀 종료 조건: num이 0인 경우 함수를 종료
    if num == 0:
        return
    # num을 base로 나눈 몫을 다시 convert 함수로 재귀 호출
    convert(num // base, base)
    # num을 base로 나눈 나머지를 출력하고, end=" "로 줄바꿈을 하지 않고 출력
    print(num % base, end=" ")


# 진법 a와 진법 b를 입력받음
a, b = map(int, input().split())

# 변환할 정수의 개수 n을 입력받음
n = int(input())

result = 0

# 변환할 정수들을 입력받아 리스트 num에 저장
num = list(map(int, input().split()))

# 리스트 num의 각 정수를 10진수로 변환하여 result에 누적
for x in num:
    result = result * a + x

# result를 진법 b로 변환하여 출력
convert(result, b)
