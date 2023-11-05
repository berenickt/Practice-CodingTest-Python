"""math() : 수학계산을 요구하는 기능
factorial, sqrt, gcd, pi, e등을 계산 할 수 있다.
"""
import math

#### (1) factorial(x)
print(math.factorial(5))
# 👉🏽 120

#### (2) sqrt(x): x의 제곱근
print(int(math.sqrt(49)))
# 👉🏽 7

#### (3) gcd(x): 최대 공약수
print(math.gcd(21, 14))
# 👉🏽 7

#### (4) 최소 공배수(LCM)을 구하기
print(21 * 14 // math.gcd(21, 14))
# 👉🏽 42

#### (5) 파이(pi) 출력
print(math.pi)
# 👉🏽 3.141592653589793

#### (6) 자연상수(e) 출력
print(math.e)
# 👉🏽 2.718281828459045
