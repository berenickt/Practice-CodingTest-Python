# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42583
"""
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다.
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며,
다리는 weight 이하까지의 무게를 견딜 수 있습니다. 
단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 
다리가 견딜 수 있는 무게 weight, 
트럭 별 무게 truck_weights가 주어집니다.
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return

입력 #1
bridge_length : 2	
weight	      : 10
truck_weights : [7, 4, 5, 6]

출력 #1
8

큐를 다리라고 생각하고 공기(0)들을 미리 채운 다음에 
매 시간마다 pop 하고 
현재 다리 위의 무게에 따라 트럭을 push 하거나 공기(0)를 push 
queue를 양방향에서 처리해야 하기 때문에 양방형 처리에 유리한 deque를 사용

cf. 내부적으로 deque은 double-linked list로 구현되어 있음
그래서 양 끝 요소의 추가/삭제가 O(1)

collections는 유용한 자료구조를 제공하는 python의 표준 라이브러리
- rotate(1) 을 하면 오른쪽으로 이동
-- 즉, 제일 뒤에 있던게 제일 앞으로 이동
- rotate(-1)을 하면 왼쪽으로 이동합니다.
-- 즉, 제일 앞에 있던데 제일 뒤로 이동

popleft()
- pop(i) : i번째 인덱스를 삭제하는 연산
- 보통의 자료구조에서 pop() 연산이라고 하면 제일 끝에 요소가 삭제
- 이를 반대로 한 것이 바로 popleft()
- popleft()는 제일 끝 요소가 아니라 제일 앞의 요소가 삭제
"""


from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque(bridge_length * [0])  # deque([0, 0])
    truck_weights = deque(truck_weights)  # deque([7, 4, 5, 6])
    time = 0
    curWeight = 0

    while len(truck_weights) != 0:
        time += 1
        # 미리 뺴주어야함 (1초가 지날 때마다 무조건 하나는 빠지므로)
        curWeight -= bridge.popleft()

        if curWeight + truck_weights[0] <= weight:
            curWeight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

    # 방금 마지막 트럭이 들어갔으므로, 브릿지 길이만큼 더해줘야함.
    time += bridge_length
    return time


print(solution(2, 10, [7, 4, 5, 6]))
