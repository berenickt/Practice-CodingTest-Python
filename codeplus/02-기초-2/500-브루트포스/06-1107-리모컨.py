# 💡 리모컨 📚 https://www.acmicpc.net/problem/1107
# 입력받은 두 개의 정수 n과 m을 각각 비밀번호의 길이와 비밀번호의 문자 개수로 간주하고
# 비밀번호를 구성하는 문자 중 깨진 문자의 개수를 최소화하는 비밀번호를 구하는 프로그램

# 입력받은 두 개의 정수를 각각 변수에 저장
n = int(input())
m = int(input())

# 깨진 문자를 저장할 리스트를 생성합니다
broken = [False] * 10

# m이 0이 아닌 경우 입력받은 비밀번호를 분석하여 깨진 문자를 저장
if m > 0:
    a = list(map(int, input().split()))
else:
    a = []
for x in a:
    broken[x] = True


# 비밀번호를 구성하는 문자 중 깨진 문자의 개수를 최소화하는 함수를 정의
def possible(c):
    if c == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if broken[c % 10]:
            return 0
        l += 1
        c //= 10
    return l


# 비밀번호를 구성하는 문자 중 깨진 문자의 개수를 최소화하는 비밀번호를 구함
ans = abs(n - 100)
for i in range(0, 1000000 + 1):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c - n)
        if ans > l + press:
            ans = l + press

# 구한 비밀번호를 출력
print(ans)
