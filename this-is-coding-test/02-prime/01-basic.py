"""소수(Prime Number) 
2보다 큰 자연수 중 
1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수

소수를 계산할때 가장 간단한 방법은 
X를 2부터 X - 1까지의 모든 수로 나누어 보는것

결론적으로 이 알고리즘의 시간복잡도는 O(X)이고 비효율적이다.
예를들어, input()값이 10,000,000이라고 가정하자.
계산 할 때는 2부터 9,999,999까지의 모든 수에 대해 하나씩 나누어야 한다.
"""


def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return "소수 아님"
        else:
            return "소수 임"


print(is_prime_number(4))  # 소수 아님
print(is_prime_number(7))  # 소수 임
