"""스택(Stack)
스택은 박스쌓기에 비유할 수 있다.
흔히 Box를 쌓는 모습을 연상하면 되는데,
이러한 구조를 선입후출(First In Last Out) 또는 후입선출(Last In First Out) 구조라고 한다.

쉽게 말해, 먼저 들어온 수는 가장 나중에 나간다.
이때 시간복잡도는 O(1)이다.
"""
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
# 👉🏽 [5, 2, 3, 1]

print(stack[::-1])
# 👉🏽 [1, 3, 2, 5]

"""
파이썬에서 스택(Stack)을 이용할 때 별도의 라이브러리를 사용할 필요가 없다.
기본 리스트에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 작용한다.

1. append(): 가장 뒤쪽 데이터 삽입
2. pop(): 가장 뒤쪽 데이터를 꺼냄
"""
