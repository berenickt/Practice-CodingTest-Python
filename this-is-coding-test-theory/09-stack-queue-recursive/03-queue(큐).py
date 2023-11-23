"""큐(Queue)
큐는 놀이공원에 입장하는 대기 줄에 비유할 수 있다.
새치기가 없다고 가정하면 먼저 줄은 선 사람은 먼저 놀이기구를 탑승 할 수 있다.
이러한 구조를 선입선출(First In First Out) 구조라고 한다.
"""
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순서대로 출력
# 👉🏽 deque([3, 7, 1, 4])
print(list(queue))
# 👉🏽 [3, 7, 1, 4]

queue.reverse()  # 다음 출력을 위해 역순으로 바꾸기
print(queue)  # 나중에 들어온 원소부터 출력
# 👉🏽 deque([4, 1, 7, 3])
print(list(queue))
# 👉🏽 [4, 1, 7, 3]

"""
파이썬으로 queue를 구현할때는 collection에서 제공하는 deque 자료구조를 활용하자.
deque는 스택과 큐의 장점을 모두 채택한 것인데,
데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 
queue 라이브러리를 이용하는 것보다 더 간단하다.
deque 객체를 리스트 자료형으로 변경할때는 마지막에 list()를 붙여주자.
"""
