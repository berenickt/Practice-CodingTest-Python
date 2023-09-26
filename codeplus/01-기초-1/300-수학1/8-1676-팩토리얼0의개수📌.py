# 💡 팩토리얼 0의 개수 📚 https://www.acmicpc.net/problem/1676
# 팩토리얼의 뒤에 연속된 0의 개수를 계산하는 함수를 정의
def calc(n, v):
    ans = 0
    i = v
    while i <= n:
        ans += n // i
        i *= v
    return ans


# 사용자로부터 정수 n을 입력받음
n = int(input())

# 함수 calc를 호출하여 n!의 뒤에 연속된 5의 개수를 계산하고 결과를 ans에 저장
ans = calc(n, 5)
print(ans)
