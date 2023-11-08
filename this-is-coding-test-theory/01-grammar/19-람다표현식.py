"""(1) 람다표현식
함수를 간단하게 작성 가능
특정 긴으을 수행하는 함수를 한 줄에 작성 가능

문법
lambda 매개변수 : 표현식
"""


def add(a, b):
    return a + b


# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))

"""(2)
내장 함수에서 자주 사용되는 람다 함수
"""
array = [("홍길동", 50), ("이순신", 32), ("아무개", 74)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))  # [('이순신', 32), ('홍길동', 50), ('아무개', 74)]
print(sorted(array, key=lambda x: x[1]))

"""(3)
여러 개의 리스트에 적용
"""
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))  # [7, 9, 11, 13, 15]
