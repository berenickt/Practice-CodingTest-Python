"""개선된 소수(Prime Number) 
비효율적인 알고리즘을 개선해서 
시간복잡도를 최대로 줄여 효율적인 알고리즘으로 만들어보자.

자연수가 가지는 특징을 파악하고 있다면 그 원리를 쉽게 이해 할 수있다.
결론적으로 제곱근까지만(가운데 약수까지만) 확인하면 된다.

16이라는 수의 약수(Divisor)는 다음과 같다.
1 2 4 8 16

이때 모든 약수에 대해, 
가운데 약수를 기준으로 대칭적으로 2개씩 앞뒤로 묶어서 곱하면 16을 만들 수 있다.

1x16, 2x8, 4x4, 8x2, 16x1

분명한 점은 가운데 약수(4)를 기준으로 각 등식이 대칭적인 형태를 보인다는 것이다.

다음과 같이 코드를 작성하면 
시간복잡도가 O(X^1/2)인 절반(Half)에 가까운 시간을 줄일 수 있다.
"""


def is_prime_sqrt(n):
    # 제곱근 구하기 : math.sqrt 모듈을 써도 됨
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "소수 아님"
    return "소수임"


print(is_prime_sqrt(4))  # 👉🏽 소수 아님
print(is_prime_sqrt(7))  # 👉🏽 소수임
