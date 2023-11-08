from collections import deque
from collections import Counter

"""deque()
Queue라이브러리는 일반적인 큐 자료구조를 구현하는 라이브러리는 아니다. 
따라서, deque()를 이용해 큐를 구현해야 한다.
"""
data = deque([2, 3, 4])

data.appendleft(1)
data.append(5)

print(data)
# 👉🏽 deque([1, 2, 3, 4, 5])

print(list(data))
# 👉🏽 [1, 2, 3, 4, 5]


"""Counter() : 등장 횟수를 세는 기능
list iterable 객체가 주어졌을 때,
해당 객체 내부의 원소가 몇 번씩 등장했는지 알려준다
"""
counter = Counter(["red", "blue", "blue", "orange", "green", "blue", "green"])

print(counter["blue"])  # 'blue'가 등장한 횟수 출력 ===> 3
print(counter["green"])  # 'green'이 등장한 횟수 출력 ===> 2
print(dict(counter))  # 사전 자료형으로 반환
# => {'red': 1, 'blue': 3, 'orange': 1, 'green': 2}
