# 💡 팩토리얼 📚 https://www.acmicpc.net/problem/10872
""" 팩토리얼 (Factorial)
N! = 1 * 2 * ... * N
팩토리얼은 매우 큰 값
6!  = 720
8!  = 40320
10! = 3628800
"""
# 팩토리얼을 계산하는 재귀 함수를 정의
def factorial(n):
    # 종료 조건: 만약 n이 0이라면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출: n * (n-1)!을 반환
    else:
        return n * factorial(n - 1)


# 사용자로부터 정수 n을 입력받음
n = int(input())

# 입력받은 n에 대한 팩토리얼 값을 계산하고 출력
print(factorial(n))
