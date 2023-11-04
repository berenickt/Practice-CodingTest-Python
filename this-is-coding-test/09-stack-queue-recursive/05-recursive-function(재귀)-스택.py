"""재귀 함수의 수행은 스택(Stack) 자료구조를 이용한다.
함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야, 
그 앞의 함수 호출이 종료되기 때문이다.
(스택구조는 선입후출 방식이다.)

결론적으로 재귀함수는 내부적으로 스택 자료구조와 동일하다는 것만 기억하자.
재귀함수를 이용하는 문제는 대표적으로 팩토리얼(factorial) 문제가 있다.
팩토리얼문제는 반복문, 재귀함수방식으로 풀 수 있다.
"""


# 반복문
def for_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


print(for_factorial(5))
# 👉🏽 120


# 재귀함수
def recursive_factorial(n):
    if n <= 1:
        return 1
    return result * for_factorial(n - 1)


print(recursive_factorial(5))
# 👉🏽 120

"""
위의 코드를 비교했을때 재귀 함수의 코드가 더 간결하다는 것을 알 수 있다.
이렇게 간결해진 이유는 재귀 함수가 수학의 점화식(재귀식)을 그대로 소스코드로 옮겼기 때문이다.

수학의 점화식은 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것을 의미한다. 
이 개념은 이후 배울 8장의 다이나믹 프로그래밍으로 이어지기 때문에 중요하다.
"""
