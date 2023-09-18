# 💡 조합 0의 개수 📚 https://www.acmicpc.net/problem/2004
# 팩토리얼의 뒤에 연속된 특정 소인수 (2 또는 5) 의 개수를 계산하는 함수를 정의
def calc(n, v):
    ans = 0
    i = v
    while i <= n:
        ans += n // i
        i *= v
    return ans


# 2의 지수와 5의 지수를 계산할 변수를 초기화
two = 0
five = 0

# 사용자로부터 두 개의 정수 n과 m을 입력받음
n, m = map(int, input().split())

# n!의 뒤에 연속된 2의 개수를 계산
two += calc(n, 2)

# (n-m)!의 뒤에 연속된 2의 개수를 빼줌
two -= calc(n - m, 2)

# m!의 뒤에 연속된 2의 개수를 빼줌
two -= calc(m, 2)

# n!의 뒤에 연속된 5의 개수를 계산
five += calc(n, 5)

# (n-m)!의 뒤에 연속된 5의 개수를 빼줌
five -= calc(n - m, 5)

# m!의 뒤에 연속된 5의 개수를 빼줌
five -= calc(m, 5)

# 연속된 2와 5 중에서 더 작은 값을 선택하여 출력
print(min(two, five))
