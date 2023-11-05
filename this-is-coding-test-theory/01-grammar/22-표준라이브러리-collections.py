"""deque()
Queue라이브러리는 일반적인 큐 자료구조를 구현하는 라이브러리는 아니다. 
따라서, deque()를 이용해 큐를 구현해야 한다.
"""
from collections import deque

data = deque([2, 3, 4])

data.appendleft(1)
data.append(5)

print(data)
# 👉🏽 deque([1, 2, 3, 4, 5])

print(list(data))
# 👉🏽 [1, 2, 3, 4, 5]


"""counter() : 등장 횟수를 세는 기능
list iterable 객체가 주어졌을 때,
해당 객체 내부의 원소가 몇 번씩 등장했는지 알려준다
"""
from collections import Counter

data_counter = ["red", "blue", "blue", "orange", "green", "blue", "green"]

print(Counter(data_counter))
# 👉🏽 Counter({'blue': 3, 'green': 2, 'red': 1, 'orange': 1})

print(dict(data_counter))
# 👉🏽 {'red': 1, 'blue': 3, 'orange': 1, 'green': 2}

print(counter["blue"])
# 👉🏽 3
