"""
함수는 프로그래밍에 있어 굉장히 중요하다.
코딩테스트에서 테스트 케이스가 입력된 뒤에 테스트 케이스만큼 
특정한 알고리즘을 수행한 결과를 반복적으로 출력하도록 
요구하는 문제가 출제되는 경우가 많다.

이럴 때는 문제 푸는 코드를 함수화하면 매우 효과적으로 풀 수 있다.
"""


#### (1) 더하기 기능(return)
def add(a, b):
    return a + b


print(add(3, 7))
# 👉🏽 10


#### (2) 더하기 기능(return 제거)
def add(a, b):
    print("함수의 결과: ", a + b)


add(3, 7)
# 👉🏽 10


#### (3) 더하기 기능(변수의 순서 바꾸기)
def add(a, b):
    print("함수의 결과: ", a + b)


add(b=7, a=3)
# 👉🏽 10

#### (4) 더하기 기능(global 변수 선언)
a = 0


def func():
    global a
    a = a + 1


for i in range(10):
    func()

print(a)
# 👉🏽 10


#### (5) 더하기 기능(람다표현식)
# lambda 매개변수 : 표현식
def add(a, b):
    return a + b


print(add(3, 7))
# 👉🏽 10

print((lambda a, b: a + b)(8, 7))
# 👉🏽 15
