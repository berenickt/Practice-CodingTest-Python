import heapq

"""힙
힙은 일종의 트리로 
수의 집합에서 가장 작은 수(키)나 가장 큰 수만을 자주 꺼내올때 유용한 자료구조

힙을 사용하는 이유
일반적인 리스트와 달리 push(), pop() 이후 자동 정렬
"""


# 최소 힙 생성, push
heap_list = []
heapq.heappush(heap_list, 4)
heapq.heappush(heap_list, 1)
heapq.heappush(heap_list, 7)
print(heap_list)  # [1, 4, 7]

# pop
heapq.heappop(heap_list)
print(heap_list)  # [4, 7]

# pop하지 않고 최솟값 얻기
print(heap_list[0])  # 4

# 기존 리스트를 힙으로 변환
a_list = [4, 1, 7, 3, 8, 5]
heapq.heapify(a_list)  # [1, 3, 5, 4, 8, 7]
